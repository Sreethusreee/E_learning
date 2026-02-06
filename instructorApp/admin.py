from django.contrib import admin
from instructorApp.models import User,Category,Course,Module,Lesson,Cart,Order
# Register your models here.
admin.site.register(User )
admin.site.register(Category )
class ModuleModel(admin.ModelAdmin):
    exclude=['order']
admin.site.register(Module,ModuleModel)
class LessonModel(admin.ModelAdmin):
    exclude=['order']
admin.site.register(Lesson,LessonModel )


class CourseModel(admin.ModelAdmin):
    exclude=['owner'] 

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner=request.user
        return super().save_model(request, obj, form, change)

admin.site.register(Course,CourseModel) 
admin.site.register(Cart)   
admin.site.register(Order)   
