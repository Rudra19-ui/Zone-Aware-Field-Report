from rest_framework import serializers
from .models import FieldReport, Zone
from django.utils import timezone
import datetime

class FieldReportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldReport
        fields = ['title', 'description', 'latitude', 'longitude']

    def create(self, validated_data):
        user = self.context['request'].user
        lat = validated_data['latitude']
        lng = validated_data['longitude']

        zone = Zone.objects.filter(
            min_lat__lte=lat,
            max_lat__gte=lat,
            min_lng__lte=lng,
            max_lng__gte=lng
        ).first()

        if not zone:
            raise serializers.ValidationError("No zone found for given coordinates.")

        now = timezone.localtime()
        is_risky = now.time() > datetime.time(18, 0)

        return FieldReport.objects.create(
            zone=zone,
            submitted_by=user,
            is_risky=is_risky,
            **validated_data
        )


class FieldReportViewSerializer(serializers.ModelSerializer):
    zone = serializers.StringRelatedField()

    class Meta:
        model = FieldReport
        fields = '__all__'


class ReportStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=['APPROVED', 'REJECTED'])
