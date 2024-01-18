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
        if form.is_valid():
            # Access the uploaded file using form.cleaned_data
            uploaded_file = form.cleaned_data['file']
            # Do something with the file, for example, save it to a specific directory
            with open('./musicdata/' + uploaded_file.name, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
        # Call the function with appropriate paths
        from .ml1 import transcribe_and_summarize
        transcribe_and_summarize("./musicdata/hello1.mp3", "./output_txt/out.txt", "./sumaudio/audio.mp3", "./output_txt/out_sum.txt")



        # self.uploaded_filename = uploaded_file.name
       #calling the ml function for summarization and audio conversion 
        
        
        return render(request, self.template_name, {'form': form})
    
    
    def read_file(request):
        file_path = 'mysite/home/out.txt'  # Replace with the actual path to your text file

        try:
            with open(file_path, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            content = "File not found."

        return render(request, 'home.html', {'content': content})
    

    
