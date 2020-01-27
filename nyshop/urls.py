from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import list_item, register_item, register_company, detail_item, detail_company, list_company

urlpatterns = [
    path('', list_item, name='list_item'),
    path('registerItem/', register_item, name='register_item'),
    path('registerItem/<int:pk>/', detail_item, name='detail_item'),
    path('registerComp/', register_company, name='register_company'),
    path('registerComp/<int:pk>/', detail_company, name='detail_company'),
    path('Comp/', list_company, name='list_company'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)