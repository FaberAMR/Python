from multiprocessing import context
from re import template
from pyparsing import Dict
from typing,  Any, Dict
from django.views.generic import TemplateView
from django.shortcuts import render


class ParienteView(TemplateView):
    template_name ='/parients/index.html'
    def get(self, request, status=None):
        context={}
        return render(request, self.template_name, context)