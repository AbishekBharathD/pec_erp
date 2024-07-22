from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('login.html',views.login_page,name='login'),
    path('login',views.login_view,name='login_valid'),
    path('profile',views.profile_view,name='profile'),
    path('student-login/', views.stu_aca_login,name="stu_aca_login"),
    path('student-time-table/', views.stu_aca_time,name="stu_aca_time"),
    path('students-academic-result/', views.stu_aca_res,name="stu_aca_res"),
    path('students-documents/', views.stu_aca_doc,name="stu_aca_doc"),
    path('students-certificate/', views.stu_aca_cer,name="stu_aca_cer"),
    path('students-lesson-plan/', views.stu_aca_les,name="stu_aca_les"),
    path('students-feed-back/', views.stu_aca_fee,name="stu_aca_fee"),
    path('students-academic-result2/',views.stu_aca_res2,name="stu_aca_res2"),
    path('students-certifications-2/',views.stu_aca_res2,name="stu_aca_cer2"),
    path('hod-profile-page.htm',views.hod_profile_page,name='hod_profile'),
    path('hod-time-table.html',views.hod_time_table,name="hod_time_table"),
    path('hod-scopus-link-2.html',views.hod_scopus_link2,name='hod_scopus_link2'),
    path('hod-scopus-link-1.html',views.hod_scopus_link1,name='hod_scopus_link1'),
    path('hod-result-search-1.html',views.hod_result_search1,name='hod_result_search1'),
    path('hod-result-search-2.html',views.hod_result_search2,name='hod_result_search2'),
    path('hod-lesson-plan-1.html',views.hod_lesson_plan1,name='hod_lesson_plan1'),
    path('hod-lesson-plan-2.html',views.hod_lesson_plan2,name='hod_lesson_plan2'),
    path('hod-feedback.html',views.hod_feedback,name='hod_feedback'),
    path('hod-academic-result-1.html',views.hod_academic_result1,name='hod_academic_result1'),
    path('hod-academic-result-2.html',views.hod_academic_result2,name='hod_academic_result2'),
    path('hod-academic-result-3.html',views.hod_academic_result3,name='hod_academic_result3'),

]