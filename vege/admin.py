from django.contrib import admin
from .models import *
# Register your models here.
from .models import *
admin.site.register(Receipe)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)
class SubjectMarkAdmin(admin.ModelAdmin):
    list_display=['student','subject','marks']

admin.site.register(Subject_marks,SubjectMarkAdmin)
# we have to register the 