from rest_framework.serializers import ModelSerializer
from app1.models import bus_details

class bus_Serializer(ModelSerializer):
    class Meta:
        model=bus_details
        fields='__all__'
        