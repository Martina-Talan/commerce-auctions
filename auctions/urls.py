from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("category", views.category, name="category"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("watchlistAdd/<int:listing_id>", views.watchlistAdd, name="watchlistAdd"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlistDelete/<int:listing_id>", views.watchlistDelete, name="watchlistDelete"),
    path("bids/<int:listing_id>", views.bids, name="bids"),
    path("comments/<int:listing_id>", views.comments, name="comments"),
    path("closeListing/<int:listing_id>", views.closeListing, name="closeListing"),
]


