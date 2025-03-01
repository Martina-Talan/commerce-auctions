from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import NewForm, BidForm, CommentForm
from django.contrib.auth.decorators import login_required
from .models import User, Listing, Category, Bids, Comment


def index(request):
    listings = Listing.objects.all()

    return render(request, "auctions/index.html", {  
        "listings": listings
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def new_listing(request):
# Create a new listing
    if request.method == "GET":
        form = NewForm()
        return render(request, "auctions/new_listing.html",{
            "form": form
        })
    else:
        form = NewForm(request.POST)
        user = request.user
        if form.is_valid():
           listing = form.save()
           listing.listed_by = user
           listing.save()
    
        return HttpResponseRedirect(reverse("index"))


def category(request):
# Show all listing in a certain category
    if request.method == "GET":
        categories = Category.objects.all()
        category_id = request.GET.get("category", 0)
        listings = Listing.objects.filter(sold=False)
        if category_id:
            listings= Listing.objects.filter(category_id=category_id)

    return render (request, "auctions/category.html", {
        "listings": listings,
        "categories": categories,
        "category_id": int(category_id)
    })

   
def listing(request, listing_id):
# Show listing by id
    if request.method == "GET":
        user =request.user
        listing = Listing.objects.get(pk=listing_id)

        return render(request, "auctions/open.html",{
            "listing": Listing.objects.get(pk=listing_id),
            "comments": Comment.objects.filter(listing=listing_id),
            "bid_form": BidForm(),
            "comment_form": CommentForm(),
            "watchlist": listing.watchlist.all(),
            "bid_counter": Bids.objects.filter(listing=listing_id).count(),
        })


@login_required
def watchlistAdd(request,listing_id):
# Add listing to a watchlist
    if request.method == "POST":
       listing = Listing.objects.get(pk=listing_id)
       listing.watchlist.add(request.user)
       listings = request.user.watchlist.all()
    return render(request, "auctions/watchlist.html",{
        "listings": listings,
    })
  

@login_required   
def watchlist(request):
# Show all listings added to a watchlist
    user = request.user
    listings = request.user.watchlist.all()

    return render(request, "auctions/watchlist.html",{
        "listings": listings,
    })
        

@login_required
def watchlistDelete(request,listing_id):
# Remove listing from a watchlist
    listing = Listing.objects.get(pk=listing_id)
    listing.watchlist.remove(request.user)

    return HttpResponseRedirect(reverse("listing", args=[listing.id]))


@login_required
# Allow user to place a bid 
def bids(request, listing_id):
    if request.method == "POST":
       bid_form = BidForm()
       listing= Listing.objects.get(pk=listing_id)
       current_bid = request.POST["current_bid"]
       
       # Check if the bid value is higher than the initial price
       if float(current_bid) > float(listing.starting_bid):
               newBid = Bids(
               user = request.user,
               current_bid = current_bid)
               newBid.save()
               # if the bid is valid, change the price to the value of a current bid
               listing.all_bids.add(newBid)
               listing.starting_bid = current_bid
               listing.save()
               messages.info(request, 'You have successfully added your bid!')
               return HttpResponseRedirect(reverse("listing", args=[listing.id]))
       else:
             messages.info(request, "Your bid amount is too low! Please try again")
             return HttpResponseRedirect(reverse("listing", args=[listing.id]))
             
            
    return HttpResponseRedirect(reverse("listing", args=[listing.id]))
        
     
@login_required         
def comments(request, listing_id):
    # Add a comment to the listing
    if request.method == "POST":
           comment_form = CommentForm()
           listing= Listing.objects.get(pk=listing_id)
           comment = Comment(
           user = request.user,
           comment = request.POST["comment"],
           listing = listing)
           comment.save()
     
    return HttpResponseRedirect(reverse("listing", args=[listing.id]))


@login_required
def closeListing(request, listing_id): 
# Close the listing
    if request.method == "POST":
          listing = Listing.objects.get(pk=listing_id)
          if request.user == listing.listed_by:
             listing.sold = True
             listing.save()

    return HttpResponseRedirect(reverse("listing", args=[listing.id]))
    


        
    



    

       

       
