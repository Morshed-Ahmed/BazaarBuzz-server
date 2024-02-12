from django.urls import path,include
from .views import CheckoutCreate,create_payment_intent,PaymentViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('checkout', CheckoutCreate)
router.register('payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-payment-intent/', create_payment_intent, name='create_payment_intent'),
]