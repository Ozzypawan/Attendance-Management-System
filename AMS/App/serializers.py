from rest_framework import serializers
from .models import UserAuth

class UserAuthSerializers(serializers.ModelSerializer):
    class meta:
        model = UserAuth
        fields = '__all__'