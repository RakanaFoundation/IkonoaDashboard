from django.urls import include, path
from rest_framework import routers
from pos.views import views, financeviews, shipmentviews, inventoryviews

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'promotion', views.ProductPromotionViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'payment', financeviews.PaymentViewSet)
router.register(r'sales', financeviews.SalesTransactionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.F

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/createsales', financeviews.CreateSalesTransactionView.as_view()),
    path('api/v1/createsalesretur', financeviews.CreateReturSalesTransactionView.as_view()),
    path('api/v1/createfaktur', shipmentviews.CreateFakturView.as_view()),
    path('api/v1/createrequestorder', shipmentviews.CreateRequestOrder.as_view()),
    path('api/v1/updatestatusrequestorder', shipmentviews.UpdateStatusRequestOrder.as_view()),
    path('api/v1/createsentorder', shipmentviews.CreateSentOrder.as_view()),
    path('api/v1/updatestatussentorder', shipmentviews.UpdateStatusSentOrder.as_view()),
    path('api/v1/createreturnorder', shipmentviews.CreateReturnOrder.as_view()),
    path('api/v1/createreturnfromsentorder', shipmentviews.CreateReturnOrderFromSentOrder.as_view()),
    path('api/v1/updatestatusreturnorder', shipmentviews.UpdateReturOrderSerializers.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/productinventory', inventoryviews.CabangInventoryViews.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view())
]
