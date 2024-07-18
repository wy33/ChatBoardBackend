from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from message.models import Message
from .serializers import MessageSerializer

@api_view(["GET"])
def getMessages(request):
    """Returns the 10 most recent messages in JSON as a response"""
    messages = Message.objects.order_by("-createdAt")[:10]
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def postMessage(request):
    """Post to database
    Returns 201 response if successful"""
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)    # Created successfully
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Fail: bad request