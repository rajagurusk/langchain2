import streamlit as st
import requests

# Replace with your Cohere API key
API_KEY = 'QwqPSSuLlMzyiwvFNVWgceGPqXB1OQZHmUUCFdrj'

def generate_letter(prompt):
    COHERE_API_URL = 'https://api.cohere.ai/generate'  # Correct endpoint for text generation

    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'model': 'command-xlarge-nightly',  # Specify the model to use
        'prompt': prompt,
        'max_tokens': 300,  # Increase max tokens if you need longer output
        'temperature': 0.7  # Adjust the temperature parameter for creativity
    }
    
    try:
        response = requests.post(COHERE_API_URL, headers=headers, json=data)
        response.raise_for_status()
        generated_text = response.json().get('text', '').strip()
        return generated_text
    except requests.exceptions.HTTPError as err:
        st.error(f"HTTP error occurred: {err.response.status_code} - {err.response.reason}")
    except requests.exceptions.RequestException as err:
        st.error(f"Request error occurred: {err}")
    except Exception as err:
        st.error(f"Other error occurred: {err}")
    return None

def main():
    st.title('Letter Generator with Cohere API')
    
    # Input prompt from user
    prompt = st.text_area('Enter prompt for the letter generation', height=200)
    
    if st.button('Generate Letter'):
        if prompt:
            generated_letter = generate_letter(prompt)
            if generated_letter:
                st.subheader('Generated Letter:')
                st.write(generated_letter)
            else:
                st.warning('Failed to generate letter. Please try again.')
        else:
            st.warning('Please enter a prompt to generate the letter.')

if __name__ == "__main__":
    main()
