from django.http import HttpResponse
from django.views.generic import TemplateView
# in yourapp/views.py
from .forms import MediaFileForm

from django.views import View
from django.shortcuts import render, redirect








class HomeView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = MediaFileForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Access the uploaded file using form.cleaned_data
            uploaded_file = form.cleaned_data['file']
            # Do something with the file, for example, save it to a specific directory
            with open('/Users/subhamsarkar/Desktop/ALL/projects&AI/audioproj/mysite/musicdata/' + uploaded_file.name, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)


        return render(request, self.template_name, {'form': form})
    
    
    def read_file(request):
        file_path = 'mysite/home/out.txt'  # Replace with the actual path to your text file

        try:
            with open(file_path, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            content = "File not found."

        return render(request, 'home.html', {'content': content})
    
