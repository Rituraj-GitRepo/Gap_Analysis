from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionalHeadResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=200)),
                ('employee_code', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('GET', 'GET — Graduate Engineer Trainee'), ('MT', 'MT — Management Trainee'), ('FH', 'Functional Head')], default='FH', max_length=10)),
                ('function', models.CharField(choices=[('sales_marketing', 'Sales & Marketing'), ('engineering', 'Engineering'), ('new_product_dev', 'New Product Development'), ('finance', 'Finance'), ('hr', 'HR'), ('procurement', 'Procurement & Localisation'), ('scm_logistics', 'SCM & Logistics'), ('it_digital', 'IT & Digital'), ('manufacturing', 'Manufacturing')], max_length=50)),
                ('date', models.DateField()),
                ('competency_ratings', models.JSONField(default=dict)),
                ('q1_critical_competency', models.TextField(blank=True)),
                ('q2_gap_risk', models.TextField(blank=True)),
                ('q3_alp_theme', models.TextField(blank=True)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-submitted_at'],
            },
        ),
        migrations.CreateModel(
            name='SelfAssessmentResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=200)),
                ('employee_code', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('GET', 'GET — Graduate Engineer Trainee'), ('MT', 'MT — Management Trainee'), ('FH', 'Functional Head')], max_length=10)),
                ('function', models.CharField(choices=[('sales_marketing', 'Sales & Marketing'), ('engineering', 'Engineering'), ('new_product_dev', 'New Product Development'), ('finance', 'Finance'), ('hr', 'HR'), ('procurement', 'Procurement & Localisation'), ('scm_logistics', 'SCM & Logistics'), ('it_digital', 'IT & Digital'), ('manufacturing', 'Manufacturing')], max_length=50)),
                ('date', models.DateField()),
                ('competency_ratings', models.JSONField(default=dict)),
                ('q1_strengths', models.TextField(blank=True)),
                ('q2_development_areas', models.TextField(blank=True)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-submitted_at'],
            },
        ),
    ]
