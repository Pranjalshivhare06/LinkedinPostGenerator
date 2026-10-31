import streamlit as st 
from few_shots import FewShotsPosts 
from postGenerator import generate_post
length_options = ["Short", "Medium", "Long"]
language_options = ["English"]

def main():
    st.title("LinkedIn Post Generator")
    col1, col2, col3 = st.columns(3)
    fs = FewShotsPosts()
    with col1:
        selected_tag = st.selectbox("Title", options=fs.get_tags())

    with col2:
        selected_len = st.selectbox("Length", options=length_options)

    with col3:
        selected_lang = st.selectbox("Language", options=language_options)

    if st.button("Generate"):
        post = generate_post(selected_len, selected_lang, selected_tag)
        st.write(post)
if __name__ == "__main__":
    main()