from django.urls import path

from djangoapp.b4c.views import SignupView, add_member, OrganizationsView

urlpatterns = [
    path('signup', SignupView.as_view(), name="signup"),
    path('member/add', add_member, name="add-member"),
    path('organizations', OrganizationsView.as_view(), name="organizations"),
]
