# Generated by Django 4.0.5 on 2022-06-17 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0002_rename_eligibility_id_baseline_subject_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baseline',
            old_name='cancderdx_date',
            new_name='disease_dxdate',
        ),
        migrations.RenameField(
            model_name='baseline',
            old_name='cancer_dx',
            new_name='disease_name',
        ),
        migrations.RenameField(
            model_name='baseline',
            old_name='subject',
            new_name='subject_baseline',
        ),
        migrations.RenameField(
            model_name='demographic',
            old_name='subject_name',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='diagnostic',
            old_name='subject',
            new_name='subject_diagnostics',
        ),
        migrations.RemoveField(
            model_name='baseline',
            name='study_name',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='tx_date',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='tx_time',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='user',
        ),
        migrations.AddField(
            model_name='baseline',
            name='past_mh',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='baseline',
            name='study_tx',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='data.treatment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='diag_coll_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='diag_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='dx_tx',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='data.treatment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treatment',
            name='tx_admin_type',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treatment',
            name='tx_type',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timepoint', models.CharField(max_length=255)),
                ('admin_date', models.DateField(blank=True, null=True)),
                ('admin_starttime', models.TimeField(blank=True, null=True)),
                ('admin_endtime', models.TimeField(blank=True, null=True)),
                ('admin_description', models.TextField(blank=True)),
                ('admin_tx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.treatment')),
                ('subject_administration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.demographic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'timepoints',
            },
        ),
    ]
