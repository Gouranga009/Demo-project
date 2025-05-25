import streamlit as st

# Website Title :
st.title("Raiganj Technical :rainbow[Educational] Society")


# Header/Sub-header :
st.header("This is a Header..")

st.subheader("This is a Subheader..")


# Text :
st.text(" This is a text msg : Hello Student's 👋 ")


# Markdown :
st.markdown(" # This is a Markdown with hash (#)")

st.markdown(" #### This is a markdown with 4 hash (####)")


# Success / Green text :
st.success("Successfully Done box")


# Information / Skyblue text :
st.info("Information box")


# Warning / Yellow text :
st.warning("This is a Warning box ")


# Error / Red text :
st.error("This is a Error box")


# Exception :
st.exception("NameError('name python is not defiened')")


# Writing text super function :
st.write("Text with write :")


# Define range function :
st.write(range(10))


# Image import function :
from PIL import Image
img=Image.open("www.jpg")
st.image(img,width=750,caption="Simple Image")


# Video import function :
vid_file = open("video.mp4","rb")
video_bytes = vid_file.read()
st.video(video_bytes)


# Audio import function :
audio_file = open("music.mp3","rb").read()
st.audio(audio_file)


# Checkbox function :
if st.checkbox("Show / Hide"):
    st.text("Hi, This is a checkbox function hidden msg")


# Radio Button function :
stats = st.radio("Select your Gender :",("Male","Female","Others"))


# Link with radio button :
if stats == "Male":
    st.success("You choose Male")
elif stats == "Female":
    st.success("You choose Female")
else:
    st.success("You choose Others")


# Selectbox :
country = st.selectbox("Select your country :",["India","China","Russia","United States","Brazil","Australia"])
st.write(f"Your current country is : {country}  ")


# Multiselect :
language = st.multiselect("Select the programing language you know :",("C++","Java","Python","javaScript","Kotlin","Swift","C"))


# To get multiselected count :
st.write("You selected ",len(language),"language")


# Slider function :
label = st.slider("Select your label : ",1,5)


# Button function :
if st.button("Submit"):
    st.success("Submit Successfully !")


# Text input function :
name = st.text_input("Enter your name :","type here...")


# Text area input function :
massage = st.text_area("Enter your massage :","type here...")
#if st.button("Submit",key="1"):
   # result = massage.title()
    #st.success("Successful")


# Date input function :
import datetime
today = st.date_input("Today is :",datetime.datetime.now())


# Time input function :
the_time = st.time_input("The time is",datetime.time())


# Display json output :
st.text("Display json data")
st.json({"Name " : " Gouranga ",
          "Gender" : " Male "})

# Display code output :
st.text("Display raw code :")
st.code("import Streamlit as st")


# Display raw code with dataframe :
st.text("Display raw code with dataframe :")
with st.echo():
    import pandas as pd
    df = pd.DataFrame()


# Progress bar function :
st.text("Progress bar :")
import time 
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p+8)


# Spinner funtion :
st.text("This is a spinner :")
with st.spinner("Please wait..."):
    time.sleep(5)
st.success("Successfull submited ")


# Side bar function :
st.sidebar.header("About")
st.sidebar.text("This is my demo project")


# Side bar selectbox function :

