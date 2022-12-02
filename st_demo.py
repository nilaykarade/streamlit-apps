import streamlit as st
#adv. input
tnc=st.checkbox("I agree")
man_or_machine=st.checkbox("I not a robot",disabled=True)
st.radio('Select your gender',['M','F'])
st.selectbox('Select your course',['DS','DM','CS'])
st.multiselect('Select your course',['DS','DM','CS'])
st.slider("Pickup a numner",0,10)

#input
st.text_input("enter name")
st.text_input("enter password",type="password")
st.number_input("enter age", max_value=100,min_value=1)
st.date_input("Enter DOB")
st.time_input("enter time")
st.color_picker("choose your fav. color")
st.file_uploader('upload a file')


#input and event handling
name=st.text_input("enter username")
btn_clicked=st.button('Submit')

if btn_clicked:
    st.info("Welcome "+name)

#Media
st.image("car.png",width=100)
st.audio("song1.mp3")
st.video("video1.mp4")


#Show text
st.title("Welcome")

st.header("DS class")

st.subheader("Batch 1")
age=33
st.write("Age = ",age)

st.code("car_age = 33")

st.success("XYZ")
st.info("XYZ")
st.warning("XYZ")

