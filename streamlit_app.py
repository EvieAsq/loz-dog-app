import streamlit as st
import random
import streamlit.components.v1 as components

# Page setup
st.set_page_config(page_title="Loz Dog Love App", layout="centered")

# Custom pink CSS styling
st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
    .stApp {
        background-color: #ffe6f0;
        font-family: 'Arial Rounded MT Bold', sans-serif;
        color: #d63384;
    }
    h1, h2, h3, .markdown-text-container {
        color: #d63384;
    }
    .css-18e3th9 {
        background-color: #ffe6f0;
    }
    </style>
""", unsafe_allow_html=True)

# Animated hearts (JS)
components.html("""
    <style>
        .hearts {
            position: fixed;
            top: -10px;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 9999;
        }
        .heart {
            position: absolute;
            top: 0;
            font-size: 24px;
            animation: fall 5s linear infinite;
        }
        @keyframes fall {
            0% {transform: translateY(0);}
            100% {transform: translateY(100vh);}
        }
    </style>
    <div class="hearts">
        <div class="heart" style="left:10%;">💖</div>
        <div class="heart" style="left:30%;">💕</div>
        <div class="heart" style="left:50%;">💘</div>
        <div class="heart" style="left:70%;">💞</div>
        <div class="heart" style="left:90%;">❤️</div>
    </div>
""", height=0)

st.title("the loz app - beta version")
st.subheader("because she is amazing")

# 💌 Love Letter
st.markdown("## to my love")

love_letter = """

you make my world warmer, brighter, and infinitely more fun.  
i love you more than all the atoms and molecules combined

"""

st.markdown(f"> {love_letter}")

# 🌡️ Love Slider
st.markdown("## 🌡️ How Loved Do You Feel Today?")
feeling = st.slider("Slide to choose how loved you feel:", 0, 100, 50)

if st.button("Submit 💖"):
    st.success("No matter the number, you are loved **100%**. Always.")

# 🎵 Spotify Embed
st.markdown("## loverrrrrr")
st.markdown("""
<iframe style="border-radius:12px" 
src="https://open.spotify.com/embed/track/2PLi7OmleXPNBrGLon3sUy?utm_source=generator" 
width="100%" height="152" frameBorder="0" allowfullscreen="" 
allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
""", unsafe_allow_html=True)

# 🌈 Affirmations
st.markdown("## affirmations")

affirmations = [
    "You're doing amazing, even if you don't always see it 💪",
    "You bring light to places no one else can ✨",
    "The world is better because you're in it 🌎",
    "You are loved exactly as you are – no edits needed 💖",
    "You’re strong, funny, kind, and absolutely unforgettable 🔥",
    "You’re the definition of lovable and loved 💯",
    "You make even the small things magical 🌟",
    "You are everything I ever dreamed of and more "
]

if st.button("Click for a loving surprise 💘"):
    st.balloons()
    st.success(random.choice(affirmations))

# Footer
st.markdown("---")
st.markdown("Made with 💖 for Loz Dog. Always.")
