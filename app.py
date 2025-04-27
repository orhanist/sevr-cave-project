import streamlit as st
import pandas as pd
import pydeck as pdk

# Page config
st.set_page_config(page_title="Cave of Thawr", page_icon="🕌", layout="wide")

# Sidebar
st.sidebar.title("🕌 Navigation")
st.sidebar.markdown("Use the options below to explore:")

st.sidebar.image("images/video_qr.png", caption="Scan to watch our Skit", use_container_width=True)
st.sidebar.markdown("---")
st.sidebar.image("images/group_photo.jpg", caption="Our Team", use_container_width=True)
st.sidebar.markdown("""
**by Kerem / Saido / Namik / Abdullah / Ekrem / Numan**

by Fatih/Orhan abi
""")

section = st.sidebar.radio(
    "Select Section",
    ("Home", 
     "Location of the Cave", 
     "Story of the Hijrah", 
     "Hijrah Timeline",
     "Quiz",
     "Reflection")
)

# -------------------- MAIN CONTENT ----------------------

if section == "Home":
    st.title("🕌 Cave of Thawr - The Migration Story")
    st.video("https://youtu.be/bCD9-_y84Zk?si=mdeb2lWwKzVIMt5x")
    st.header("📜 Selected Qur'an Verses about the Hijrah")

    # Ayet Cards with Animation
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

        <style>
        @keyframes fadeIn {{
          0% {{ opacity: 0; }}
          100% {{ opacity: 1; }}
        }}
        </style>
        """, unsafe_allow_html=True)

    # Yasin 36:9
    ayet1 = "وَجَعَلْنَا مِنۢ بَيْنِ أَيْدِيهِمْ سَدًّا وَمِنْ خَلْفِهِمْ سَدًّا فَأَغْشَيْنَـٰهُمْ فَهُمْ لَا يُبْصِرُونَ"
    animated_ayet_card("Yā-Sīn, 36:9", ayet1,
                       "Onların önlerine bir set, arkalarına bir set yaptık; böylece onları öylesine perdeleyip kuşattık ki artık hiçbir şey göremezler.",
                       "And We have set before them a barrier and behind them a barrier and covered them, so they do not see.")

    if st.button("📋 Copy Yā-Sīn 36:9 Arabic"):
        st.code(ayet1)

    st.markdown("---")

    # Al-Anfal 8:30
    ayet2 = "وَإِذْ يَمْكُرُ بِكَ ٱلَّذِينَ كَفَرُوا۟ لِيُثْبِتُوكَ أَوْ يَقْتُلُوكَ أَوْ يُخْرِجُوكَ ۚ وَيَمْكُرُونَ وَيَمْكُرُ ٱللَّهُ ۖ وَٱللَّهُ خَيْرُ ٱلْمَـٰكِرِينَ"
    animated_ayet_card("Al-Anfāl, 8:30", ayet2,
                       "Hani bir zamanlar kâfirler ya seni tutuklayıp hapsetmek veya öldürmek ya da yurdundan zorla çıkarmak için bir takım tuzaklar kuruyorlardı. Onlar böyle tuzaklar hazırlayadursunlar, ama Allah da onların tuzaklarına karşılık verecektir. Çünkü Allah, tuzak kuranlara en güzel karşılığı verendir.",
                       "And [remember, O Muhammad], when those who disbelieved plotted against you to restrain you or kill you or evict you. But they plan, and Allah plans. And Allah is the best of planners.")

    if st.button("📋 Copy Al-Anfāl 8:30 Arabic"):
        st.code(ayet2)

    st.markdown("---")

    st.image("images/sevr_cave.jpg", caption="Cave of Thawr - Present Day", use_container_width=True)

    st.header("Introduction")
    st.write("""
The Cave of Thawr (Ghar al-Thawr) holds an extraordinary and sacred place in Islamic history. 
It served as a refuge for Prophet Muhammad (peace be upon him) and his closest companion Abu Bakr as-Siddiq 
(may Allah be pleased with him) during the critical moments of the Hijrah — the migration from Mecca to Medina.

Under severe threat of assassination by the Quraysh, the Prophet and Abu Bakr strategically diverted their path southward, 
contrary to the expected northern route to Yathrib (Medina). They sought shelter in the rocky, secluded heights of Mount Thawr, 
approximately five kilometers from Mecca, in a small cave that providentially became a place of miracles and divine protection.

