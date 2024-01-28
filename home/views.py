from django.http import HttpResponse
from django.views.generic import TemplateView
# in yourapp/views.py
from .forms import MediaFileForm
from .models import MediaFile, details
from django.views import View
from django.shortcuts import render, redirect
import moviepy.editor
import os








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
        title = None

        if form.is_valid():
            # Access the uploaded file using form.cleaned_data
            uploaded_file = form.cleaned_data['file']
            title = form.cleaned_data['title']
            file_path = './musicdata/' + uploaded_file.name
            # Do something with the file, for example, save it to a specific directory
            with open(file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
        # Call the function with appropriate paths
            _, file_extension = os.path.splitext(file_path.lower())
            # valid_audio_formats = ['.mp3', '.wav']
            valid_video_formats = ['.mp4']

            # if file_extension in valid_audio_formats:
            #     updated_file_path = file_path

            if file_extension in valid_video_formats:
                video = moviepy.editor.VideoFileClip(file_path)
                audio = video.audio
                audio.write_audiofile(file_path)
        from .ml1 import transcribe_and_summarize
        transcribe_and_summarize(file_path, "./output_txt/out.txt", "./sumaudio/audio.mp3", "./output_txt/out_sum.txt")

        try:
            with open('./output_txt/out_sum.txt', 'r') as file:
                output_content = file.read()
            details.objects.update_or_create(person_name=request.user, defaults={'summary': output_content,'title': title})
        except FileNotFoundError:
            output_content = "Output file not found."
                    
        audio_file_path = "../../sumaudio/audio.mp3"
        # self.uploaded_filename = uploaded_file.name
        #calling the ml function for summarization and audio conversion 
        
        
        return render(request, self.template_name, {'form': form, 'output_content': output_content, 'audio_file_path': audio_file_path})
    


class HomeData(View):
    template_name = 'data_list.html'  # Replace with the actual path to your template

    def get(self, request, *args, **kwargs):
        data = details.objects.all()  # Replace 'Details' with the actual name of your model
        return render(request, self.template_name, {'data': data})
    







