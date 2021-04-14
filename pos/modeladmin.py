from django.contrib import admin

class ShowIdAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
