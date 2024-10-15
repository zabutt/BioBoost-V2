import streamlit as st
import google.generativeai as genai

# Configure the Google Gemini API (you'll need to set this up)
genai.configure(api_key='AIzaSyDa7tTO-H2l1OqNbhVK4r6I_1hTcdhXi58')

# Set up the model
model = genai.GenerativeModel('gemini-pro')

def generate_bio(profession, bio_type, platform):
    prompt = f"Generate a {bio_type} for a {profession} on {platform}. Include appropriate emojis. Keep it concise and suitable for the platform's character limits."
    response = model.generate_content(prompt)
    return response.text

st.title('🚀 BioBoost: AI-Powered Social Media Bio Generator')

# Profession selection
professions = [
    'Programmer', 'Doctor', 'Businessman', 'Student', 'Retired',
    'Teacher', 'Artist', 'Entrepreneur', 'Athlete', 'Scientist'
]
profession = st.selectbox('Select your profession', professions)

# Bio type selection
bio_types = [
    'Professional Bio', 'Creative/Artistic Bio', 'Humorous Bio',
    'Minimalist Bio', 'Inspirational Bio', 'Storytelling Bio'
]
bio_type = st.selectbox('Select a bio type', bio_types)

# Social media platform selection
platforms = ['Twitter', 'Facebook', 'LinkedIn', 'Instagram', 'TikTok']
platform = st.selectbox('Select a social media platform', platforms)

if st.button('Generate Bio'):
    with st.spinner('Generating your bio...'):
        generated_bio = generate_bio(profession, bio_type, platform)
    st.text_area('Your generated bio:', generated_bio, height=150)
    st.success('Bio generated successfully!')
    if st.button('Copy to Clipboard'):
        st.write('Bio copied to clipboard!')
        st.experimental_set_query_params(bio=generated_bio)

st.markdown('---')
st.markdown('Created with ❤️ by BioBoost')
