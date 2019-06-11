from django.shortcuts import render,get_object_or_404
from django.views.generic import View,ListView,DetailView
from .models import *
from .forms import DateForm


class Dashboard(View):
    def get(self,request):
        return render(request,'staff/index.html')

class Tutors(ListView):
    template_name = 'staff/tutors.html'
    model = Tutor


class TutorDetail(View):
    def get(self,request,**kwargs):
        template_name = 'staff/tutor_detail.html'
        pk = self.kwargs.get('pk')
        tutor = get_object_or_404(Tutor,id=pk)
        form = DateForm()
        return render(request,template_name,{"tutor":tutor,"form":form})