Inside the narrow, hidden cave, over the course of three tense days and nights, they were safeguarded by miraculous signs: 
a spider spun its web across the cave’s entrance, and two pigeons nested nearby — deceptive natural signs that misled their pursuers.

This cave was perfectly positioned and shaped for concealment: it could only be entered by crawling, 
and inside, occupants could see outside, but those outside could not see within.

During their hiding, Abdullah ibn Abi Bakr (the son of Abu Bakr) brought news updates at night, 
while a shepherd, Amir ibn Fuhayrah, allowed sheep to graze around the cave during the day, masking their tracks and providing milk.

Ultimately, after three days, the Prophet and Abu Bakr resumed their journey to Medina with the help of a hired guide, 
Abdullah ibn Uraiqit, successfully establishing the Muslim community that would forever alter world history.
    """)

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

    st.header("🌍 3D View of Jabal Thawr (External)")
    st.components.v1.iframe("https://peakvisor.com/peak/jabal-thawr.html", height=600)

elif section == "Story of the Hijrah":
    st.title("📖 The Story Unfolds")

    story_part = st.radio(
        "Choose a part of the story:",
        ("The Escape from Mecca", 
         "Arrival at the Cave", 
         "The Three Days in Hiding", 
         "Departure towards Medina")
    )

    if story_part == "The Escape from Mecca":
        st.subheader("The Escape from Mecca")
        st.write("""
In 622 CE, Prophet Muhammad (pbuh) planned a secret migration to Medina.
Quraysh leaders plotted to kill him, but he escaped under the cover of night,
heading south instead of north to avoid pursuers.
        """)
        st.image("images/mecca_escape.jpg", caption="Escape from Mecca", use_container_width=True)

    elif story_part == "Arrival at the Cave":
        st.subheader("Arrival at the Cave")
        st.write("""
Upon reaching the Cave of Thawr, Abu Bakr inspected the interior for dangers.
He suffered a snake bite but bore the pain silently until Prophet Muhammad (pbuh) healed him with his blessed touch.
        """)
        st.image("images/cave_entry.jpg", caption="Entry into the Cave", use_container_width=True)

    elif story_part == "The Three Days in Hiding":
        st.subheader("The Three Days in Hiding")
        st.write("""
A spider spun a web, and pigeons nested outside, misleading the Quraysh.
Meanwhile, Abdullah ibn Abi Bakr gathered intelligence, and Amir ibn Fuhayrah tended the sheep to erase tracks.
        """)
        st.image("images/spider_pigeons.jpg", caption="The Spider's Web and Pigeons", use_container_width=True)

    elif story_part == "Departure towards Medina":
        st.subheader("Departure towards Medina")
        st.write("""
After three days, they departed stealthily guided by Abdullah ibn Uraiqit,
beginning the momentous journey that would lead to the establishment of the Islamic community in Medina.
        """)
        st.image("images/departure_medina.jpg", caption="Journey to Medina", use_container_width=True)

elif section == "Hijrah Timeline":
    st.title("🕰️ Hijrah Timeline")
    st.markdown("""
- **610 CE** - First revelation received by Prophet Muhammad.
- **613 CE** - Public preaching of Islam begins.
- **615 CE** - Early Muslims migrate to Abyssinia.
- **622 CE** - Prophet Muhammad migrates to Medina (Hijrah).
- **624 CE** - Battle of Badr.
- **632 CE** - Prophet Muhammad's final pilgrimage and passing away.
    """)

elif section == "Quiz":
    st.title("🧠 Test Your Knowledge")
    st.markdown("### How many days did Prophet Muhammad and Abu Bakr stay in the Cave of Thawr?")
    answer = st.radio("Choose one:", ["1 day", "2 days", "3 days", "4 days"])

    if st.button("Check Answer"):
        if answer == "3 days":
            st.success("✅ Correct! They stayed 3 days.")
        else:
            st.error("❌ Incorrect. The correct answer is 3 days.")

elif section == "Reflection":
    st.title("🧠 Reflection")
    st.write("""
The story of the Cave of Thawr embodies trust, strategy, patience, and perseverance.
It remains a powerful example of unwavering faith under pressure, teaching timeless lessons for humanity.
    """)

# Footer
st.markdown("---")
st.markdown("**Developed with ❤️ using [Streamlit](https://streamlit.io/)**")
