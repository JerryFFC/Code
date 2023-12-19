import pandas as pd
from transcipt.readJSON import extract_context,transcriptFromJSON
from mentions.mentions import readMentions
import streamlit as st

json = transcriptFromJSON()
mentions = readMentions()


#print(extract_context(json, 'yes', num_words=5))

#title = st.text_input('Input Game name', 'lethal company')

text_input = st.text_input(
        "Enter a game name.",
        placeholder='lethal company')

df = extract_context(json, text_input, num_words=10)
print("Running")
st.dataframe(df)
print("Done")