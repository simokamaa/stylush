from django.urls import path,include

from . import mathViews
from . import views
from . import payslipViews
from . import balancesheetViews
from . import employeesViews
from . import expensesViews
from . import overtimeViews
from . import dailyrecordViews
from . import departmentViews
from . import awardViews
from . import uploadViews
from . mathViews import calculate_salary
from . import settingsViews 

urlpatterns = [
    path('', views.index, name='index'),
    path('addemployee/', employeesViews.addEmployee, name='addEmployee'),
    path('deleteAllemployees', employeesViews.deleteAllEmployees, name='deleteAllEmployees'),
    path('removeemployee/', employeesViews.employeeList , name='removeEmployee'),
    path('employees/create/', employeesViews.addEmployee, name='employee_create'),
    path('employees/<int:pk>/', employeesViews.employee_detail, name='employee_detail'),
    path('employees/<int:pk>/update/',employeesViews. employee_update, name='employee_update'),
    path('employees/<int:pk>/employee_delete/', employeesViews.employee_delete, name='employee_delete'),
    path('employeeList/', employeesViews.employeeList, name='employeeList'),
    path('salarytemplates/',views.salaryTemplates, name='salaryTemplates'),
    path('jobadd/', views.commisionTemplates, name='commisionTemplates' ),
    path('jobtypes', views.jobTypes, name='jobtypes'),
    path('jobtypes_delete/', views.jobtypes_delete, name  = 'jobtypes_delete'),
    path('managesalary/', views.manageSalary , name='manageSalary'),
    path('employeeSalaryList', views.employeeSalaryList, name='employeeSalaryList'),
    path('makepayment/', views.makePayment, name = 'makePayment'),
    path('payslip/', payslipViews.generate_payslip, name='generate_payslip'),
    path('payrollsummary/', views.payrollSummary, name='payrollSummary'),
    path('advanceSalary/', views.advanceSalary, name='advanceSalary'),
    path('advancesalary_list/', views.advancesalary_list, name='advancesalary_list'),
    path('advancesalary_delete_all/', views.advancesalary_delete_all, name='advancesalary_delete_all'),
    path('providentfund/', views.providentFund, name='providentFund'),
    path('overtime/', overtimeViews.overtime, name='overtime'),
    path('overtime_list/', overtimeViews.overtime_list, name='overtime_list'),
    path('create/', overtimeViews.overtime_create, name='overtime_create'),
    path('update/<int:pk>/', overtimeViews.overtime_update, name='overtime_update'),
    path('delete/<int:pk>/', overtimeViews.overtime_delete, name='overtime_delete'),
    path('employeeaward/', awardViews.employeeCreateAward, name='employeeAward'),
    path('award_list/', awardViews.award_list, name='award_list'),
    path('create/', awardViews.award_create, name='award_create'),
    path('update/<int:pk>/', awardViews.award_update, name='award_update'),
    path('delete/<int:pk>/', awardViews.award_delete, name='award_delete'),
    path('addDepartment/', departmentViews.addDepartment, name='addDepartment'),
    path('removedepartment/<int:pk>/', departmentViews.removeDepartment, name='removeDepartment'),
    path('manageDepartments/', departmentViews.departmentList, name='manageDepartments'), 
    path('departmentlist/', departmentViews.departmentList, name='departmentList'),
    path('department_view/', departmentViews.department_view, name='department_view'),
    path('departments_delete/', departmentViews.departments_delete, name='departments_delete'),
    path('dailyreports/', views.dailyReports, name='dailyReports'),
    path('monthlyReports/', views.monthlyReports, name='monthlyReports'),
    path('yearlyReport/', views.yearlyReports, name='yearlyReports'),
    path('balanceSheet/', balancesheetViews.balance_sheet,name='balanceSheet'),
    path('profile/', views.profile, name='profile'),
    path('profileDelete/', views.profileDelete, name="profileDelete"),
    path('addExpenses/', expensesViews.addMoreExpenses, name='addExpenses'),
    path('expense_list/', expensesViews.expense_list, name='expense_list'),
    path('create/', expensesViews.expense_create, name='expense_create'),
    path('update/<int:pk>/', expensesViews.expense_update, name='expense_update'),
    path('delete/<int:pk>/', expensesViews.expense_delete, name='expense_delete'),
    path('commisionList/', views.commisionList, name="commisionList"),
    path('makepaymentlist/', views.makePaymentList, name="makePaymentList"),
    path('manageSalaryList/', views.manageSalaryList, name="manageSalaryList"),
    path('dailyRecord/create/', dailyrecordViews.dailyRecord , name = "dailyRecord"),
    path('dailyRecordList/', dailyrecordViews.dailyRecordList, name='dailyRecordList'),
    path('dailyworks/create/', dailyrecordViews.dailyRecord , name='dailywork_create'),
    path('dailyworks/<int:pk>/', dailyrecordViews.dailywork_detail, name='dailywork_detail'),
    path('dailyworks/<int:pk>/update/', dailyrecordViews.dailywork_update, name='dailywork_update'),
    path('dailyworks/<int:pk>/delete/', dailyrecordViews.dailywork_delete, name='dailywork_delete'),
    path('dailyworks_delete/', dailyrecordViews.dailyworks_delete, name='dailyworks_delete'),
    path('needhelp/', views.needHelp, name="needHelp"),
    path('settings/', settingsViews.settings, name= "settings"),
    path('logout/', views.logout, name='logout'),
    path('generatePayslip/', payslipViews.generatePayslip, name="generatePayslip"),
    path('search/', views.search_bar, name = "search_bar"),
    path('company_account/',settingsViews.company_account, name="company_account" ),
    path('company_account_deleteAll/', settingsViews.company_account_deleteAll, name='company_account_deleteAll'),
    path('math/', mathViews.calculate_income, name='calculate_income'),
    path('calculate_income/', views.calculate_income, name='calculate_income'),
    path('personalAccount/', views.personalAccount, name = "personalAccount"),
    path('employeee_initializer/', views.employeee_initializer, name='employeee_initializer')
]

