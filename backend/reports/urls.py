from django.urls import path
from .views import (
    CreateReportView,
    MyReportsView,
    ZoneReportsView,
    UpdateReportStatusView
)

urlpatterns = [
    path('reports/', CreateReportView.as_view()),
    path('reports/my/', MyReportsView.as_view()),
    path('reports/zone/', ZoneReportsView.as_view()),
    path('reports/<int:id>/status/', UpdateReportStatusView.as_view()),
]
