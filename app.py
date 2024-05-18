import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

def main():
    st.title("Word Cloud Generator")

    st.header("Input Text")
    user_input = st.text_area("Enter the text for the word cloud")

    if st.button("Generate Word Cloud"):
        if user_input.strip():
            wordcloud = generate_wordcloud(user_input)
            
            st.header("Word Cloud")
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.error("Please enter some text to generate the word cloud")

if __name__ == "__main__":
    main()
