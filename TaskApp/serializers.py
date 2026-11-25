from django.contrib.auth.models import User
from TaskApp.models import TaskDB
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskDB
        fields = "__all__"
        read_only_fields = ["id","user"]