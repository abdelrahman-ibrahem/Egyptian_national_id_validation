from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from .util.generic import validate_egyptian_id, extract_data_from_id
from .models import APIRequestLog
from .serializers import IDValidationSerializer, APIRequestLogSerializer
from .util.pagination import StandardPagination

class ValidateIDView(generics.GenericAPIView):
    """
    Validate Egyptian national ID and extract data
    """
    permission_classes = [IsAuthenticated]
    serializer_class = IDValidationSerializer
    
    def post(self, request):
        serializer = IDValidationSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                {'is_valid': False, 'error': serializer.errors['id_number'][0]},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        id_number = serializer.validated_data['id_number']
        extracted_data = extract_data_from_id(id_number)
        
        return Response({
            'is_valid': True,
            'extracted_data': extracted_data
        })


class ListLogs(generics.ListAPIView):
    """
    List API request logs 
    """
    serializer_class = APIRequestLogSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardPagination  # Use the pagination class properly

    def get_queryset(self):
        return APIRequestLog.objects.select_related('user').order_by('-timestamp')
