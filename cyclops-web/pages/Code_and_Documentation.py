import streamlit as st
from codeSnippets import serialConnectionCode, objectDetectionCode

st.markdown("# Code & Documentation")
st.sidebar.markdown("# Code & Documentation")

st.markdown('### Serial Connction between PC and Arduino')
st.code(serialConnectionCode, language="python", line_numbers=False)

st.markdown('### Object Detection with OpenCV2 & YOLOv4')
st.code(objectDetectionCode, language="python", line_numbers=False)