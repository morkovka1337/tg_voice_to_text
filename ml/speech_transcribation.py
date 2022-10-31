import os
import time
import mutagen
import pandas as pd
import numpy as np
import torch
from ftlangdetect import detect
from huggingsound import SpeechRecognitionModel
import whisper

from pydub import AudioSegment
from pydub.silence import split_on_silence

class SpeechTranscribation:

  def __init__(self):
    self.model = whisper.load_model("base")

  def make_nice_chunks(self, chunks, limit=30000):
    new_chunks = []
    new_audio = None
    for chunk_idx in range(len(chunks)):
      if new_audio==None:
        new_audio = chunks[chunk_idx]
      elif len(new_audio+chunks[chunk_idx]) < limit:
        new_audio = new_audio+chunks[chunk_idx]
      else:
        new_chunks.append(new_audio)
        new_audio = chunks[chunk_idx]
    new_chunks.append(new_audio)
    return new_chunks

  def transform(self, audio_path: str):
    init_sound_path = audio_path # must have naming "audio.ogg"
    prep_sound_path = []

    if mutagen.File(init_sound_path).info.length>30: 
      sound_file = AudioSegment.from_ogg(init_sound_path)
      audio_chunks = split_on_silence(sound_file, min_silence_len=1000, silence_thresh=-40)

      fast_sounds = make_nice_chunks(audio_chunks, limit=30000)
      prep_sound_path = [init_sound_path.split('.')[0]+f'_new_{str(i)}.ogg' for i in range(len(fast_sounds))]
      for idx in range(len(prep_sound_path)):
        fast_sounds[idx].export(prep_sound_path[idx], format="ogg")
    else:
      prep_sound_path = [init_sound_path]

    full_text = ''
    for prep_sound in prep_sound_path:
      voice = whisper.load_audio(prep_sound)
      voice = whisper.pad_or_trim(voice)
      mel = whisper.log_mel_spectrogram(voice).to(self.model.device)
      options = whisper.DecodingOptions(fp16 = False, language='ru')
      full_text += whisper.decode(self.model, mel, options).text
    
    return full_text

