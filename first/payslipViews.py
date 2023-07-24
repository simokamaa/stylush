from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
import csv
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import ManagerForm, EmployeesForm,DailyWorkForm, CommisionSalaryForm, FixedSalaryForm, AllowancesForm, DeductionsForm, SalaryDetailsForm, JobTypeForm, CommissionTemplatesForm, ManageSalaryForm, SelectDepartmentForm, PayrollSummaryForm, AdvanceSalaryForm, OvertimeForm, EmployeeAwardForm, AddExpensesForm, DepartmentForm , first_departmentForm
from .models import Manager, Employees, Commision_saraly, Fixed_saraly, allowances, deductions, salary_details, job_type, commission_templates, ManageSalary, SelectDepartment, PayrollSummary, AdvanceSalary,  overtime, employeeAward, addExpenses, Department,DailyWork,first_department
from fpdf import FPDF
from .models import Transaction
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.template.loader import get_template
from xhtml2pdf import pisa



    
def generatePayslip(request):
    employees = Employees.objects.all()
    return render(request,'Dashboard/generatePayslip.html', {'employees' : employees})
      


def generate_payslip(request):
    # Get the required data for the payslip (replace with your own logic to fetch the data)
    company_name = "STYLUSH HAIR AND BEAUTY COLLEGE"
    employee = "Simon"
    generation_date = "May 25, 2023"
    tax_amount = "Kshs 100.00"
    allowance = "Kshs 500.00"
    commission = "Kshs 200.00"
    company_logo = "static/img/logo.png"

    # Create a dictionary to pass the data to the template
    payslip_data = {
        'company_name': company_name,
        'employee': employee,
        'generation_date': generation_date,
        'tax_amount': tax_amount,
        'allowance': allowance,
        'commission': commission,
        'company_logo': company_logo,
    }

    # Render the payslip template with the provided data
    template = get_template('Dashboard/payslip_template.html')
    payslip_html = template.render(payslip_data)

    # Create a PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="payslip.pdf"'

    # Generate the PDF from the HTML using xhtml2pdf library
    pisa_status = pisa.CreatePDF(payslip_html, dest=response)

    # Check if PDF generation was successful
    if pisa_status.err:
        return HttpResponse('PDF generation failed.')

    return response