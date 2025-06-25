from django.contrib import admin
from home.models import Author,Books,UserProfile

# Register your models here.
class BooksInline(admin.TabularInline):
    model = Books
    extra = 1

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id","author_name",)
    search_fields = ("author_name",)
    inlines =(BooksInline,)


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ("id","book_name","book_price","published_date","written",)
    search_fields = ("book_name",)
    list_filter = ("published_date",)
    readonly_fields = ("published_date","book_price","written",)
    # exclude = ("published_date","published_date",)

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ("user","phone_number","otp",)

    
    













