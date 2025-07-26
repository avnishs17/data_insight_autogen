# Data Insight AutoGen

A Streamlit application for analyzing CSV data using AutoGen agents with Docker code execution.

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd data_insight_autogen
```

2. Install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory and add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

4. Make sure Docker is installed and running on your system.

## How to Run

1. Start the Streamlit app:
```bash
streamlit run streamlit_app.py
```

2. Open your browser and go to `http://localhost:8501`

3. Upload a CSV file using the file uploader

4. Enter your analysis task in the chat input

5. The app will process your data using AutoGen agents and display the results

## Features

- CSV file upload and processing
- AI-powered data analysis using AutoGen agents
- Docker-based code execution for safety
- Interactive chat interface
- Automatic visualization generation
