from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from apps.serializers import *
from apps.models import *
from rest_framework import permissions
from rest_framework_simplejwt import authentication

class UdIdView(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTTokenUserAuthentication]
    queryset = UdId.objects.all()
    serializer_class = UdIdSerializers

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
