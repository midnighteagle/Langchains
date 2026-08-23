# import streamlit as st
# import os
# from dubbing_pipeline import (
#     extract_audio,
#     transcribe_audio,
#     translate_text,
#     text_to_speech,
#     merge_audio_video
# )

# st.set_page_config(page_title="AI Movie Dubbing Tool", layout="wide")
# st.title("🎬 AI Movie Dubbing Studio")
# st.write("Upload a video clip, select your target language, and generate an AI-dubbed version.")

# # Sidebar API Key configuration
# openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

# # Language mappings (gTTS codes)
# LANGUAGES = {
#     "Spanish": "es",
#     "French": "fr",
#     "German": "de",
#     "Hindi": "hi",
#     "Japanese": "ja",
#     "Italian": "it"
# }

# target_lang_name = st.selectbox("Select Target Language for Dubbing:", list(LANGUAGES.keys()))
# target_lang_code = LANGUAGES[target_lang_name]

# uploaded_file = st.file_uploader("Upload Video Clip (.mp4)", type=["mp4", "mov"])

# if uploaded_file and openai_api_key:
#     # Save input video locally
#     os.makedirs("temp", exist_ok=True)
#     video_path = os.path.join("temp", uploaded_file.name)
#     with open(video_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())

#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Original Video")
#         st.video(video_path)

#     if st.button("Start Dubbing Process"):
#         with st.spinner("Step 1/5: Extracting audio..."):
#             audio_path = extract_audio(video_path, "temp/extracted.mp3")

#         with st.spinner("Step 2/5: Transcribing original speech..."):
#             transcript = transcribe_audio(audio_path)
#             st.text_area("Original Transcript:", transcript, height=100)

#         with st.spinner(f"Step 3/5: Translating into {target_lang_name} via LangChain..."):
#             translated_text = translate_text(transcript, target_lang_name, openai_api_key)
#             st.text_area("Translated Dialogue:", translated_text, height=100)

#         with st.spinner("Step 4/5: Generating dubbed speech..."):
#             dubbed_audio_path = text_to_speech(translated_text, target_lang_code, "temp/dubbed.mp3")

#         with st.spinner("Step 5/5: Merging new audio into video..."):
#             output_video = merge_audio_video(video_path, dubbed_audio_path, "temp/final_dubbed.mp4")

#         st.success("Dubbing Complete!")

#         with col2:
#             st.subheader("Dubbed Video")
#             st.video(output_video)
            
#             with open(output_video, "rb") as file:
#                 st.download_button(
#                     label="Download Dubbed Video",
#                     data=file,
#                     file_name="dubbed_movie.mp4",
#                     mime="video/mp4"
#                 )
# elif not openai_api_key:
#     st.warning("Please enter your OpenAI API key in the sidebar to proceed.")

import os
import tempfile
import streamlit as st
from moviepy.editor import VideoFileClip, AudioFileClip
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from gtts import gTTS

# --- Page Configuration ---
st.set_page_config(page_title="AI Movie Dubber", page_icon="🎬", layout="wide")
st.title("🎬 AI Movie & Video Dubbing Tool")
st.caption("Extract audio, translate dialogue using LangChain, and generate dubbed video output.")

# --- Sidebar Inputs ---
with st.sidebar:
    st.header("Configuration")
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    target_language = st.selectbox(
        "Target Language",
        ["Spanish", "French", "German", "Hindi", "Japanese", "Italian"]
    )
    lang_code_map = {
        "Spanish": "es", "French": "fr", "German": "de",
        "Hindi": "hi", "Japanese": "ja", "Italian": "it"
    }

# --- Core Helper Functions ---

def extract_audio(video_path, audio_out_path):
    """Extracts MP3 audio from the video clip."""
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_out_path, logger=None)
    clip.close()

def transcribe_audio(audio_path, client):
    """Uses OpenAI Whisper to transcribe audio to text."""
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
    return transcript.text

