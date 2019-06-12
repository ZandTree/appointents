from django.shortcuts import render,get_object_or_404
from django.views.generic import View,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import DateForm
from datetime import datetime


class Dashboard(View):
    def get(self,request):
        return render(request,'staff/index.html')

class Tutors(ListView):
    template_name = 'staff/tutors.html'
    model = Tutor


class TutorDetail(LoginRequiredMixin,View):
    def get(self,request,**kwargs):
        template_name = 'staff/tutor_detail.html'
        pk = self.kwargs.get('pk')
        tutor = get_object_or_404(Tutor,id=pk)
        form = DateForm()
        return render(request,template_name,{"tutor":tutor,"form":form})

    def post(self,request,**kwargs):
        template_name = 'staff/tutor_detail.html'
        form = DateForm(self.request.POST)
        tutor_id = self.kwargs.get('pk')
        tutor = get_object_or_404(Tutor,id=tutor_id)
        if form.is_valid():
            stud_id = request.user.id
            date = self.request.POST.get('date')
            date_app = form.cleaned_data['date']
            app = Appointment(date=date_app,
                        student_id=stud_id,
                        docent_id=tutor_id
                        )
            app.save()
        else:
            msg = 'form is not valid'
            print('form error')    
        return render(request,template_name,{"tutor":tutor,"form":form})
