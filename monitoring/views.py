# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import FormView
from monitoring.forms import UploadFileForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import UploadFileForm
from .models import DBFFile
from pig_apps.settings import MEDIA_ROOT
import os
# Create your views here.


class UploadRainView(FormView):
    template_name = 'rain.html'
    form_class = UploadFileForm
    success_url = "/"

    def form_valid(self, form):
        print "form is valid"
        files = DBFFile(title1=self.request.FILES['file1'].name, file1=self.request.FILES['file1'],
                        title2=self.request.FILES['file2'].name, file2=self.request.FILES['file2'])
        files.save()

        filename1 = DBFFile.objects.last().title1
        filename2 = DBFFile.objects.last().title2

        path1 = MEDIA_ROOT + "/" + filename1
        path2 = MEDIA_ROOT + "/" + filename2

        DBFFile.handle_uploaded_file(self, path1, path2)

        all_dbfs = DBFFile.objects.all()
        for dbf_file in all_dbfs:
            dbf_file.delete()
            os.remove(path1)
            os.remove(path2)
        return HttpResponseRedirect(self.get_success_url())