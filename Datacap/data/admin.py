from django.contrib import admin
from .models import Demographic, Baseline, Diagnostic, Treatment, Administration

admin.site.register(Demographic)
admin.site.register(Baseline)
admin.site.register(Diagnostic)
admin.site.register(Treatment)
admin.site.register(Administration)