
import google.generativeai as genai
import streamlit as st

# Securely get your API Key from Streamlit Secrets
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error("Missing API Key! Please add it to Streamlit Secrets.")
    st.stop()

st.set_page_config(page_title="AI Viral Maker", page_icon="🔥")
st.title("🔥 Viral Content AI")
st.write("Turn any idea into 5 viral Tweets and 1 LinkedIn post instantly.")

user_text = st.text_area("Paste your article or idea here:", height=200)

if st.button("Generate Social Posts"):
    if user_text:
        with st.spinner("AI is thinking..."):
            prompt = f"Write 5 viral Tweets and 1 professional LinkedIn post from this content: {user_text}"
            response = model.generate_content(prompt)
            st.success("Done!")
            st.markdown(response.text)
            st.divider()
            st.write("### ❤️ Support the Creator")
            st.link_button("☕ Buy Me a Coffee", "https://www.buymeacoffee.com/")
    else:
        st.warning("Please enter some text first!")
      
