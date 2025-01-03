
from django.urls import path

from djangoBestFootballCardCollectibles.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, \
    ProfileDetailView, ProfileUpdateView, DeactivateProfileView, ProfilesView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('details/', ProfileDetailView.as_view(), name='details'),
    path('edit/', ProfileUpdateView.as_view(), name='edit'),
    path('delete/', DeactivateProfileView.as_view(), name='delete-profile'),
    path('seller/<int:pk>/', ProfilesView.as_view(), name='profile-pk'),
]
