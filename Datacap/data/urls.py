from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demographics/', views.demographics, name = 'demographics'),
    path('demodetails/<int:id>', views.demodetails, name = 'demodetails'),
    path('baselinedetails/<int:id>', views.medhistory, name = 'baseline'),
    path('diagnosticdetails/<int:id>', views.diagnosticdetails, name = 'diagnostics'),
    path('administrationdetails/<int:id>', views.details, name = 'timepoints'),
    path('treatments/', views.treatments, name = 'treatments'),
    path('treatmentdetail/<int:id>', views.treatmentdetail, name = 'txdetails'),
    path('newtstudy/', views.newTreatment, name = 'newstudy'),
    path('newhistory/', views.newHistory, name = 'newhistory'),
    path('newsubject/', views.newSubject, name = 'newsubject'),
    path('newdiagnostic/', views.newDiagnostic, name = 'newdiagnostic'),
    path('newtimepoint/', views.newTimepoint, name = 'newtimepoint'),
    path('loginmessage/', views.loginmessage, name = 'loginmessage'),
    path('logoutmessage/', views.logoutmessage, name = 'logoutmessage'),
]