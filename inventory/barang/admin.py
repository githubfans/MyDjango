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
            currentDT = datetime.datetime.now()
            stock.updated_at = currentDT
            stock.save()
            stock.kodebarang = '{0}.{1}' . format(stock.created_by_id, stock.id)
            stock.save()


admin.site.register(Post, PostAdmin)
