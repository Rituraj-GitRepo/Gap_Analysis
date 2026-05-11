from django.urls import path
from . import views

urlpatterns = [
    path('',                                          views.welcome,                name='welcome'),
    path('survey/functional-head/<str:function_key>/',views.functional_head_survey, name='fh_survey'),
    path('survey/self-assessment/<str:function_key>/',views.self_assessment,         name='sa_survey'),
    path('survey/success/',                           views.success,                name='success'),

    path('admin-login/',                              views.admin_login,            name='admin_login'),
    path('admin-logout/',                             views.admin_logout,           name='admin_logout'),
    path('admin-dashboard/',                          views.admin_dashboard,        name='admin_dashboard'),
    path('admin-responses/<str:survey_type>/',        views.admin_responses,        name='admin_responses'),
    path('admin-delete/<str:survey_type>/<int:pk>/',  views.delete_response,        name='delete_response'),
    path('admin-gap-analysis/',                       views.gap_analysis,           name='gap_analysis'),
    path('admin-export/<str:survey_type>/',           views.export_excel,           name='export_excel'),
]
