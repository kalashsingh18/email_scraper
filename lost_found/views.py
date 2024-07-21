# your_app/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from .serializer import EmailSerializer

@api_view(['POST'])
def send_email_view(request):
    serializer = EmailSerializer(data=request.data)
    
    if serializer.is_valid():
        email = serializer.validated_data['email']
        
        # Send the email
        send_mail(
            'MATCH FOUND!',
            'for your listed item the match is found',
            'dhananjaymva@gmail.com',
            [email],
            fail_silently=False,
        )
        
        return Response({'message': 'Email sent successfully!'}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
