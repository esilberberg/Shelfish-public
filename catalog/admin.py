from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 
                    'pub_year',
                    'author', 
                    'isbn',
                    'date_created',
                    'location')
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'first_name', 'birth_year', 'death_year')

class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'term')

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Language, LanguageAdmin)