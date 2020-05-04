from django.shortcuts import render
from django.views import View



class Home(View):
    template_name = 'base.html'

    def get(self, request):
        return render(request, self.template_name)