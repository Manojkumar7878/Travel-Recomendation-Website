"""
URL configuration for project4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from app3 import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'busroutes', views.BusRouteViewSet)
router.register(r'bookings', views.BookingViewSet, basename='booking')
router.register(r'places', views.PlaceViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="index1"),
    path('booking1', (views.booking), name="booking"),
    path('mybooking', (views.mybooking), name="mybooking"),
    path('search/', views.search_bus, name='search_bus'),
    path('place_list1', views.place_list, name="place_list"),
    path('hire_bus1', (views.hire_bus), name="hire_bus"),
    path('help1', views.help, name="help"),
    path('about1', views.about, name="about"),
    path('login1', views.login, name="login"),
    path('signup1', views.signup, name="signup"),
    path('updateData/<int:id>', (views.updateData), name='updateData'),
    path('deleteData/<int:id>', (views.deleteData), name='deleteData'),
    path('logout/', views.logout_view, name='logout'),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



