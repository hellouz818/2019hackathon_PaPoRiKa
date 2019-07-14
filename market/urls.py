from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.store, name='store'),
    path('new/', views.new, name='new'),
    path('postcreate', views.postcreate, name='postcreate'),
    path('<int:post_id>', views.detail, name="detail"),
    path('edit', views.edit, name='edit'),
    path('postupdate/<int:post_id>', views.postupdate, name='postupdate'),
    path('postdelete/<int:post_id>', views.postdelete, name='postdelete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)