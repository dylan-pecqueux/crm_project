from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Contract, Client, Event
from .forms import UserAdminChangeForm, UserAdminCreationForm


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ["id", "first_name", "last_name", "email"]
    list_filter = ["groups"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("groups", "is_staff")}),
    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password", "password_2")}),
    )
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = ()


class ContractAdmin(admin.ModelAdmin):
    list_display = ["id", "client", "sales_contact", "status"]


class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "company_name", "sales_contact"]


class EventAdmin(admin.ModelAdmin):
    list_display = ["id", "event_date", "client", "support_contact"]


admin.site.register(User, UserAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Event, EventAdmin)
