from django.urls import path
from . import views

app_name = 'librarians'

urlpatterns = [
    path('login', views.login_librarian, name='login'),
    path('logout', views.logout_librarian, name='logout'),
]