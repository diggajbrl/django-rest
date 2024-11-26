from django.urls import path
from .views import StudentListApiView, StudentDetailView

urlpatterns = [
    path ('', StudentListApiView.as_view(), name = 'Student-List-View'),
    path ('<int:pk>/', StudentDetailView.as_view(), name = 'Student-Details')
]