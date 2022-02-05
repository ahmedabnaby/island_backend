from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from island import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryView, 'category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#imp for what you want to achieve.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)