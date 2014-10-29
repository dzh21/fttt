from django.contrib import admin
from tasks42.models import Person, RequestObject

admin.site.register(Person)


class RequestObjectAdmin(admin.ModelAdmin):
    pass
    #list_display = ('id', 'save_date_time', 'remote_address', )
    #date_hierarhy = ('save_date_time',)

admin.site.register(RequestObject, RequestObjectAdmin)