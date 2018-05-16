# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import FormView
from monitoring.forms import UploadFileForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import UploadFileForm

# Create your views here.


class UploadRainView(FormView):
    template_name = 'rain.html'
    form_class = UploadFileForm
    success_url = ""


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        print request.POST
        if form.is_valid():
            print "Form is valid"
            uploadfileform = UploadFileForm()
            uploadfileform.handle_uploaded_file(files[0], files[1])
            return self.form_valid(form)
        else:
            print "Form is not valid"
            return self.form_invalid(form)