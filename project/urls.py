
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from app.views import (register_complete_view, addItem, login_view, register_view, logout_view, home_view, auction_view, getItems_view, profile_view, bidding_view)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(
            template_name="app/password_reset.html"
            ), 
        name="password_reset"),
    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name="app/password_reset_done.html"
        ), 
        name="password_reset_done"),
     path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name="app/password_reset_confirm.html"
        ), 
        name="password_reset_confirm"),
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(
            template_name="app/password_reset_complete.html"
            ), 
        name="password_reset_complete"),
    path('health', lambda request: HttpResponse('okay')),
    path('login/', LoginView.as_view(template_name = 'app/login.html'), name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('auction/', auction_view, name='auction'),
    path('register_complete', register_complete_view, name='register_complete'),
    path('profile/<int:id>/', profile_view, name='profile'),
    path('biddingview/<int:id>/', bidding_view, name='biddingview'),
    path('getItems.json', getItems_view, name='getItems_view'),
    path('addItem/', addItem, name='addItem'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
