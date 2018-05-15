from django import forms
# from monitoring.func import RainfallFunc
# from graph import Draw

class UploadFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    # def handle_uploaded_file(f):
    #     nlist = RainfallFunc.merge_dbf(file1, file2)
    #     daily_sum = RainfallFunc.rainfall_sum(nlist)
    #     Draw.plot_rainfall(daily_sum)