def translate_script_with_langchain(text, target_lang, api_key):
    """Uses LangChain to translate and format the transcript for dubbing."""
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key, temperature=0.3)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert film translation and dubbing assistant. "
                "Translate the provided dialogue into {target_language}. "
                "Maintain natural flow, conversational tone, and similar line length for sync."),
        ("user", "Original Script:\n{script}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({"target_language": target_lang, "script": text})
    return response.content

def text_to_speech(text, lang_code, output_path):
    """Generates audio from text using gTTS."""
    tts = gTTS(text=text, lang=lang_code, slow=False)
    tts.save(output_path)

def merge_audio_video(video_path, new_audio_path, output_video_path):
    """Replaces the original video audio with the new dubbed audio track."""
    video = VideoFileClip(video_path)
    new_audio = AudioFileClip(new_audio_path)
    
    # Adjust new audio duration to fit video length if necessary
    final_video = video.set_audio(new_audio)
    final_video.write_videofile(
        output_video_path, 
        codec="libx264", 
        audio_codec="aac", 
        logger=None
    )
    video.close()
    new_audio.close()

# --- Main Application Logic ---
uploaded_file = st.file_uploader("Upload a Video (MP4 / MOV / AVI)", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    if not openai_api_key:
        st.warning("Please enter your OpenAI API Key in the sidebar to proceed.")
        st.stop()
        
    st.video(uploaded_file)
    
    if st.button("🚀 Start Dubbing Process", type="primary"):
        with tempfile.TemporaryDirectory() as temp_dir:
            from openai import OpenAI
            client = OpenAI(api_key=openai_api_key)
            
            # Step 1: Save uploaded video to temp file
            input_video_path = os.path.join(temp_dir, "input_video.mp4")
            with open(input_video_path, "wb") as f:
                f.write(uploaded_file.read())
            
            # Step 2: Extract Audio
            with st.status("Step 1/5: Extracting audio...", expanded=True) as status:
                audio_path = os.path.join(temp_dir, "extracted_audio.mp3")
                extract_audio(input_video_path, audio_path)
                status.update(label="Audio extracted!", state="complete")
            
            # Step 3: Transcribe
            with st.status("Step 2/5: Transcribing original audio...", expanded=True) as status:
                original_text = transcribe_audio(audio_path, client)
                st.write("**Original Text:**", original_text)
                status.update(label="Transcription complete!", state="complete")
            
            # Step 4: Translate with LangChain
            with st.status("Step 3/5: Translating dialogue using LangChain...", expanded=True) as status:
                translated_text = translate_script_with_langchain(
                    original_text, target_language, openai_api_key
                )
                st.write(f"**Translated ({target_language}):**", translated_text)
                status.update(label="Translation complete!", state="complete")
            
            # Step 5: Synthesize Dubbed Audio
            with st.status("Step 4/5: Generating dubbed speech...", expanded=True) as status:
                dubbed_audio_path = os.path.join(temp_dir, "dubbed_audio.mp3")
                lang_code = lang_code_map[target_language]
                text_to_speech(translated_text, lang_code, dubbed_audio_path)
                status.update(label="Speech generated!", state="complete")
            
            # Step 6: Merge & Render
            with st.status("Step 5/5: Merging new audio into video...", expanded=True) as status:
                final_output_path = os.path.join(temp_dir, "dubbed_output.mp4")
                merge_audio_video(input_video_path, dubbed_audio_path, final_output_path)
                status.update(label="Dubbed video ready!", state="complete")
            
            # Render Final Output
            st.subheader("🎉 Dubbed Video Output")
            st.video(final_output_path)
            
            with open(final_output_path, "rb") as file:
                st.download_button(
                    label="📥 Download Dubbed Video",
                    data=file,
                    file_name=f"dubbed_{target_language.lower()}.mp4",
                    mime="video/mp4"
                )