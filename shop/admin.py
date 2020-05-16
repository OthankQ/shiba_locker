from django.contrib import admin

# Register your models here.
from .models import UserAdditionalInfo, Item, Invoice, LineItem
from django.contrib.auth.admin import UserAdmin


class InvoiceInline(admin.TabularInline):
    model = Invoice
    extra = 1


class LineItemInline(admin.TabularInline):
    model = LineItem
    extra = 3


class UserAdditionalInfoAdmin(admin.ModelAdmin):
    fieldsets = [('General Information', {'fields': (
        'user_id', 'name', 'phone_number', 'password')}), ]
    inlines = [InvoiceInline]


class InvoiceAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ('date', 'status', 'user')})]
    inlines = [LineItemInline]


class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('name', 'desc', 'price', 'stock', 'image_id')})]


# admin.site.register(User, UserAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Item, ItemAdmin)
