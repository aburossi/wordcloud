import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(credentials)
spreadsheet = client.open("WordCloudInputs")  # Replace with your spreadsheet name
worksheet = spreadsheet.sheet1

def add_input_to_sheet(input_text):
    worksheet.append_row([input_text])

def get_all_inputs():
    return worksheet.col_values(1)

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

def main():
    st.title("Collaborative Word Cloud Generator")

    st.header("Input Text")
    user_input = st.text_area("Enter the text for the word cloud")

    if st.button("Submit"):
        if user_input.strip():
            add_input_to_sheet(user_input)
            st.success("Text added!")
        else:
            st.error("Please enter some text")

    if st.button("Generate Word Cloud"):
        all_inputs = get_all_inputs()
        combined_text = " ".join(all_inputs)
        if combined_text.strip():
            wordcloud = generate_wordcloud(combined_text)
            
            st.header("Word Cloud")
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.error("No text available to generate word cloud")

    if st.button("Clear All Inputs"):
        worksheet.clear()
        st.success("All inputs cleared!")

    all_inputs = get_all_inputs()
    if all_inputs:
        st.header("All User Inputs")
        st.write(all_inputs)

if __name__ == "__main__":
    main()
