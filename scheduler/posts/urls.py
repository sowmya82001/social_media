from django.urls import path
from .views import home, schedule_post, dashboard
from .views import CustomLoginView, CustomLogoutView, schedule_post, dashboard
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('schedule/', schedule_post, name='schedule_post'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)