import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def generate_wordcloud(text, max_words, colormap):
    wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=max_words, colormap=colormap).generate(text)
    return wordcloud

def main():
    st.title("Word Cloud Generator")

    st.header("Input Text")
    user_input = st.text_area("Enter the text for the word cloud")

    st.sidebar.header("Customization Options")
    max_words = st.sidebar.slider("Max Words", 10, 200, 100)
    colormap = st.sidebar.selectbox("Colormap", plt.colormaps())

    if st.button("Generate Word Cloud"):
        if user_input.strip():
            wordcloud = generate_wordcloud(user_input, max_words, colormap)
            
            st.header("Word Cloud")
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.error("Please enter some text to generate the word cloud")

if __name__ == "__main__":
    main()
