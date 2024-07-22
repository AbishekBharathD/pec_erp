from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import CustomUser


# Create your views here.
def home(request):
    return render(request,'home.html')

def login_page(request):
    return render(request,'login.html')


def login_view(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username,password)
            user = CustomUser.objects.filter(username=username, password=password).last()
            print(user)
            if not user:
                messages.error(request,'Invalid Login Credentials')
                return render(request,'login.html')

            login(request,user)   
            return redirect('profile')
        

    
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')

@login_required
def profile_view(request):
    user = request.user
    context = {'user': user}
    if user.user_type == 'student':
        context['details'] = user.student
        return render(request,'student-login.html',context)
    elif user.user_type == 'faculty':
        context['details'] = user.faculty
        return render(request,'faculty-profile.html',context)
    elif user.user_type == 'hod':
        context['details'] = user.hod
        return render(request,'hod-profile-page.html',context)
    else:
        return render(request,'login.html')

def hod_time_table(request):
    return render(request,'hod-time-table.html')

def hod_scopus_link2(request):
    return render(request,'hod-scopus-link-2.html')

def hod_scopus_link1(request):
    return render(request,'hod-scopus-link-1.html')

def hod_result_search1(request):
    return render(request,'hod-result-search-1.html')

def hod_result_search2(request):
    return render(request,'hod-result-search-2.html')

def hod_lesson_plan1(request):
    return render(request,'hod-lesson-plan-1.html')

def hod_lesson_plan2(request):
    return render(request,'hod-lesson-plan-2.html')

def hod_feedback(request):
    return render(request,'hod-feedback.html')

def hod_academic_result1(request):
    return render(request,'hod-academic-result-1.html')

def hod_academic_result2(request):
    return render(request,'hod-academic-result-2.html')

def hod_academic_result3(request):
    return render(request,'hod-academic-result-3.html')

def hod_profile_page(request):
    return render(request,'hod-profile-page.html')

def stu_aca_login(request):
    return render(request,'student-login.html')

def stu_aca_time(request):
    return render(request,'student-time-table.html')

def stu_aca_res(request):
    return render(request,'students-academic-result.html')

def stu_aca_doc(request):
    return render(request,'students-documents.html')

def stu_aca_cer(request):
    return render(request,'students-certificate.html')

def stu_aca_les(request):
    return render(request,'students-lesson-plan.html')

def stu_aca_fee(request):
    return render(request,'students-feed-back.html')

def stu_aca_res2(request):
    return render(request,'students-academic-result2.html')

def stu_aca_cer2(request):
    return render(request,'students-certifications-2.html')
