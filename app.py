import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="MelodyMind AI",
    page_icon="🎵"
)

st.title("🎵 MelodyMind AI")
st.subheader("AI-Powered Music Composer")

st.write("Files detected by app:")
st.write([p.name for p in Path(".").iterdir()])

audio = Path("MelodyMind_Generated.wav")
midi = Path("MelodyMind_Generated.mid")

if audio.exists():
    st.audio(audio.read_bytes(), format="audio/wav")
    st.download_button(
        "Download WAV",
        audio.read_bytes(),
        file_name="MelodyMind_Generated.wav"
    )

if midi.exists():
    st.download_button(
        "Download MIDI",
        midi.read_bytes(),
        file_name="MelodyMind_Generated.mid"
    )

st.caption("Built with Python, TensorFlow and LSTM")
st.info("Model training is still being improved.")
