from django.contrib import admin
from django.urls import path
from student.views import StudentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentView.as_view(), name='students'),
]
