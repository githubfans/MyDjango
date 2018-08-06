from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):

    list_display = ('kodebarang', 'namabarang', 'created_by', 'updated_at')
    # actions = notne

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            stock = form.save(commit=False)
            stock.created_by = request.user
            import datetime
            stock.updated_at = datetime.datetime.now()
            stock.save()
            suffix = stock.namabarang.replace(' ', '')
            suffix = suffix.decode('utf-8').lower()
            stock.kodebarang = '{0}.{1}.{2}' . format(suffix[:3], stock.created_by_id, stock.id)
            stock.save()

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(created_by=request.user)

    # def has_change_permission(self, request, obj=None):
    #     if not obj:
    #         # the changelist itself
    #         return True
    #     return obj.user == request.user


admin.site.register(Post, PostAdmin)
