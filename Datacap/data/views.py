from django.shortcuts import render, get_object_or_404
from .forms import DemogForm, BaseForm, TxForm, DiagForm, TimepointForm
from .models import Demographic, Baseline, Diagnostic, Treatment, Administration
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'data/index.html')

def treatments(request):
    tx_name = Treatment.objects.all()
    return render(request, 'data/treatments.html', {'tx_name' : tx_name})

def treatmentdetail(request, id):
    tx = get_object_or_404(Treatment, id=id)
    treatmentname = tx.tx_name
    treatmenttype = tx.tx_type
    treatmentdescription = tx.tx_description
    administrationtype = tx.tx_admin_type
    context = {
        'tx' : tx,
        'treatmentname' : treatmentname,
        'treatmenttype' : treatmenttype,
        'treatmentdescription' : treatmentdescription,
        'administrationtype' : administrationtype,
    }
    return render(request, 'data/treatmentdetail.html', context)

def demographics(request):
    subject = Demographic.objects.all()
    return render(request, 'data/demographics.html', {'subject' : subject})

def demodetails(request, id):
    study_tx = Baseline.objects.all().filter(study_tx__id=id)
    diag_name = Diagnostic.objects.all().filter(subject_diagnostics__id = id)
    timepoint = Administration.objects.all().filter(subject_administration__id=id)
    context = {
        'study_tx' : study_tx,
        'diag_name' : diag_name,
        'timepoint' : timepoint,
    }
    return render(request, 'data/demodetails.html', context)

def medhistory(request, id):
    base = get_object_or_404(Baseline, id=id)
    subjectname = base.subject_baseline
    treatment = base.study_tx
    screeningdate = base.screen_date
    diseasename = base.disease_name
    diagnosisdate = base.disease_dxdate
    pastmedhistory = base.past_mh
    context = {
        'base' : base,
        'subjectname' : subjectname,
        'treatment' : treatment,
        'screeningdate' : screeningdate,
        'diseasename' : diseasename,
        'diagnosisdate' : diagnosisdate,
        'pastmedhistory' : pastmedhistory,
    }
    return render(request, 'data/baselinedetails.html', context)

def diagnosticdetails(request, id):
    diag = get_object_or_404(Diagnostic, id=id)
    diagnosticname = diag.diag_name
    subjectname = diag.subject_diagnostics
    treatmentname = diag.dx_tx
    collectiondate = diag.diag_date
    collectiontime = diag.diag_coll_time
    labname1 = diag.labname1
    labvalue1 = diag.labval1
    labname2 = diag.labname2
    labvalue2 = diag.labval2
    labname3 = diag.labname3
    labvalue3 = diag.labval3
    labname4 = diag.labname4
    labvalue4 = diag.labval4
    labname5 = diag.labname5
    labvalue5 = diag.labval5
    labname6 = diag.labname6
    labvalue6 = diag.labval6
    labname7 = diag.labname7
    labvalue7 = diag.labval7
    labname8 = diag.labname8
    labvalue8 = diag.labval8
    labname9 = diag.labname9
    labvalue9 = diag.labval9
    context = {
        'diag' : diag,
        'diagnosticname' : diagnosticname,
        'subjectname' : subjectname,
        'treatmentname' : treatmentname,
        'collectiondate' : collectiondate,
        'collectiontime' : collectiontime,
        'labname1' : labname1,
        'labvalue1' : labvalue1,
        'labname2' : labname2,
        'labvalue2' : labvalue2,
        'labname3' : labname3,
        'labvalue3' : labvalue3,
        'labname4' : labname4,
        'labvalue4' : labvalue4,
        'labname5' : labname5,
        'labvalue5' : labvalue5,
        'labname6' : labname6,
        'labvalue6' : labvalue6,
        'labname7' : labname7,
        'labvalue7' : labvalue7,
        'labname8' : labname8,
        'labvalue8' : labvalue8,
        'labname9' : labname9,
        'labvalue9' : labvalue9,
    }
    return render(request, 'data/diagnosticdetails.html', context)

def details(request, id):
    tp = get_object_or_404(Administration, id=id)
    timepoint = tp.timepoint
    subjectname = tp.subject_administration
    studytreatment = tp.admin_tx
    administrator = tp.user
    administrationdate = tp.admin_date
    starttime = tp.admin_starttime
    endtime = tp.admin_endtime
    adminoutcome = tp.admin_description
    context = {
        'tp' : tp,
        'timepoint' : timepoint,
        'subjectname' : subjectname,
        'studytreatment' : studytreatment,
        'administrator' : administrator,
        'administrationdate' : administrationdate,
        'starttime' : starttime,
        'endtime' : endtime,
        'adminoutcome' : adminoutcome,
    }
    return render(request, 'data/administrationdetails.html', context)

@login_required
def newSubject(request):
    form = DemogForm

    if request.method == 'POST':
        form = DemogForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = DemogForm()
    else:
        form = DemogForm()
    return render(request, 'data/newsubject.html', {'form' :form})

@login_required
def newHistory(request):
    form = BaseForm

    if request.method == 'POST':
        form = BaseForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = BaseForm()
    else:
        form = BaseForm()
    return render(request, 'data/newhistory.html', {'form' :form})

@login_required
def newTreatment(request):
    form = TxForm

    if request.method == 'POST':
        form = TxForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = TxForm()
    else:
        form = TxForm()
    return render(request, 'data/newstudy.html', {'form' :form})

@login_required
def newDiagnostic(request):
    form = DiagForm

    if request.method == 'POST':
        form = DiagForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = DiagForm()
    else:
        form = DiagForm()
    return render(request, 'data/newdiagnostic.html', {'form' :form})

@login_required
def newTimepoint(request):
    form = TimepointForm

    if request.method == 'POST':
        form = TimepointForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = TimepointForm()
    else:
        form = TimepointForm()
    return render(request, 'data/newtimepoint.html', {'form' :form})

def loginmessage(request):
    return render(request, 'data/loginmessage.html')

def logoutmessage(request):
    return render(request, 'data/logoutmessage.html')