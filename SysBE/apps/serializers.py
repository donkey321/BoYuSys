from rest_framework import serializers
from apps.models import *
from User.serializers import UserSerializer
from User.models import CustomUser
import pprint


class UdIdSerializers(serializers.ModelSerializer):
    class Meta:
        model = UdId
        fields = ('id', 'content', 'remark')

