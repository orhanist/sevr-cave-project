import streamlit as st
import time
import pandas as pd
import pydeck as pdk

# -------------- 🚨 MUST BE FIRST: Page Config -------------------
st.set_page_config(page_title="Cave of Thawr", page_icon="🕌", layout="wide")

# -------------- Visitor Counter -------------------
if 'visits' not in st.session_state:
    st.session_state['visits'] = 1
else:
    st.session_state['visits'] += 1

# -------------- Custom Loading Screen -------------------
loading_placeholder = st.empty()
loading_placeholder.image("images/group_photo.jpg", width=300, caption="Loading... Please wait.")
time.sleep(2)
loading_placeholder.empty()

# -------------- Welcome Banner -------------------
st.markdown("""
<div style="background-color: #DFF6FF; padding: 20px; border-radius: 10px; text-align:center; animation: fadeIn 2s;">
    <h2 style="color:#023047;">👋 Welcome to Our Sevr Cave Hijrah Project!</h2>
</div>

<style>
@keyframes fadeIn {
  0% {opacity: 0;}
  100% {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

# -------------- Sidebar -------------------
st.sidebar.title("🕌 Navigation")
st.sidebar.markdown(f"👥 **Visitors so far:** {st.session_state['visits']}")
st.sidebar.markdown("---")
st.sidebar.image("images/video_qr.png", caption="Scan to watch our Skit", use_container_width=True)
st.sidebar.markdown("---")
st.sidebar.image("images/group_photo.jpg", caption="Our Team", use_container_width=True)
st.sidebar.markdown("""
**by Fatih / Orhan Abi**

Kerem / Saido / Namik / Abdullah / Ekrem / Numan
""")

# Sidebar Menu
section = st.sidebar.radio(
    "Select Section",
    ("Home", 
     "Location of the Cave", 
     "Route Map", 
     "Story of the Hijrah", 
     "Hijrah Timeline",
     "Quiz",
     "Reflection")
)

# -------------------- MAIN CONTENT ----------------------

if section == "Home":
    st.title("🕌 Cave of Thawr - The Migration Story")

    st.header("📜 Selected Qur'an Verses about the Hijrah")

    def animated_ayet_card(title, arabic, turkish, english):
        st.markdown(f"""
        <div style="
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
            animation: fadeIn 2s;
            position: relative;
            ">
            <h4 style="margin-top:0;">🕌 {title}</h4>
            <b>Arabic:</b><br>
            <i>{arabic}</i><br><br>
            <b>Turkish Translation:</b><br>
            "{turkish}"<br><br>
            <b>English Translation:</b><br>
            "{english}"
        </div>
        """, unsafe_allow_html=True)

    ayet1 = "وَجَعَلْنَا مِنۢ بَيْنِ أَيْدِيهِمْ سَدًّا وَمِنْ خَلْفِهِمْ سَدًّا فَأَغْشَيْنَـٰهُمْ فَهُمْ لَا يُبْصِرُونَ"
    animated_ayet_card("Yā-Sīn, 36:9", ayet1,
                       "Önlerine bir set, arkalarına da bir set çektik. Böylece onları kuşattık, artık göremezler.",
                       "And We have set before them a barrier and behind them a barrier and covered them, so they do not see.")

    st.markdown("---")

    ayet2 = "وَإِذْ يَمْكُرُ بِكَ ٱلَّذِينَ كَفَرُوا۟ لِيُثْبِتُوكَ أَوْ يَقْتُلُوكَ أَوْ يُخْرِجُوكَ ۚ وَيَمْكُرُونَ وَيَمْكُرُ ٱللَّهُ ۖ وَٱللَّهُ خَيْرُ ٱلْمَـٰكِرِينَ"
    animated_ayet_card("Al-Anfāl, 8:30", ayet2,
                       "Ey Muhammed! Hani inkâr edenler seni tutuklamak, öldürmek veya sürgün etmek için tuzak kuruyorlardı. Allah da onların tuzaklarını boşa çıkarıyordu. Allah tuzak kuranların en hayırlısıdır.",
                       "And [remember, O Muhammad], when those who disbelieved plotted against you to restrain you or kill you or evict you. But they plan, and Allah plans. And Allah is the best of planners.")

    st.markdown("---")

    st.image("images/sevr_cave.jpg", caption="Cave of Thawr - Present Day", use_container_width=True)

    st.header("Introduction")
    st.write("""
The Cave of Thawr holds an extraordinary and sacred place in Islamic history. It served as a refuge for Prophet Muhammad (peace be upon him) and his closest companion Abu Bakr as-Siddiq (may Allah be pleased with him) during the critical moments of the Hijrah — the migration from Mecca to Medina.

Under severe threat of assassination by the Quraysh, the Prophet and Abu Bakr strategically diverted their path southward, contrary to the expected northern route to Yathrib (Medina). They sought shelter in the rocky, secluded heights of Mount Thawr, approximately five kilometers from Mecca, in a small cave that providentially became a place of miracles and divine protection.

Inside the cave, they were safeguarded by miraculous signs: a spider spun its web across the cave’s entrance, and two pigeons nested nearby — deceptive natural signs that misled their pursuers.

Ultimately, after three days, the Prophet and Abu Bakr resumed their journey to Medina with the help of a hired guide, Abdullah ibn Uraiqit, successfully establishing the Muslim community that would forever alter world history.
    """)

    st.markdown("""
        <a href="#" style="text-decoration: none;">
            <button style="padding:10px 20px; background-color: #f0f2f6; border-radius: 10px; border: 1px solid #ccc; margin-top:20px;">
                🔝 Back to Top
            </button>
        </a>
    """, unsafe_allow_html=True)

elif section == "Location of the Cave":
    st.title("📍 Location of the Cave")

    cave_location = {"latitude": 21.3775, "longitude": 39.8508}
    
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/satellite-streets-v11',
        initial_view_state=pdk.ViewState(
            latitude=cave_location["latitude"],
            longitude=cave_location["longitude"],
            zoom=12,
            pitch=40,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=[cave_location],
                get_position='[longitude, latitude]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))

elif section == "Route Map":
    st.title("🗺️ Route of the Hijrah Journey (Mecca ➔ Cave ➔ Medina)")

    route_data = pd.DataFrame([
        {"name": "Mecca", "lat": 21.3891, "lon": 39.8579},
        {"name": "Cave of Thawr", "lat": 21.3775, "lon": 39.8508},
        {"name": "Medina", "lat": 24.5247, "lon": 39.5692},
    ])

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=22.5,
            longitude=39.7,
            zoom=5,
            pitch=30,
        ),
        layers=[
            pdk.Layer(
                "LineLayer",
                data=route_data,
                get_source_position="[lon, lat]",
                get_target_position="[lon, lat]",
                get_color=[0, 0, 255],
                auto_highlight=True,
                width_scale=10,
                width_min_pixels=2,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=route_data,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=5000,
            ),
        ],
    ))

# (Timeline, Quiz, Reflection gibi bölümler zaten var, istersen onları da güncelleyebilirim.)

# Footer
st.markdown("---")
st.markdown("**Developed with ❤️ using [Streamlit](https://streamlit.io/)**")
