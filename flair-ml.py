import streamlit as st
from flair.models import TextClassifier
from flair.data import Sentence
classifier = TextClassifier.load('en-sentiment')
st.title('Sentiment Analysis')
st.subheader('Display the sentiments according to the text to be enter below')
ss=st.text_input('Enter Text Here : ')
if ss != '':
    sentence = Sentence(ss)
    with st.spinner('Predicting...'):
        classifier.predict(sentence)
        
    st.write('Prediction:')
    st.write(sentence.labels[0].value,'with',sentence.labels[0].score*100,'% Confidence of model')