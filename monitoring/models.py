# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from monitoring.func import RainfallFunc
from graph import Draw
import os

# Create your models here.

class DBFFile(models.Model):
    title = models.CharField(max_length=100, null=True)
    file = models.FileField()

    @staticmethod
    def handle_uploaded_file(self, file1, file2):
        nlist = RainfallFunc.merge_dbf(file1, file2)
        daily_sum = RainfallFunc.rainfall_sum(nlist)
        Draw.plot_rainfall(daily_sum)

    @classmethod
    def delete_file(path):
        if os.path.isfile(path):
            os.remove(path)
        else:
            print "No file found in this path"
