import streamlit as st
from pathlib import Path

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="MelodyMind AI | Music Studio",
    page_icon="🎧",
    layout="wide"
)

# ---------------- FILE DETECTION ----------------
ROOT = Path(__file__).parent

def find_file(extension):
    matches = list(ROOT.rglob(f"*{extension}"))
    return matches[0] if matches else None

audio_file = find_file(".wav")
midi_file = find_file(".mid")
model_file = find_file(".keras")

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, #252052 0%, transparent 40%),
        radial-gradient(ellipse at 90% 30%, #172b50 0%, transparent 35%),
        #090b14;
    color: #f4f3ff;
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: #ffffff !important;
}

.hero {
    padding: 42px 35px;
    border: 1px solid #39345f;
    border-radius: 25px;
    background: linear-gradient(120deg, #201b42, #151d38 65%, #24204b);
    margin-bottom: 25px;
}

.eyebrow {
    color: #b7a5ff;
    letter-spacing: 3px;
    font-size: 12px;
    font-weight: 700;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(35px, 6vw, 60px);
    font-weight: 800;
    line-height: 1.1;
    margin: 15px 0;
}

.gradient-text {
    background: linear-gradient(90deg, #bd9cff, #66d8ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-desc {
    color: #c4c4d9;
    font-size: 16px;
    max-width: 600px;
    line-height: 1.7;
}

.panel {
    background: linear-gradient(145deg, #191b2c, #111522);
    border: 1px solid #30334b;
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 20px;
}

.panel-title {
    font-size: 21px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 8px;
}

.muted {
    color: #a5a9c2;
    font-size: 14px;
    line-height: 1.6;
}

.status {
    display: inline-block;
    border: 1px solid #48406f;
    background: #25203f;
    color: #c9baff;
    padding: 7px 13px;
    border-radius: 30px;
    font-size: 12px;
    margin: 5px 5px 5px 0;
}

.wave {
    height: 75px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 5px;
    margin: 15px 0;
}

.wave span {
    width: 5px;
    border-radius: 10px;
    background: linear-gradient(180deg, #b58aff, #50cfff);
    animation: pulse 1s ease-in-out infinite alternate;
}

.wave span:nth-child(3n) { animation-delay: .3s; }
.wave span:nth-child(2n) { animation-delay: .6s; }

@keyframes pulse {
    from { transform: scaleY(.35); opacity: .6; }
    to { transform: scaleY(1); opacity: 1; }
}

.stButton > button, .stDownloadButton > button {
    background: linear-gradient(100deg, #8060e9, #398ddc);
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 700;
    min-height: 45px;
    width: 100%;
}

.stButton > button:hover, .stDownloadButton > button:hover {
    border: 1px solid #c4b5fd;
    color: white;
    background: linear-gradient(100deg, #9678f3, #55a7ee);
}

div[data-testid="stAudio"] {
    background: #202238;
    border-radius: 14px;
    padding: 10px;
}

hr {
    border-color: #30334b;
}

footer {visibility: hidden;}

@media(max-width: 700px) {
    .hero { padding: 27px 20px; }
    .panel { padding: 18px; }
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <div class="eyebrow">✦ YOUR CREATIVE AI MUSIC STUDIO</div>
    <div class="hero-title">
        MelodyMind <span class="gradient-text">AI</span>
    </div>
    <div class="hero-desc">
        Discover a new world of music with artificial intelligence.
        Explore musical patterns, experience AI-assisted composition
        and listen to your generated melodies.
    </div>
    <br>
    <span class="status">♫ AI MUSIC PROJECT</span>
    <span class="status">✧ LSTM ARCHITECTURE</span>
    <span class="status">◈ PYTHON POWERED</span>
</div>
""", unsafe_allow_html=True)

# ---------------- PROJECT OVERVIEW ----------------
st.markdown("## Your Music Space")
st.markdown(
    '<p class="muted">A creative space for exploring AI-powered music.</p>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="panel">
        <div class="panel-title">🎼 Composition</div>
        <div class="muted">Explore musical note patterns and AI-assisted composition.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="panel">
        <div class="panel-title">🧠 LSTM Model</div>
        <div class="muted">A recurrent neural network architecture for learning musical sequences.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="panel">
        <div class="panel-title">🎧 Audio Studio</div>
        <div class="muted">Listen to your available music and download project files.</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- MUSIC PLAYER ----------------
st.markdown("---")
st.markdown("## 🎧 Now Playing")

st.markdown("""
<div class="panel">
    <div class="eyebrow">MELODY COLLECTION / TRACK 001</div>
    <div class="panel-title">AI Music Experience</div>
    <div class="muted">Your MelodyMind audio preview</div>
    <div class="wave">
""", unsafe_allow_html=True)

bars = [20, 38, 55, 30, 65, 45, 25, 60, 42, 70, 32, 52, 25, 65, 40, 58, 30, 48, 68, 35, 55, 25, 45, 62, 32, 50, 70, 40, 25, 58]

st.markdown(
    "".join(f'<span style="height:{h}px"></span>' for h in bars)
    + "</div></div>",
    unsafe_allow_html=True
)

if audio_file:
    st.success("Music file detected — ready to play.")
    st.audio(str(audio_file), format="audio/wav")

    st.download_button(
        "⬇ Download WAV Audio",
        data=audio_file.read_bytes(),
        file_name="MelodyMind_Generated.wav",
        mime="audio/wav",
        use_container_width=True
    )
else:
    st.warning("No WAV audio file found in the repository.")

# ---------------- DOWNLOAD CENTER ----------------
st.markdown("---")
st.markdown("## 📥 Download Center")

d1, d2 = st.columns(2)

with d1:
    st.markdown("""
    <div class="panel">
        <div class="panel-title">🎵 MIDI File</div>
        <div class="muted">Musical note sequence file for compatible music software.</div>
    </div>
    """, unsafe_allow_html=True)

    if midi_file:
        st.download_button(
            "Download MIDI",
            data=midi_file.read_bytes(),
            file_name="MelodyMind_Generated.mid",
            mime="audio/midi",
            use_container_width=True
        )
    else:
        st.info("MIDI file not available.")

with d2:
    st.markdown("""
    <div class="panel">
        <div class="panel-title">🧠 Model Asset</div>
        <div class="muted">Saved LSTM model file included in the project.</div>
    </div>
    """, unsafe_allow_html=True)

    if model_file:
        st.success("LSTM model file detected.")
    else:
        st.warning("Model file not detected.")

# ---------------- MODEL STATUS ----------------
st.markdown("---")
st.markdown("## 🧠 AI Lab")

if model_file:
    st.markdown("""
    <div class="panel">
        <div class="panel-title">LSTM Architecture Available</div>
        <div class="muted">
            The LSTM model was trained for 3 epochs using
note sequences from the MAESTRO MIDI dataset.
It generates new musical note sequences.
        </div>
        <span class="status">MODEL FILE AVAILABLE</span>
        <span class="status">LSTM MODEL TRAINED-3 EPOCHS</span>
    </div>
    """, unsafe_allow_html=True)
else:
    st.info("The saved LSTM model file is not currently available.")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("""
<div style="text-align:center; padding:20px 5px;">
    <div style="font-size:22px; font-weight:800; color:#c5aaff;">
        MelodyMind AI
    </div>
    <p class="muted">
        Designed for creativity. Powered by Python and LSTM.
    </p>
    <p style="font-size:12px;color:#777d99;">
        AI Music Composer Project
    </p>
</div>
""", unsafe_allow_html=True)

