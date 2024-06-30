import streamlit as st
from pydub import AudioSegment
from pydub.playback import play

def play_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    play(audio)

def main():
    st.title("Play Audio without UI")

    # Path to your audio file
    audio_file_path = "D:\My Python Stuff\Happy_birthday\Happy_birthday_A_cappella_K4Ei6x1ofCk_140.mp3"

    if st.button("Play Audio"):
        play_audio(audio_file_path)