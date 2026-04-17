"""
# Structure
UI
Image collect
Gemini
Response
Error handle

"""

from dotenv import load_dotenv
from google import genai
from PIL import Image
from gtts import gTTS

import streamlit as st
import streamlit as st
import os
import io

# api
load_dotenv()
api_key = os.environ.get("GIMINI_API_KEY")
client = genai.Client(api_key=api_key)


# generating method
def note_generator(images, prompt):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents =[images, prompt],
    )
    return response.text


# gtts
def audio_transcript(text, lang='en'):
    audio_buffer = io.BytesIO()

    speech = gTTS(text, lang=lang, slow=False)
    speech.write_to_fp(audio_buffer)
    
    return audio_buffer

# quiz generate
def quiz_generate(images, difficulty):
    prompt = f"""
    Generate 10 quiz from given images, write in markdown formate.keep space between line and option for easy understanting, add new line after each question. mention answer at the end, keep dificulty {difficulty}
    """
    
    return note_generator(images,prompt)

#  work
st.title("Note summarizer and Quiz generator")
st.markdown("Upload upto 3 images")
st.divider()


with st.sidebar:
    st.header("Controls")
    
    
    images = st.file_uploader(
        "Upload images (upto 3)",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True 
    )

    pil_images =[]
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)
    
    if images:
        if len(images) > 3:
            st.error("You can upload upto 3 images")

        else:
            st.success("Uploaded images")
            cols =st.columns(len(images))
            
            for i,img in enumerate(images):
                with cols[i]:
                    st.image(img)
    
    if not images:
        st.error("Please upload an image")
    
    # difficulty

    selected_options = st.selectbox(
        "Select defficulty",
        ("Easy","Medium","High"),
        index=None,
    )

    if not selected_options:
        st.error("Select difficulty")

    # btn

    disable_btn = True

    if selected_options and images:
        disable_btn = False

    pressed = st.button(
        "Submit to AI", type='primary', disabled=disable_btn
        )
    

if pressed:
    if not images:
        st.error("You did not upload any image")
    if not selected_options:
        st.error("You did not select difficulty")
    
    
    # now
    if images and selected_options:
        # note
        with st.container(border=True):
            with st.spinner("AI summarizing"):
                st.subheader("Your notes")               
                generated_notes = note_generator(pil_images, f"describe notes in image in 150 words, keep difficulty {selected_options}")
                st.markdown(generated_notes)
        
        
            
        # audio transcript
        with st.container(border=True):
            with st.spinner("AI transcripting"):
            
                st.subheader("Transcript")
                
                # cleaning md
                generated_notes = generated_notes.replace("#","")
                generated_notes = generated_notes.replace("*","")
                generated_notes = generated_notes.replace("-","")
                generated_notes = generated_notes.replace("`","")
                
                st.audio(audio_transcript(generated_notes))
        
        
        # quiz
        with st.container(border=True):
            with st.spinner("Generating Quiz"):
        
                st.subheader("Quiz")
                st.markdown(quiz_generate(pil_images, selected_options))
        
        