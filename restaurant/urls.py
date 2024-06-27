from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token
# router = DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('items/', MenuItemsView.as_view()),
    path('items/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]
