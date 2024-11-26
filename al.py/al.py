import streamlit as st
import datetime

st.set_page_config(page_title="Muhyl's Biography", layout="wide")

# CSS for custom styling
st.markdown("""
    <style>
    body {
        background-color: #ffe4e1; /* Light pink background */
    }
    .main-header {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #ff69b4; /* Hot pink text */
        margin-bottom: 20px;
    }
    .section-header {
        text-align: center;
        font-size: 25px;
        font-weight: bold;
        color: #ff1493; /* Deep pink text */
        margin: 20px 0;
    }
    .custom-container {
        background-color: #fff0f5; /* Lavender blush background */
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .social-icons img {
        margin: 0 10px;
    }
    input, textarea, select {
        border: 2px solid #ff69b4; /* Pink border */
        border-radius: 10px;
        padding: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state if not already initialized
if 'toggle_state' not in st.session_state:
    st.session_state.toggle_state = False
if 'name' not in st.session_state:
    st.session_state.name = "Al Muhyl G. Camsa"
if 'about_me' not in st.session_state:
    st.session_state.about_me = ("Hi I'm Al Muhyl! I love playing Mobile Legends and watching anime in my free time. When I'm not gaming or binge-watching my favorite shows, you can find me playing basketball.")
if 'mother_name' not in st.session_state:
    st.session_state.mother_name = "Marilou Camsa"
if 'father_name' not in st.session_state:
    st.session_state.father_name = "Ibrahim Camsa"
if 'mother_bday' not in st.session_state:
    st.session_state.mother_bday = datetime.date(1972, 9, 8)
if 'father_bday' not in st.session_state:
    st.session_state.father_bday = datetime.date(1969, 8, 13)
if 'high_school' not in st.session_state:
    st.session_state.high_school = "Amando A. Fabio Memorial National Highschool"
if 'senior_high_school' not in st.session_state:
    st.session_state.senior_high_school = "Toledo S. Pantilo Sr. Memorial National High School"
if 'college' not in st.session_state:
    st.session_state.college = "Surigao del Norte State University"
if 'hobbies' not in st.session_state:
    st.session_state.hobbies = "- I Play online games\n- Watch One Piece\n- Play Basketball"
if 'gender' not in st.session_state:
    st.session_state.gender = "Male"
if 'birthplace' not in st.session_state:
    st.session_state.birthplace = "Sta.Cruz, Placer, Surigao del Norte"
if 'current_address' not in st.session_state:
    st.session_state.current_address = "Sta.Cruz, Placer, Surigao del Norte"
if 'mybirthday' not in st.session_state:
    st.session_state.mybirthday = datetime.date(2005, 11, 8)  # Default birthdate (can be updated)

def toggle_button():
    st.session_state.toggle_state = not st.session_state.toggle_state

# Main Header
st.markdown('<div class="main-header">Muhyl\'s Biography</div>', unsafe_allow_html=True)

# Content Layout
with st.container():
    left_column, right_column = st.columns([2, 1])  # Adjust column ratio for better alignment

    with left_column:
        st.markdown('<div class="custom-container">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">Personal Details</div>', unsafe_allow_html=True)
        st.text_input("Name", st.session_state.name, key="name")
        birth_date = st.date_input("Date of Birth", st.session_state.mybirthday)
        st.session_state.mybirthday = birth_date
        st.session_state.age = (datetime.date.today() - birth_date).days // 365
        st.write(f"Age: {st.session_state.age} years old")
        st.text_input("Place of Birth", st.session_state.birthplace, key="birthplace")
        st.text_input("Current Address", st.session_state.current_address, key="current_address")
        st.text_area("What I do", st.session_state.hobbies, height=125, key='hobbies')
        st.text_area("About Me", st.session_state.about_me, height=200, key="about_me")
        st.markdown('</div>', unsafe_allow_html=True)

    with right_column:
        st.markdown('<div class="custom-container">', unsafe_allow_html=True)
        st.image("https://scontent.fcgy2-1.fna.fbcdn.net/v/t39.30808-1/467027618_1932016050616441_4950739363074378939_n.jpg?stp=c0.0.720.720a_dst-jpg_s200x200&_nc_cat=107&ccb=1-7&_nc_sid=50d2ac&_nc_eui2=AeHBp2Ppn4XHuAwulAHNnZpvy-izudzzFyXL6LO53PMXJW4-qSPqUaWDXbMhmWqDZFFHVyAp84zmzdvs57eWWzLz&_nc_ohc=v3GiBDW4rj4Q7kNvgFL3tlQ&_nc_zt=24&_nc_ht=scontent.fcgy2-1.fna&_nc_gid=A8N3q38M9T05-6WOn1wweJ9&oh=00_AYDaSBCHStWs3Ha73ytwPW5JzFiE1odxp_JXMlLk_NlrSQ&oe=674AEF3C", width=250)
        st.markdown('<div class="section-header">Family Background</div>', unsafe_allow_html=True)
        st.text_input("Mother's Name", st.session_state.mother_name, key="mother_name")
        st.date_input("Mother's Birthday", st.session_state.mother_bday, key="mother_bday")
        st.text_input("Father's Name", st.session_state.father_name, key="father_name")
        st.date_input("Father's Birthday", st.session_state.father_bday, key="father_bday")
        st.markdown('<div class="section-header">Educational Attainment</div>', unsafe_allow_html=True)
        st.text_input("High School", st.session_state.high_school, key="high_school")
        st.text_input("Senior High School", st.session_state.senior_high_school, key="senior_high_school")
        st.text_input("College", st.session_state.college, key="college")
        st.markdown('</div>', unsafe_allow_html=True)

# Achievements Section
st.markdown('<div class="custom-container">', unsafe_allow_html=True)
st.markdown('<div class="section-header">Achievements</div>', unsafe_allow_html=True)
if st.button("Show Achievements"):
    toggle_button()
if st.session_state.toggle_state:
    st.text_area("Achievements", "- With Honor\n", height=125)
    st.text_area("Game Achievements", "- Reach Mythical Immortal in Mobile Legends\n- Champion in ML tournament\n- Obtain Cosmic Clean\n- Obtain Divine Goddess\n- Top 54 Global using Kadita\n- Top 1 Surigao del Norte Selena", height=125)
st.markdown('</div>', unsafe_allow_html=True)

# Social Media Section
st.markdown('<div class="custom-container">', unsafe_allow_html=True)
st.markdown('<div class="section-header">Social Media Accounts</div>', unsafe_allow_html=True)
social_media_html = """
    <div class="social-icons" style="text-align: center;">
        <a href="https://www.facebook.com/jamesamerkhan" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook" width="40" height="40" />
        </a>
        <a href="https://www.instagram.com/muhyl.jpg/profilecard/?igsh=MTU3YnEydHE4ZGswaQ==" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/128/174/174855.png" alt="Instagram" width="40" height="40" />
        </a>
    </div>
"""
st.markdown(social_media_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
