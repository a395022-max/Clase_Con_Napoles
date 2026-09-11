import streamlit as st 

st.title("This is my app ")
st.button("click here ")
st.ballons()
import streamlit as st

st.text("This is text\n[and more text](that's not a Markdown link).")
import streamlit as st

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")
