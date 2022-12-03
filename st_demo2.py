
#Display texts with Streamlit
import streamlit as st
#Add sidebar to the app
st.sidebar.image("car.png",width=100)
st.sidebar.markdown("### My first Awesome App")
st.sidebar.markdown("Welcome to my first awesome app. This app is built using Streamlit and uses data source from redfin housing market data. I hope you enjoy!")

#Create three columns/filters
col1, col2, col3 = st.columns(3)
with col1:
    st.title ("this is the app title")
    st.header("this is the markdown")
    st.markdown("this is the header")
    st.subheader("this is the subheader")
    st.caption("this is the caption")
    st.code("x=2021")
    st.latex(r''' a+a r^1+a r^2+a r^3 ''')

#Display an image, video or audio file with Streamlit




"""st.checkbox(): This function returns a Boolean value.
 When the box is checked, it returns a True value,
  otherwise a False value. 
  
  st.button(): This function is used to display a
   button widget. 
   
   st.radio(): This function is used to display a
    radio button widget.
    
     st.selectbox(): This function is used to display 
     a select widget.
     
      st.multiselect(): This function is used to
       display a multiselect widget.

 st.select_slider(): This function is used to
  display a select slider widget.
  
 st.slider(): This function is used to display a
  slider widget.
"""
with col2:
    st.image("car.png")
    #st.audio("Audio.mp3")
    #st.video("video.mp4")
    st.checkbox('yes')
    st.button('Click')
    st.radio('Pick your gender',['Male','Female'])
    st.selectbox('Pick your gender',['Male','Female'])
    st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
    st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
    st.slider('Pick a number', 0,50)


#input
with col3:
    st.number_input('Pick a number', 0,10)
    st.text_input('Email address')
    st.date_input('Travelling date')
    st.time_input('School time')
    st.text_area('Description')
    st.file_uploader('Upload a photo')
    st.color_picker('Choose your favorite color')


