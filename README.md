
# Note Summarizer and Quiz Generator

An AI-powered Streamlit application that transforms images of study notes into concise summaries, audio narration, and practice quizzes using Google's Gemini AI.

<img width="1852" height="970" alt="image" src="https://github.com/user-attachments/assets/966db9f1-5880-4901-b068-e39091d40358" /><br>
<img width="1760" height="918" alt="Screenshot_20261018_082338" src="https://github.com/user-attachments/assets/ff9d0887-4bb5-414f-8cf5-76596b82db7c" />

## Features

- **Image Upload:** Upload up to 3 images of study notes in JPG, JPEG, or PNG format.
- **AI Note Summarization:** Generate a concise summary of uploaded notes in approximately 150 words.
- **Text-to-Speech:** Convert generated notes into audio using Google Text-to-Speech (gTTS).
- **Quiz Generation:** Generate 10 practice questions based on the uploaded images, with answers provided at the end.
- **Difficulty Selection:** Choose Easy, Medium, or High difficulty.
- **Interactive UI:** Use a simple Streamlit interface to upload images, select difficulty, and view results.

## Technologies Used

- Python
- Streamlit
- Google Gemini API (`google-genai`)
- Pillow (PIL)
- gTTS
- python-dotenv

## Project Structure

```text
project/
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Linux / macOS**
```bash
source .venv/bin/activate
```

**Windows**
```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install streamlit google-genai pillow gTTS python-dotenv
```

Alternatively, create a `requirements.txt` file:

```text
streamlit
google-genai
Pillow
gTTS
python-dotenv
```

Then run:

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GIMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your actual Gemini API key. The variable name must match the one used in `app.py`.

Keep your API key private and never commit the `.env` file to a public repository.

### 5. Run the application

```bash
streamlit run app.py
```

Streamlit will provide a local URL where you can open the application in your browser.

## How to Use

1. Launch the application.
2. Upload up to three images containing study notes.
3. Select a difficulty level: Easy, Medium, or High.
4. Click **Submit to AI**.
5. Read the generated summary.
6. Play the audio narration of the summary.
7. Review the 10 generated quiz questions and their answers.

## How It Works

1. **Image Processing:** Uploaded images are opened using Pillow.
2. **AI Generation:** The Gemini model analyzes the images and generates a summary or quiz.
3. **Audio Conversion:** gTTS converts the summary text into spoken audio.
4. **Result Display:** Streamlit displays the summary, audio player, and quiz in the browser.

## Error Handling and Limitations

- The application is intended to accept a maximum of three images per submission.
- A valid Gemini API key and internet connection are required.
- Image uploads should contain readable text for better results.
- Gemini API errors, unsupported image content, and gTTS network failures should be handled to provide a more reliable user experience.
- The current implementation does not yet include comprehensive exception handling or persistent storage.
- Audio generation uses English by default.

## Future Improvements

- Add robust API and network error handling.
- Validate image count and file sizes before processing.
- Add support for multiple audio languages.
- Allow users to download summaries and quizzes.
- Improve Markdown-to-speech text cleaning.
- Add caching to avoid repeating expensive API calls.

