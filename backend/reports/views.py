from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import FieldReport
from .serializers import (
    FieldReportCreateSerializer,
    FieldReportViewSerializer,
    ReportStatusSerializer
)
from .permissions import IsFieldExecutive, IsSupervisor


# POST /api/reports/
class CreateReportView(generics.CreateAPIView):
    serializer_class = FieldReportCreateSerializer
    permission_classes = [IsAuthenticated, IsFieldExecutive]


# GET /api/reports/my/
class MyReportsView(generics.ListAPIView):
    serializer_class = FieldReportViewSerializer
    permission_classes = [IsAuthenticated, IsFieldExecutive]

    def get_queryset(self):
        return FieldReport.objects.filter(submitted_by=self.request.user)


# GET /api/reports/zone/
class ZoneReportsView(generics.ListAPIView):
    serializer_class = FieldReportViewSerializer
    permission_classes = [IsAuthenticated, IsSupervisor]

    def get_queryset(self):
        return FieldReport.objects.filter(
    zone__supervisor=self.request.user
)



# PATCH /api/reports/{id}/status/
class UpdateReportStatusView(generics.GenericAPIView):
    serializer_class = ReportStatusSerializer
    permission_classes = [IsAuthenticated, IsSupervisor]

    def patch(self, request, id):
        report = get_object_or_404(FieldReport, id=id)

        if report.zone not in request.user.zone_set.all():
            return Response(
                {"error": "Cannot access reports outside your zone"},
                status=status.HTTP_403_FORBIDDEN
            )

        if report.submitted_by == request.user:
            return Response(
                {"error": "Cannot review your own report"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        report.status = serializer.validated_data['status']
        report.save()

        return Response({"message": "Status updated successfully"})
