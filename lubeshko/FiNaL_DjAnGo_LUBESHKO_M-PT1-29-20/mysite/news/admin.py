from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "photo", "title", 'category', "created_at", "update_at", "is_pblished")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_editable = ('is_pblished',) #Поля для редактирования в админке
    list_filter =  ("created_at", "is_pblished", 'category') #Фильтр в админке


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title",)
    list_display_links = ("id", "title",)
    search_fields = ("title",)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin) # НЕ ЗАБУДЬ ТУТ ПРОПИСАТЬ
