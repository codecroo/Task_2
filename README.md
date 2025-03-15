# Song Writing Assistant🎵

A Streamlit-based creative writing assistant that helps you find rhyming words and generate song lyrics using Google's Gemini AI.

## Features

- **Rhyme Finder**: Find rhyming words for your lyrics
- **AI Lyrics Generator**: Generate creative lyrics using Google's Gemini AI
- **Word Suggestions**: Get word suggestions when rhymes aren't found

## Technical Details

The application uses the following key components:

- **Google Gemini AI**: For creative and contextual lyrics generation
- **NLTK**: For natural language processing
- **Pronouncing**: For finding rhyming words
- **Streamlit**: For the web interface

## Setup Instructions

1. Install Python 3.11 or later
2. Install the required packages:
   ```bash
   pip install streamlit nltk pronouncing google-generativeai
   ```

3. Set up your Google API key in the environment variables
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage Tips

- For best results, provide clear themes or starting lines for lyrics generation
- Adjust the number of lines to generate different length compositions
- Try different seed texts to get varied results
- Use the rhyme finder to create rhyming patterns in your lyrics

## Requirements

- Python 3.11+
- streamlit>=1.43.2
- nltk>=3.9.1
- pronouncing>=0.2.0
- google-generativeai

## How It Works

The application uses:
- Google's Gemini AI for creative lyrics generation
- Pronouncing dictionary for finding rhyming words
- NLTK for word suggestions and text processing
- Streamlit's interactive components for the user interface

## Notes

- The lyrics generator uses Google's Gemini AI model for high-quality, creative output
- Word suggestions are provided when exact rhymes aren't found
- The interface is designed to be intuitive and user-friendly

- **Developed by Parth Delvadiya**
