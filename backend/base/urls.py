from django.urls import path
from . import views

# router = routers.DefaultRouter()
# router.register(r'users', views.userViewSet)

urlpatterns = [
    path('images/', views.images, name='images'),
    path('images/<pk>', views.getImage, name='getImage'),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]