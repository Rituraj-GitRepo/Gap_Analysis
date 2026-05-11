from django.db import models

ROLE_CHOICES = [
    ('GET', 'GET — Graduate Engineer Trainee'),
    ('MT', 'MT — Management Trainee'),
    ('FH', 'Functional Head'),
]

FUNCTION_CHOICES = [
    ('sales_marketing', 'Sales & Marketing'),
    ('engineering', 'Engineering'),
    ('new_product_dev', 'New Product Development'),
    ('finance', 'Finance'),
    ('hr', 'HR'),
    ('procurement', 'Procurement & Localisation'),
    ('scm_logistics', 'SCM & Logistics'),
    ('it_digital', 'IT & Digital'),
    ('manufacturing', 'Manufacturing'),
]


class FunctionalHeadResponse(models.Model):
    employee_name = models.CharField(max_length=200)
    employee_code = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='FH')
    function = models.CharField(max_length=50, choices=FUNCTION_CHOICES)
    date = models.DateField()
    competency_ratings = models.JSONField(default=dict)
    q1_critical_competency = models.TextField(blank=True)
    q2_gap_risk = models.TextField(blank=True)
    q3_alp_theme = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-submitted_at']

    def top10_count(self):
        return sum(1 for v in self.competency_ratings.values() if v.get('top10'))

    def avg_importance(self):
        vals = [v.get('importance', 0) for v in self.competency_ratings.values() if v.get('importance')]
        return round(sum(vals) / len(vals), 2) if vals else 0

    def __str__(self):
        return f"{self.employee_name} ({self.get_function_display()}) — FH Survey"


class SelfAssessmentResponse(models.Model):
    employee_name = models.CharField(max_length=200)
    employee_code = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    function = models.CharField(max_length=50, choices=FUNCTION_CHOICES)
    date = models.DateField()
    competency_ratings = models.JSONField(default=dict)
    q1_strengths = models.TextField(blank=True)
    q2_development_areas = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-submitted_at']

    def avg_proficiency(self):
        vals = [v.get('current_level', 0) for v in self.competency_ratings.values() if v.get('current_level')]
        return round(sum(vals) / len(vals), 2) if vals else 0

    def __str__(self):
        return f"{self.employee_name} ({self.role} — {self.get_function_display()}) — SA"
