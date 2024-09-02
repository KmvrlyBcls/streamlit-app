import streamlit as st

st.set_page_config(layout="wide")


with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


image_path = 'images/kim.png'
friends_images = [
    'images/friend3.jpg',
    'images/friend1.jpg',
    'images/friend2.jpg'
]
dog1_video_path = 'videos/pet1_video.mp4'
dog2_video_path = 'videos/pet2_video.mp4'
dog3_video_path = 'videos/pet3_video.mp4'
song1_path = 'songs/song1.mp3'
song2_path = 'songs/song2.mp3'
song3_path = 'songs/song3.mp3'
resume_file = 'File/Resume.pdf'


st.markdown("""
    <div class="navbar">
        <a href="#home">Home</a>
        <a href="#achievements">Achievements</a>
        <a href="#hobbies">Hobbies</a>
        <a href="#likes">Likes & Dislikes</a>
        <a href="#friends">Friends</a>
        <a href="#sasha">My Dog</a>
        <a href="#songs">Favorite Songs</a>
    </div>
""", unsafe_allow_html=True)


st.markdown("<a id='home'></a>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])

with col1:
    st.markdown('<div class="profile-image-container">', unsafe_allow_html=True)
    st.image(image_path, width=300)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    col2_1, col2_2 = st.columns([4, 1])
    
    with col2_1:
        st.markdown("<div class='title'>Kimverly Bacalso</div>", unsafe_allow_html=True)
        st.markdown("<div class='subtitle'>Bachelor of Science in Information Technology</div>", unsafe_allow_html=True)
        st.markdown("<div class='details'>Cebu Institute of Technology University</div>", unsafe_allow_html=True)
    
    with col2_2:
       
        with open(resume_file, 'rb') as file:
            st.download_button(
                label="Download Resume",
                data=file,
                file_name='Resume.pdf',
                mime='application/pdf'
            )
    
  
    col1, col2, col3, col4, col5, col6 = st.columns([1, 6, 1, 6, 1, 6])

    with col1:
        st.image("images/fb.jpg", width=30)

    with col2:
        st.markdown("""
        <a href="https://www.facebook.com/Kmvrly.Bcls12" target="_blank" style="text-decoration: none; color: inherit;">
            Facebook
        </a>
    """, unsafe_allow_html=True)

    with col3:
        st.image("images/ig.jpg", width=30)

    with col4:
        st.markdown("""
        <a href="https://www.instagram.com/itskimmm12/" target="_blank" style="text-decoration: none; color: inherit;">
            Instagram
        </a>
        """, unsafe_allow_html=True)

    with col5:
        st.image("images/github.jpg", width=30)

    with col6:
        st.markdown("""
        <a href="https://github.com/KmvrlyBcls" target="_blank" style="text-decoration: none; color: inherit;">
            Github
        </a>
        """, unsafe_allow_html=True)

st.write('<div class="stDivider"></div>', unsafe_allow_html=True)


st.markdown("<a id='achievements'></a>", unsafe_allow_html=True)
st.markdown("<h3>Achievements</h3>", unsafe_allow_html=True)
st.markdown("""
<ul class='details'>
<li>Completed a comprehensive web development course.</li>
<li>Huawei HCIA_Storage Passer</li>
<li>Huawei Information Representation and Data Organization Passer</li>
</ul>
""", unsafe_allow_html=True)

st.write('<div class="stDivider"></div>', unsafe_allow_html=True)


st.markdown("<a id='hobbies'></a>", unsafe_allow_html=True)
st.markdown("<h3>Hobbies</h3>", unsafe_allow_html=True)
st.markdown("""
<ul class='details'>
<li>Playing Online Games</li>
<li>Reading Novels</li>
<li>Playing Badminton</li>
<li>Singing</li>
</ul>
""", unsafe_allow_html=True)

st.write('<div class="stDivider"></div>', unsafe_allow_html=True)


st.markdown("<a id='likes'></a>", unsafe_allow_html=True)
col3, col4 = st.columns([1, 1])

with col3:
    st.markdown("<h3>Likes</h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul class='details'>
    <li>Learning new programming languages</li>
    <li>Collaborating on tech projects</li>
    <li>Outdoor activities and hiking</li>
    </ul>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("<h3>Dislikes</h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul class='details'>
    <li>Procrastination</li>
    <li>Poorly documented code</li>
    <li>Unreliable internet connection</li>
    </ul>
    """, unsafe_allow_html=True)

st.write('<div class="stDivider"></div>', unsafe_allow_html=True)


st.markdown("<a id='friends'></a>", unsafe_allow_html=True)
st.markdown("<h2>My Friends</h2>", unsafe_allow_html=True)

cols = st.columns(len(friends_images))
for col, img_path in zip(cols, friends_images):
    with col:
        st.image(img_path, use_column_width=True)

st.write('<div class="stDivider"></div>', unsafe_allow_html=True)


st.markdown("<a id='sasha'></a>", unsafe_allow_html=True)
st.markdown("<h2>My Dog</h2>", unsafe_allow_html=True)

col5, col6, col7 = st.columns([1, 1, 1])

with col5:
    st.video(dog1_video_path)

with col6:
    st.video(dog2_video_path)

with col7:
    st.video(dog3_video_path)

st.write('<div class="stDivider"></div>', unsafe_allow_html=True)


st.markdown("<a id='songs'></a>", unsafe_allow_html=True)
st.markdown("<h2>My Favorite Songs</h2>", unsafe_allow_html=True)

st.write("Sining")
st.audio(song1_path, format='audio/mp3')

st.write("Best Part")
st.audio(song2_path, format='audio/mp3')

st.write("Hoodie")
st.audio(song3_path, format='audio/mp3')
