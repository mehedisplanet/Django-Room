
from django.urls import path
from .views import user_logout
from .views import UserRegistrationView, UserLoginView,UserBankAccountUpdateView
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    # path('logout/', UserLogoutView.as_view(), name='logout'),
    path('logout/', user_logout, name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' )
]