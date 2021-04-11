from django.urls import include, path
from rest_framework import routers
from . import views, financeviews

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'promotion', views.ProductPromotionViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'payment', financeviews.PaymentViewSet)
router.register(r'sales', financeviews.SalesTransactionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/createsales', financeviews.CreateSalesTransactionView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
