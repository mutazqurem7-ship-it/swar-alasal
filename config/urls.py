from django.contrib import admin
from django.urls import path
from clothes.views import product_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list), # هذا يجعل الصفحة الرئيسية تعرض منتجاتك
    path('offers/', views.offers, name='offers'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
