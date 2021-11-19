from rest_framework import serializers
from .models import Client, Contract, Event


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
