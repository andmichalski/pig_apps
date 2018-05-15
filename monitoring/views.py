# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import FormView
from monitoring.forms import UploadFileForm
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


class UploadRainView(FormView):
    template_name = 'rain.html'
    form_class = UploadFileForm


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                pass  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)