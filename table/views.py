from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .models import Employee

from .forms import EmployeeUpdateForm


def employee_table(request):
    employee_list = Employee.objects.all()
    print(employee_list)  # getting whole list
    print(request.user)  # getting user
    context = {
        'employee_list': employee_list,
        'title': "Employee List",
    }
    return render(request, 'employee-table.html', context)


# edit
class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeUpdateForm
    success_url = reverse_lazy('employee-table')
    template_name = 'employee_edit.html'

    success_message = "Employee was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["title"] = "Update Product Information"
        context["nav_bar"] = "product_list"
        return context


# delete
def delete_emp(request, pk):
    Employee.objects.get(id=pk).delete()
    return redirect('employee-table')
