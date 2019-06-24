from django.contrib import admin
from home.models import Book,Movie,Novel,Author,Genre,library

# Register your models here.

""" admin.site.register(Book)
admin.site.register(Movie)
admin.site.register(Novel)
admin.site.register(Genre)
admin.site.register(Author) """



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
   search_fields=('id','Movie')
   list_filter=('Director','Producer')

@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(library)
class libraryAdmin(admin.ModelAdmin):
    list_filter=('Branch','IssueDate')




