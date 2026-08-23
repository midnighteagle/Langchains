import os
import whisper
from moviepy.editor import VideoFileClip, AudioFileClip
from gtts import gTTS
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Extract Audio from Video
def extract_audio(video_path, output_audio_path="temp_audio.mp3"):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(output_audio_path, logger=None)
    clip.close()
    return output_audio_path

# 2. Transcribe Audio using OpenAI Whisper
def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

# 3. Translate Text using LangChain
def translate_text(text, target_language, openai_api_key):
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key, temperature=0.3)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert movie subtitle and dialogue translator. "
                "Translate the following transcript into {target_language}. "
                "Maintain tone, natural speech flow, and emotion suited for dubbing."),
        ("user", "{text}")
    ])
    
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"target_language": target_language, "text": text})

# 4. Generate TTS Audio
def text_to_speech(translated_text, target_language_code, output_tts_path="dubbed_audio.mp3"):
    # Note: For production voice-cloning, swap gTTS with ElevenLabs or Coqui TTS
    tts = gTTS(text=translated_text, lang=target_language_code, slow=False)
    tts.save(output_tts_path)
    return output_tts_path

# 5. Merge New Audio with Original Video
def merge_audio_video(video_path, new_audio_path, output_video_path="final_dubbed_video.mp4"):
    video = VideoFileClip(video_path)
    dubbed_audio = AudioFileClip(new_audio_path)
    
    # Adjust audio duration if needed or set directly
    final_video = video.set_audio(dubbed_audio)
    final_video.write_videofile(output_video_path, codec="libx264", audio_codec="aac", logger=None)
    
    video.close()
    dubbed_audio.close()
    return output_video_pat