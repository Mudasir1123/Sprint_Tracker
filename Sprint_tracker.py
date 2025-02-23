import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime

# ✅ Set page configuration at the very top
st.set_page_config(page_title="🧘 Mindful Moments", layout='wide', initial_sidebar_state="expanded")

# 🔄 Initialize session state for dark mode
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# 🌿 Custom CSS for Styling (Dark & Light Mode)
dark_mode_styles = """
    <style>
        body, .stApp {
            background-color: #222222;
            color: white;
        }
        .title { text-align: center; font-size: 28px; font-weight: bold; color: white; }
        .card { background: #333333; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(255,255,255,0.1); color: white; }
        
        /* Fix input text color */
        .stTextInput > div > div > input,
        .stRadio label, 
        .stSlider, 
        .stButton button, 
        .stDownloadButton button {
            color: black !important;
        }

        /* Fix placeholder color */
        ::placeholder { color: black !important; opacity: 1 !important; }

        /* Fix sliders and buttons */
        .stSlider div[role="slider"], .stButton button, .stDownloadButton button {
            background-color: #444 !important;
            color: black !important;
            border: 1px solid #888 !important;
        }
    </style>
"""

light_mode_styles = """
    <style>
        .title { text-align: center; font-size: 28px; font-weight: bold; }
        .card { background: #f4f4f4; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
"""

# 🌙 **Dark Mode Toggle**
dark_mode = st.sidebar.toggle("🌙 Enable Dark Mode")
st.session_state.dark_mode = dark_mode  # Update session state

# Apply the correct CSS based on the dark mode setting
if st.session_state.dark_mode:
    st.markdown(dark_mode_styles, unsafe_allow_html=True)
else:
    st.markdown(light_mode_styles, unsafe_allow_html=True)

# 🎯 **Header & Title**
st.markdown('<h1 class="title">🧘 Mindful Moments: Daily Well-Being Tracker</h1>', unsafe_allow_html=True)
st.write("Track your emotions, practice gratitude, and nurture mindfulness every day.")

# ✅ **Sidebar - User Profile**
st.sidebar.header("👤 Your Profile")
name = st.sidebar.text_input("Enter your name:", placeholder="Your Name")

current_date = datetime.now().strftime('%Y-%m-%d')

# 🌟 **Daily Affirmation**
affirmations = [
    "I am enough just as I am.",
    "Today, I choose to be kind to myself.",
    "I embrace the present moment with gratitude.",
    "My mind is calm, my heart is at peace.",
    "I deserve happiness and inner peace.",
]
st.sidebar.subheader("💡 Daily Affirmation")
st.sidebar.write(f"📢 *{random.choice(affirmations)}*")

# 🎭 **Mood Tracker**
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("😊 How are you feeling today?")
moods = ["Happy", "Calm", "Anxious", "Stressed", "Tired", "Energized"]
selected_mood = st.radio("Select your mood:", moods, horizontal=True)
st.markdown('</div>', unsafe_allow_html=True)

# 🌈 **Gratitude Journal**
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🙏 Gratitude Journal")
gr1 = st.text_input("1. Something I’m grateful for:", placeholder="Write here...")
gr2 = st.text_input("2. Another thing I appreciate:", placeholder="Write here...")
gr3 = st.text_input("3. One more reason to be thankful:", placeholder="Write here...")
st.markdown('</div>', unsafe_allow_html=True)

# 🌿 **Mindfulness Challenge of the Day**
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🌿 Mindfulness Challenge")
challenges = [
    "Take a 5-minute deep breathing break.",
    "Spend 10 minutes journaling your thoughts.",
    "Go for a short walk and observe your surroundings.",
    "Listen to calming music for 15 minutes.",
    "Practice guided meditation for relaxation.",
]
st.write(f"💬 Today's Challenge: *{random.choice(challenges)}*")
st.markdown('</div>', unsafe_allow_html=True)

# 🌬 **Breathing Exercise**
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🌬 Guided Breathing Exercise")
breath_time = st.slider("Set duration (seconds):", 10, 60, 30)
if st.button("Start Breathing Exercise"):
    st.success("🌿 Inhale... Hold... Exhale... Repeat...")
    time.sleep(breath_time)
    st.info("💆 Well done! Take a moment to relax.")
st.markdown('</div>', unsafe_allow_html=True)

# 📊 **Save & Display Progress**
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📊 Save & Track Your Progress")
if st.button("💾 Save Entry"):
    data = pd.DataFrame({
        "Name": [name if name else "Anonymous"],
        "Date": [current_date],
        "Mood": [selected_mood],
        "Gratitude 1": [gr1],
        "Gratitude 2": [gr2],
        "Gratitude 3": [gr3],
    })
    st.success("✅ Your mindfulness log has been saved! Keep nurturing your well-being.")
    st.dataframe(data)

    # 📥 Download Progress Data
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Your Log",
        data=csv,
        file_name=f"mindful_moments_{name}_{current_date}.csv",
        mime="text/csv",
    )
st.markdown('</div>', unsafe_allow_html=True)

# 📊 **Mood Trend Chart**
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📊 Mood Tracker Progress")
chart_data = pd.DataFrame(
    {"Mood": moods, "Occurrences": [2, 5, 3, 1, 4, 6]}
)
st.bar_chart(chart_data)
st.markdown('</div>', unsafe_allow_html=True)

st.sidebar.write("💡 Take care of your mind and body. You deserve peace and happiness! 🎶")
