from django.http import HttpResponse
from django.views.generic import TemplateView
# in yourapp/views.py
from .forms import MediaFileForm

from django.views import View
from django.shortcuts import render, redirect









class HomeView(View):
    template_name = 'home.html'

    uploaded_filename = None


    def get(self, request, *args, **kwargs):
        form = MediaFileForm()
        return render(request, self.template_name, {'form': form})




    def post(self, request, *args, **kwargs):
        form = MediaFileForm(request.POST, request.FILES)
        output_content = None
        audio_file_path = None 
        file_path = None

        if form.is_valid():
            # Access the uploaded file using form.cleaned_data
            uploaded_file = form.cleaned_data['file']
            file_path = './musicdata/' + uploaded_file.name
            # Do something with the file, for example, save it to a specific directory
            with open(file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
        # Call the function with appropriate paths
        from .ml1 import transcribe_and_summarize
        transcribe_and_summarize(file_path, "./output_txt/out.txt", "./sumaudio/audio.mp3", "./output_txt/out_sum.txt")

        try:
            with open('./output_txt/out_sum.txt', 'r') as file:
                output_content = file.read()
        except FileNotFoundError:
            output_content = "Output file not found."
                    
        audio_file_path = "../../sumaudio/audio.mp3"
        # self.uploaded_filename = uploaded_file.name
       #calling the ml function for summarization and audio conversion 
        
        
        return render(request, self.template_name, {'form': form, 'output_content': output_content, 'audio_file_path': audio_file_path})
    

    
    
    def read_file(request):
        file_path = 'mysite/home/out.txt'  # Replace with the actual path to your text file

        try:
            with open(file_path, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            content = "File not found."

        return render(request, 'home.html', {'content': content})
    








