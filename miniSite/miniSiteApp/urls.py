from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ArticleView


urlpatterns = [
    path('', views.index, name='index'),
    path('maqola/<int:pk>/', ArticleView.as_view(), name='batafsil'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)