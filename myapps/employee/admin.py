from django.contrib import admin
from .models import Profile, Employee


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass


class EmployeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Employee, EmployeeAdmin)
