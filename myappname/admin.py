from django.contrib import admin
from .models import Book, Publisher, User, BookClub, ProfilePhoto, BookImage
# Register your models here.

# admin.site.register(Publisher)
# admin.site.register(User)
# admin.site.register(Book)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id','profile_pic','username','name','date_added','last_login','gender'
    )

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        'id','name',
    )

@admin.register(ProfilePhoto)
class ProfilePhotoAdmin(admin.ModelAdmin):
    list_display = (
        'id','image','date_added'
    )

@admin.register(BookClub)
class BookClubAdmin(admin.ModelAdmin):
    list_display = (
        'id','name',
    )

@admin.register(BookImage)
class BookImageAdmin(admin.ModelAdmin):
    list_display = (
        'id','image','date_added'
    )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'book_image','sku','name','publisher','author','date_published','date_added'
    )