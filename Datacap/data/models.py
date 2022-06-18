from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Demographic (models.Model):
    subject = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.subject
    
    class Meta:
        db_table = 'demographics'

class Treatment (models.Model):
    tx_name = models.CharField(max_length=255)
    tx_type = models.CharField(max_length=255)
    tx_description = models.TextField(blank=True)
    tx_admin_type = models.CharField(max_length=255)

    def __str__(self):
        return self.tx_name
    
    class Meta:
        db_table = 'treatment' 

class Baseline (models.Model):
    subject_baseline = models.ForeignKey(Demographic, on_delete=models.CASCADE)
    study_tx = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    screen_date = models.DateField(null=True, blank=True)
    disease_name = models.CharField(max_length=255)
    disease_dxdate = models.DateField(null=True, blank=True)
    past_mh = models.TextField(blank=True)

    def __str__(self):
        return self.study_tx

    class Meta:
        db_table = 'baseline'
    
class Diagnostic (models.Model):
    diag_name = models.CharField(max_length=255)
    subject_diagnostics = models.ForeignKey(Demographic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dx_tx = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    diag_date = models.DateField(null=True, blank=True)
    diag_coll_time = models.TimeField(null=True, blank=True)
    labname1 = models.CharField(max_length=50, null=True, blank=True)
    labval1 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    labname2 = models.CharField(max_length=50, null=True, blank=True)
    labval2 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    labname3 = models.CharField(max_length=50, null=True, blank=True)
    labval3 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    labname4 = models.CharField(max_length=50, null=True, blank=True)
    labval4 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    labname5 = models.CharField(max_length=50, null=True, blank=True)
    labval5 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    labname6 = models.CharField(max_length=50, null=True, blank=True)
    labval6 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    labname7 = models.CharField(max_length=50, null=True, blank=True)
    labval7 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    labname8 = models.CharField(max_length=50, null=True, blank=True)
    labval8 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    labname9 = models.CharField(max_length=50, null=True, blank=True)
    labval9 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.diag_name
    
    class Meta:
        db_table = 'diagnostics'

class Administration (models.Model):
    timepoint = models.CharField(max_length=255)
    subject_administration = models.ForeignKey(Demographic, on_delete=models.CASCADE)
    admin_tx = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    admin_date = models.DateField(null=True, blank=True)
    admin_starttime = models.TimeField(null=True, blank=True)
    admin_endtime = models.TimeField(null=True, blank=True)
    admin_description = models.TextField(blank=True)

    def __str__(self):
        return self.timepoint
    
    class Meta:
        db_table = 'timepoints'