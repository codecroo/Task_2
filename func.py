import nltk
import pronouncing
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Download required NLTK data with explicit error handling
def download_nltk_data():
    required_packages = ['words', 'averaged_perceptron_tagger']
    for package in required_packages:
        try:
            nltk.download(package, quiet=True)
        except Exception as e:
            print("Error downloading {}: {}".format(package, str(e)))
# Fetch initial NLTK Data
download_nltk_data()
load_dotenv()
# Configure Gemini API with error handling
try:
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    model = genai.GenerativeModel('gemini-2.0-flash')
except Exception as e:
    print(f"Error initializing Gemini API: {str(e)}")
    model = None

def find_rhyming_words(word):
    """Find rhyming words using the pronouncing library."""
    if not word:
        return []

    try:
        rhymes = pronouncing.rhymes(word.lower())
        # Remove duplicates limit the results to twenty
        return list(set(rhymes))[:20]
    except Exception as e:
        return []

def clean_text(text):
    """Clean and prepare text for processing."""
    # Basic text cleaning
    text = text.strip()
    try:
        # Simple sentence splitting by common punctuation
        sentences = [s.strip() for s in text.replace('!', '.').replace('?', '.').split('.') if s.strip()]
        return ' '.join(sentences)
    except Exception:
        return text

def generate_lyrics(seed_text, num_lines=4):
    """Generate lyrics using Google's Gemini model."""
    if not model:
        return "Error: Lyrics generation is currently unavailable. Please check your API key and try again."

    if len(seed_text.strip()) < 5:
        return "Please provide more seed text (at least 5 characters)."

    try:
        # Prepare the prompt
        prompt = f"""
        Explain how to write {num_lines} lines of song lyrics based on this theme:
        "{seed_text}"

        Rules:
        1. Each line must be a complete phrase
        2. Include natural rhyming where possible
        3. Keep a consistent theme and mood
        4. Be creative and poetic
        5. write every line in proper alignment one sentence in one line and another rhyme in second line

        Return only the lyrics, one line per line.
        """

        #Generate lyrics with safety settings
        response = model.generate_content(
            prompt,
            safety_settings=[
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            ],
            generation_config={
                'temperature': 0.7,
                'candidate_count': 1,
                'max_output_tokens': 1024,
            }
        )

        if not response or not response.text:
            return "Could not generate lyrics. Please try again with different seed text."
        
        #Process the response
        lines = [line.strip() for line in response.text.split('\n') if line.strip()]
        if not lines:
            return "Could not generate meaningful lyrics. Please try again."

        return '\n'.join(lines[:num_lines])

    except Exception as e:
        error_msg = str(e)
        return f"Error generating lyrics: Please ensure your API key is correct and try again. Technical details: {error_msg}"

def get_word_suggestions(word):
    """Get related words using NLTK."""
    try:
        from nltk.corpus import words
        word_list = words.words()
        suggestions = [w for w in word_list if w.startswith(word.lower())][:10]
        return suggestions
    except Exception:
        return []