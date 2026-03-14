from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import detect_scam

@api_view(['POST'])
def detect(request):
    text = request.data.get("text", "")
    result = detect_scam(text)
    return Response(result)