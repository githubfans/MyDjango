from django.contrib import admin
from .models import Tenant


class TenantAdmin(admin.ModelAdmin):

    list_display = ('id', 'domain_url', 'schema_name', 'name')
    # actions = notne

    # def get_queryset(self, request):
    #     qs = super(TenantAdmin, self).get_queryset(request)
    #     return qs.filter(created_by=request.user)

    # def has_change_permission(self, request, obj=None):
    #     if not obj:
    #         # the changelist itself
    #         return True
    #     return obj.user == request.user


admin.site.register(Tenant, TenantAdmin)
