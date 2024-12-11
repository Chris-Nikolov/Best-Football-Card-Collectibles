
from django.urls import path

from djangoBestFootballCardCollectibles.reports.views import ReportCreateView, ReportListView, ReportDeleteView

urlpatterns = [
    path('create-report/<int:card_id>/', ReportCreateView.as_view(), name='create-report'),
    path('report-page', ReportListView.as_view(), name='report-page'),
    path('report-delete/<int:pk>/', ReportDeleteView.as_view(), name='report_delete')
]
