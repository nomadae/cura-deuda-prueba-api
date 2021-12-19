from rest_framework import serializers
from zipcodes.models import *


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = (
            'name',
            'state_code',
            'is_active'
        )


class MunicipalitySerializer(serializers.HyperlinkedModelSerializer):
    state = serializers.StringRelatedField()

    class Meta:
        model = Municipality
        fields = (
            'name',
            'municipality_code',
            'state',
            'is_active'
        )


class SuburbSerializer(serializers.HyperlinkedModelSerializer):
    municipality = serializers.StringRelatedField()
    class Meta:
        model = Suburb
        fields = (
            'name',
            'zip_code',
            'settlement_type',
            'zone_type',
            'municipality',
            'is_active'
        )
