from django.urls import path

from table import views

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('table', views.employee_table, name='employee-table'),
    path('edit/<int:pk>', views.EmployeeUpdateView.as_view(), name='employee-table-edit'),
    path('delete/<int:pk>', views.delete_emp, name='employee-table-delete'),
]
