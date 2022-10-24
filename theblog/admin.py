from django.contrib import admin
from .models import Post, Category, Profile, Comment
from django.utils.safestring import mark_safe

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'header_image', 'status','post_date', 'category')
    list_filter = ('status','category',)
    search_fields = ['title', 'content']
    list_editable = ['category']

    # admin后台缩略图显示
    def header_image(self, obj):
        try:
            img = mark_safe('<img src="%s" width="50px" />' % (obj.file.url,))
        except Exception as e:
            img = ''
            return img
    header_image.short_description = 'Thumb'
    header_image.allow_tags = True

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)