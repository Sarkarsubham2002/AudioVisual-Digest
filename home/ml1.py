#!/usr/bin/env python3
import sys
import numpy as np
import librosa  
from functools import lru_cache
import time
import moviepy.editor
# from tkinter.filedialog import *
from gtts import gTTS
import whisper
from transformers import pipeline
import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import nltk
import re
# nltk.download('punkt')
from nltk import sent_tokenize
from nltk import word_tokenize









############################################################################
#for vedio to audio part (mp3)
# video = askopenfilename()
# video = r"/Users/subhamsarkar/Desktop/ALL/projects&AI/audioproj/whisper/vido.mp4"
# video = moviepy.editor.VideoFileClip(video)
# audio = video.audio
# audio.write_audiofile("sample2.mp3")

############################################################################




############################################################################
#Models and summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")#summarizer
model_name = 'tuner007/pegasus_paraphrase'#paraphraser
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'#checking if gpu is available
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)


###########################################################################





# 
# #
# # #
#############################################################################
#summarization part
#Fuctions
def chunks(text):
    words = word_tokenize(text)

    if len(words) < 2500:
        sentences = sent_tokenize(text)
    else:
        print("The number of words is greater than or equal to 2500.")
    chunks = []
    current_chunk = ""
    current_word_count = 0
    token_limit = 300
    for sentence in sentences:

        sentence = re.sub(r'\s{2,}', ' ', sentence).strip()#replacing many spaces with one space
        sentence_length = len(sentence.split())

        # If adding the sentence would exceed the token limit, save the current chunk and start a new one
        if current_word_count + sentence_length > token_limit:
            chunks.append(current_chunk)
            current_chunk = ""
            current_word_count = 0

        # Add the sentence to the current chunk
        current_chunk += sentence + " "
        current_word_count += sentence_length
        
    chunks.append(current_chunk)
    return chunks

def berty_generating_paragraph(chunks):
    
    all_sentences = []
    generated_sentences = []   

    for i, chunk in enumerate(chunks):
        text1 =summarizer(chunk, max_length=170, min_length=80, do_sample=False)
        outbert = text1[0]['summary_text']
        generated_sentences = outbert
        all_sentences.append(generated_sentences)

    generated_paragraph = ' '.join(all_sentences)
    return generated_paragraph

        ## Concatenate the generated sentences into a single string
        
#############################################################################
######
####
##
#




###########################################################################
def transcribe_and_summarize(input_audio_path, output_txt_path, output_sum_audio_path, output_sum_txt_path):
    # Transcribe audio to text
    model = whisper.load_model("base")
    result = model.transcribe(input_audio_path)

    # Write transcribed text to a text file
    with open(output_txt_path, "w", encoding="utf-8") as output_file:
        output_file.write(result["text"])

    # Summarize text
    text1 = result["text"]

    formatted_text = ' '.join(text1.split())
    chunks_text = chunks(formatted_text)
    summarized_text = berty_generating_paragraph(chunks_text)

    # Convert summarized text to speech
    tts = gTTS(summarized_text, lang='en')
    tts.save(output_sum_audio_path)

    # Write summarized text to a text file
    with open(output_sum_txt_path, "w") as file:
        file.write(summarized_text)

########################################################################################



# # Call the function with appropriate paths
# transcribe_and_summarize("../musicdata/hello1.mp3", "../output_txt/out.txt", "../sumaudio/audio.mp3", "../output_txt/out_sum.txt")