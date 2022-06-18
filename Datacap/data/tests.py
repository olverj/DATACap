from django.test import TestCase
from django.contrib.auth.models import User
from .models import Demographic, Treatment, Baseline, Diagnostic, Administration
from .forms import DemogForm, BaseForm, TxForm, DiagForm, TimepointForm
from django.urls import reverse
import datetime

# Model Tests Here

class DemographicSubjectTest(TestCase):
    def setUp(self):
        self.name = Demographic(subject = 'Darrel Durian')

    def test_substring(self):
        self.assertEqual(str(self.name), 'Darrel Durian')

    def test_tablename(self):
        self.assertEqual(str(Demographic._meta.db_table), 'demographics')

class TreatmentNameTest(TestCase):
    def setUp(self):
        self.tx = Treatment(tx_name = 'Memory Enhancement')

    def test_substring(self):
        self.assertEqual(str(self.tx), 'Memory Enhancement')

    def test_tablename(self):
        self.assertEqual(str(Treatment._meta.db_table), 'treatment')

class BaselineTest(TestCase):
    def test_tablename(self):
        self.assertEqual(str(Baseline._meta.db_table), 'baseline')

class DiagnosticNameTest(TestCase):
    def setUp(self):
        self.diag = Diagnostic(diag_name = 'CBC')

    def test_substring(self):
        self.assertEqual(str(self.diag), 'CBC')
    
    def test_tablename(self):
        self.assertEqual(str(Diagnostic._meta.db_table), 'diagnostics')

class AdministrationTest(TestCase):
    def setUp(self):
        self.tp = Administration(timepoint = 'Day 0')
    
    def test_substring(self):
        self.assertEqual(str(self.tp), 'Day 0')

    def test_tablename(self):
        self.assertEqual(str(Administration._meta.db_table), 'timepoints')

# Forms Test

class NewDemogForm(TestCase):
    def test_demogform(self):
        data = {
            'subject' : 'Ernie Elderberry',
            'dob' : '2000-01-01'
        }
        form = DemogForm(data)
        self.assertTrue(form.is_valid)

class NewBaseForm(TestCase):
    def test_baseform(self):
        data = {
            'subject_baseline' : 'Frank Fig',
            'study_tx' : 'Treatment',
            'user' : 'user',
            'screen_date' : '2022-01-01',
            'disease_name' : 'Disease',
            'disease_dxdate' : '2020-01-01',
            'past_mh' : 'History'
        }
        form = BaseForm(data)
        self.assertTrue(form.is_valid)

class NewTxForm(TestCase):
    def test_txform(self):
        data = {
            'tx_name' : 'Treatment',
            'tx_type' : 'Type',
            'tx_description' : 'Description',
            'tx_admin_type' : 'Administration'
        }
        form = TxForm(data)
        self.assertTrue(form.is_valid)

class NewDiagForm(TestCase):
    def test_diagform(self):
        data = {
            'diag_name' : 'CBC',
            'subject_diagnostics' : 'subject',
            'user' : 'user',
            'dx_tx' : 'treatment',
            'diag_date' : '2022-01-01',
            'diag_coll_time' : '13:00',
            'labname1' : 'RBC',
            'labval1' : '42'
        }
        form = DiagForm(data)
        self.assertTrue(form.is_valid)

class NewTpForm(TestCase):
    def test_timepointform(self):
        data = {
            'timepont' : 'Day 0',
            'subject_administration' : 'Greg Gord',
            'admin_tx' : 'treatment',
            'user' : 'user',
            'admin_date' : '2022-01-01',
            'admin_starttime' : '12:00',
            'admin_endtime' : '12:44',
            'admin_description' : 'description'
        }
        form = TimepointForm(data)
        self.assertTrue(form.is_valid)

# Authorization Tests

class NewTimepointAuthTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser1', password = 'password')
        self.subject = Demographic(subject = 'Hiram Hazelnut')
        self.subject.save()
        self.treat = Treatment(tx_name = 'Treatment')
        self.treat.save()
        self.tp = Administration.objects.create(
            timepoint = 'day 0',
            subject_administration = self.subject,
            admin_tx = self.treat,
            user = self.test_user,
            admin_date = '2022-01-01',
            admin_starttime = '12:00',
            admin_endtime = '12:12',
            admin_description = 'description'
        )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newtimepoint'))
        self.assertRedirects(response, '/accounts/login/?next=/data/newtimepoint/')

class LoginTest(TestCase):
    def test_login_template(self):
        response = self.client.get(reverse('loginmessage'))
        self.assertTemplateUsed(response, 'data/loginmessage.html')