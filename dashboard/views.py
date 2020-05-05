from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import SafariAccount


class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        data = list(SafariAccount.objects.values()) 
        return JsonResponse(data, safe=False)