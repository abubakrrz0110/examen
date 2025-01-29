from django.urls import path
from django.contrib import admin
from apps.views import UserCreateView, UserSigninView, LogOutView
from django.conf.urls.static import static
from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserCreateView.as_view(), name='signup'),
    path('signin/', UserSigninView.as_view(), name='signin'),
    path('logout/', LogOutView.as_view(), name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
