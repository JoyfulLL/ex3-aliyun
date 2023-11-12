from django.utils.safestring import mark_safe
from .models import Resume
from django.contrib import admin
from .models import Ad
# Register your models here.
admin.site.register(Ad)


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'personID', 'birth', 'edu', 'school',
                    'major', 'position', 'image_data')

    def image_data(self, obj):
        return mark_safe(u'<img src="%s" width="120px" />' % obj.photo.url)

    image_data.short_description = u'个人照片'


admin.site.register(Resume, ResumeAdmin)
