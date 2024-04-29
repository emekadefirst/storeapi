from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as rest_status  # Rename the imported status variable to avoid conflict
from .serializers import PaymentSerializer
from .paystack import Paystack, Verify
import os
from dotenv import load_dotenv

load_dotenv()

sk = os.environ.get('PAYSTACK')

class PayView(APIView):
    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['user'].email
            amount = serializer.validated_data['amount']
            paystack = Paystack(email, amount, sk)
            payment_result = paystack.pay()
            # Construct a Response object with the payment result
            return Response(payment_result, status=rest_status.HTTP_200_OK)
        else:
            # If serializer is not valid, return a Response with serializer errors
            return Response(serializer.errors, status=rest_status.HTTP_400_BAD_REQUEST)
        
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as rest_status
from .paystack import Verify
from .model import Payment

class PaymentVerificationView(APIView):
    def post(self, request, format=None):
        reference = request.data.get('reference')

        # Retrieve the payment object based on the reference
        try:
            payment = Payment.objects.get(reference=reference)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=rest_status.HTTP_404_NOT_FOUND)

        # Initialize Verify object
        verifier = Verify(reference, sk)

        # Call the status method to verify payment status
        payment_status = verifier.status()

        # Update the payment status in the database
        if payment_status == "successful":
            payment.status = Payment.TRANSACTION_STATUS.SUCCESSFUL
        elif payment_status == "pending":
            payment.status = Payment.TRANSACTION_STATUS.PENDING
        else:
            payment.status = Payment.TRANSACTION_STATUS.FAILED

        # Save the updated payment object
        payment.save()

        return Response({"status": payment_status}, status=rest_status.HTTP_200_OK)

