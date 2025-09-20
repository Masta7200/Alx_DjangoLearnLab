# django-models/admin_view.py
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

def is_admin(user):
    """
    Check if the logged-in user has an Admin role.
    """
    return hasattr(user, "profile") and user.profile.role == "Admin"


@login_required
@user_passes_test(is_admin)
def admin_view(request):
    """
    Admin-only view: Only accessible if user.profile.role == 'Admin'
    """
    return render(request, "admin_view.html", {
        "title": "Admin Dashboard",
        "user_role": request.user.profile.role
    })
