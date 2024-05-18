# Collaborative Word Cloud Generator

This Streamlit app allows students to collaboratively create word clouds by submitting their input text. The app collects the text inputs, stores them in a Google Sheets document, and generates a word cloud from the combined inputs.

## Features

- **Collaborative Input**: Students can submit their own text inputs.
- **Word Cloud Generation**: The app generates a word cloud from all the inputs.
- **Google Sheets Integration**: All inputs are stored in a Google Sheets document for easy management.

## How to Use

### Prerequisites

- A Google Cloud project with a Service Account and Google Sheets API enabled.
- Streamlit account for deploying the app.

### Setup

1. Clone the Repository:
   ```sh
   git clone https://github.com/your-username/wordcloud.git
   cd wordcloud
2. Install Dependencies:

pip install -r requirements.txt

3. Google Cloud Credentials:

- Create a Google Cloud project and enable the Google Sheets API.
- Create a Service Account and download the credentials JSON file.
- Add the credentials to your Streamlit secrets.

4. Streamlit Secrets:
- Go to your Streamlit Cloud dashboard.
- Navigate to the "Secrets" section.
- Add your Google Cloud credentials in the following format:

[google_credentials]
type = "service_account"
project_id = "your-project-id"
private_key_id = "some-private-key-id"
private_key = "-----BEGIN PRIVATE KEY-----\nYOUR-PRIVATE-KEY\n-----END PRIVATE KEY-----\n"
client_email = "your-service-account@your-project-id.iam.gserviceaccount.com"
client_id = "some-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account%40your-project-id.iam.gserviceaccount.com"

5. Deploy the App:

Push your repository to GitHub.
- Deploy the app on Streamlit Cloud by connecting to your GitHub repository.

### Usage Instructions
1. Run the App Locally:

streamlit run app.py

2. Submit Text:

- Open the app in your browser.
- Enter text in the input area and click "Submit".
- Click "Generate Word Cloud" to create a word cloud from all submitted texts.

### Notes
- Ensure that the Google Sheets document is shared with the service account email (found in the credentials JSON).
- Replace "WordCloudInputs" in the code with the actual name of your Google Sheets document.

Contributing
Feel free to fork this repository and submit pull requests. Contributions are welcome!

License
This project is licensed under the MIT License.

Contact
For any questions or feedback, please contact your copilot of trust.

Happy Teaching!
