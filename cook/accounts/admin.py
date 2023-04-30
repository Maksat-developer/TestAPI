from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django import forms

from accounts.models import User


class UserCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'is_superuser', 'is_staff']

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    list_display = ['id', 'username', 'email', 'is_admin']
    search_fields = ()
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("email",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_admin",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", )}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", 'password', 'email'),
            },
        ),
    )


admin.site.register(User, UserAdmin)
