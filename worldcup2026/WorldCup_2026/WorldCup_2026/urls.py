from django.contrib import admin
from django.urls import path
from user_management.views import login_view, register, logout_view, my_profile
from teams.views import teams, team_detail, player_detail, techs, players, can, us, mex
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('login', login_view, name="login"),
    path('register', register, name="register"),
    path('home', views.home, name="home"),
    path('logout/', logout_view, name="logout"),
    path('my_profile', my_profile, name="my_profile"),
    path('teams', teams, name="teams"),
    path('teams/<int:id>/', team_detail, name='team_detail'),
    path('player/<int:id>/', player_detail, name='player_detail'),
    path('techs/', techs, name='techs'),
    path('players/', players, name='players'),
    path('cities/canada', views.canada, name='cities_canada'),
    path('cities/united-states', views.us, name='cities_us'),
    path('cities/mexico', views.mexico, name='cities_mx'),
    path('cities/can', can, name='city_can'),
    path('cities/us', us, name='city_us'),
    path('cities/mx', mex, name='city_mex'),
    path('no-access/', views.no_access_view, name='no_access'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
