from django.contrib import admin
from django.urls import path, include
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('market/', include('market.urls')),
    path('msg/', include('msg.urls')),
    path('', account.views.home, name="home"),
]