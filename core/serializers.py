from rest_framework import serializers
from datetime import datetime

class DifferenceSerializer(serializers.Serializer):
    datetime: serializers.DateTimeField = serializers.DateTimeField()
    value: serializers.IntegerField = serializers.IntegerField()
    number: serializers.IntegerField = serializers.IntegerField()
    occurrences: serializers.IntegerField = serializers.IntegerField()
    last_datetime: serializers.DateTimeField = serializers.DateTimeField()
