from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language


class BooksInline(admin.TabularInline):
    model = Book


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('basic', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )


admin.site.register(Genre)
admin.site.register(Language)

# admin.site.register(Book)
# admin.site.register(Book, BookAdmin)
# admin.site.register(BookInstance)
# admin.site.register(BookInstance, BookInstanceAdmin)
# admin.site.register(Author)
# admin.site.register(Author, AuthorAdmin)





