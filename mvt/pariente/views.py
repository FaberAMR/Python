from multiprocessing import context
from typing import Any, Dict
from django import template
from django.views.generic import TemplateView
from django.shortcuts import render


class ParienteView(TemplateView):
    template_name ='pariente/index.html'
    def get(self, request, status=None):
        print(request.GET.get('edad'))
        context={
            'edad':request.GET.get('edad'),
            'list_test':[1,2,3,4]
        }
        return render(request, self.template_name, context)