from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LoginView
from cases.views import HomePageView


urlpatterns = [ 
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
    path('accounts/', include('allauth.urls')),
    path('accounts/login', LoginView.as_view(), name="login"),
    path('staff/', include('staff.urls', namespace="staff")),
    path('cases/', include('cases.urls', namespace="cases")),
    path('users/', include('users.urls', namespace="users")),
]

if settings.DEBUG == int(True):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)