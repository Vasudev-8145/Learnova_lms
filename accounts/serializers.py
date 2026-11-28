
from rest_framework import serializers

from accounts.models import User,TrainerProfile

class TrainerSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","email","password","phone","role"]

        read_only_fields = ["id","role"]

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data,role="trianer")

class StudentSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","email","password","phone","role"]

        read_only_fields = ["id","role"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data,role="student")
           
class TrainerProfileSerializer(serializers.ModelSerializer):

    trainer = serializers.StringRelatedField()

    class Meta:

        model = TrainerProfile

        fields = "__all__"

        read_only_fields = ["id","trainer","created_at","updated_at"]
        