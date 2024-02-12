from rest_framework import viewsets,filters
from .models import CheckoutInfo,Payment
from .serializers import CheckoutSerializer,PaymentSerializer
from rest_framework.filters import OrderingFilter, SearchFilter

import environ
env = environ.Env()
environ.Env.read_env()


class CheckoutCreate(viewsets.ModelViewSet):
    queryset = CheckoutInfo.objects.all()
    serializer_class = CheckoutSerializer


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import stripe

stripe.api_key = env("STRIPE_API_KEY")

@csrf_exempt  
def create_payment_intent(request):
    if request.method == "POST":
        data = json.loads(request.body)
        price = data.get("price")
        amount = int(price * 100)

        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=amount,
                currency="usd",
                payment_method_types=["card"]
            )

            return JsonResponse({
                "clientSecret": payment_intent.client_secret
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)


if __name__ == '__main__':
    app.run(port=4242)



class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email']