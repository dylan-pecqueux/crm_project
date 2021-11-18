from rest_framework import serializers
from .models import User, Client, Contract, Event


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "team", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"


class ContractDetailSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Contract
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class EventDetailSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Event
        fields = "__all__"


class EventPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["attendees", "event_date", "notes"]
