from django.contrib import admin

from .models import User, Listing, Category, Comment, Bids

# Register your models here.

class ListingAdmin(admin.ModelAdmin):

    fields = ( "title","description","image_url","category", "starting_bid", "listed_by")

admin.site.register(User)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Bids)


