import streamlit as st
from func import find_rhyming_words, generate_lyrics, get_word_suggestions

def main():
    st.title("Song Writing Assistant🎵")
    
    #tabs for two different functionalities
    tab1,tab2 = st.tabs(["Rhyme Finder", "Lyrics Generator"])
    
    with tab1:
        st.header("Find Rhyming Words")
        
        #Input for rhyme finder
        word = st.text_input("Enter a word to find rhymes:", key="rhyme_input")
        
        if word:
            rhymes = find_rhyming_words(word)
            
            if rhymes:
                st.success(f"Found {len(rhymes)} rhyming words:")
                cols = st.columns(3)
                for idx, rhyme in enumerate(rhymes):
                    cols[idx % 3].write(f"{idx+1} - {rhyme}")
            else:
                st.warning("No rhyming words found. Try another word!")
                
                #Show word suggestions
                suggestions = get_word_suggestions(word)
                if suggestions:
                    st.info("You might want to try these similar words:")
                    st.write(", ".join(suggestions))
    
    with tab2:
        st.header("Generate Lyrics")
        
        #Input for lyrics generator
        seed_text = st.text_area(
            "Enter some seed text for lyrics generation:",
            height=150,
            help="Enter at least 3 to 4 sentences to get better results.",
            key="lyrics_input"
        )
        
        num_lines = st.slider(
            "Number of lines to generate:",
            min_value=1,
            max_value=10,
            value=1,
            key="num_lines"
        )
        
        if st.button("Generate Lyrics", key="generate_btn"):
            if seed_text.strip():
                with st.spinner("Generating lyrics..."):
                    lyrics = generate_lyrics(seed_text, num_lines)
                    
                    if "Error" in lyrics:
                        st.error(lyrics)
                    else:
                        st.success("Generated Lyrics:")
                        st.write(lyrics)
                        
                        #copy button
                        st.button(
                            "Copy to clipboard",
                            help="Click to copy the generated lyrics",
                        )
            else:
                st.error("Please enter some seed text first!")
    
    #footer information
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center'>
        Made with Streamlit | 
        Uses NLTK </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()