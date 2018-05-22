# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView, FormView
from monitoring.forms import UploadFileForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import UploadFileForm, UploadFormSet, NumberFilesForm
from .models import DBFFile
from pig_apps.settings import MEDIA_ROOT
import os
from django.forms import formset_factory
# Create your views here.

class DecideNumberFileView(FormView):
    form_class = NumberFilesForm
    success_url = "upload/"
    template_name = 'main.html'



class UploadRainView(CreateView):
    template_name = 'rain.html'
    form_class = UploadFileForm
    success_url = "/"

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        new_extra = int(self.request.GET['number_dbfs'])
        upload_formset = formset_factory(UploadFileForm,extra=new_extra)
        return self.render_to_response(
            self.get_context_data(form=form, upload_formset=upload_formset)
        )

    def get_context_data(self, **kwargs):
        data = super(UploadRainView, self).get_context_data(**kwargs)
        print data
        upload_formset = data['upload_formset']
        if self.request.POST:
            data['file'] = upload_formset(self.request.POST)
        else:
            data['file'] = upload_formset
        return data


    def form_valid(self, form):
        files = DBFFile(title1=self.request.FILES['file1'].name, file1=self.request.FILES['file1'],
                        title2=self.request.FILES['file2'].name, file2=self.request.FILES['file2'])
        files.save()
        print self.request.FILES
        filename1 = DBFFile.objects.last().title1
        filename2 = DBFFile.objects.last().title2

        path1 = MEDIA_ROOT + "/" + filename1
        path2 = MEDIA_ROOT + "/" + filename2

        DBFFile.handle_uploaded_file(self, path1, path2)

        os.remove(path1)
        os.remove(path2)
        for dbf_file in DBFFile.objects.all():
            dbf_file.delete()

        return HttpResponseRedirect(self.get_success_url())

# def upload_rain_dbf(request):
#     UploadFileFormSet = formset_factory(UploadFileForm)
#     if request.method == 'POST':
#         formset = UploadFileFormSet(request.POST, request.FILES)
#         if formset.is_valid():
#             # do something with the formset.cleaned_data
#             pass
#     else:
#         formset = UploadFileFormSet()
#     return render(request, '/', {'formset': formset})