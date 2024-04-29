from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PaymentSerializer
from .paystack import Paystack, Verify
from .model import Payment
import os
from dotenv import load_dotenv

load_dotenv()

class PayView(APIView):
    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['user'].email
            amount = serializer.validated_data['amount']
            paystack = Paystack(email, amount)
            payment_result = paystack.pay()
            if payment_result != "404":
                serializer.save(reference=payment_result['reference_id'], status="PENDING")
                # Create a Payment object with PENDING status
                payment = serializer.instance
                # Initiate payment verification
                verifier = Verify(payment.reference, os.environ.get('PAYSTACK'))
                status = verifier.status()
                # Update payment status based on verification result
                if status == "successful":
                    payment.status = Payment.TRANSACTION_STATUS.SUCCESSFUL
                elif status == "failed":
                    payment.status = Payment.TRANSACTION_STATUS.FAILED
                # Save the updated payment status
                payment.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("Payment initialization failed", status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
