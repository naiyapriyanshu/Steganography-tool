# to run: streamlit run stego_app.py
import streamlit as st
import cv2
import numpy as np
import tempfile
import os

# Set modern UI with dark cyberpunk theme and neon yellow highlights
def set_modern_ui():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
        .stApp {
            background: radial-gradient(circle, #111 30%, #222 100%);
            color: #FFD700;
            font-family: 'Orbitron', sans-serif;
        }
        .title-container {
            text-align: center;
            font-size: 3em;
            font-weight: bold;
            color: #FFD700;
            padding: 15px;
            text-shadow: 0px 0px 15px #FFD700;
        }
        .stButton > button {
            background-color: #333;
            color: #FFD700;
            border-radius: 10px;
            padding: 12px 25px;
            font-size: 1.2em;
            border: 2px solid #FFD700;
            transition: all 0.3s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #FFD700;
            color: #111;
            transform: scale(1.05);
        }
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {
            background-color: #222;
            color: #FFD700;
            border-radius: 8px;
            border: 1px solid #FFD700;
            padding: 10px;
            box-shadow: 0px 0px 10px #FFD700;
        }
        .stFileUploader > div > div > div > div > div {
            color: #FFD700;
        }
        .stMarkdown, .stSubheader, .stCaption, .stText {
            color: #FFD700;
        }
        .divider {
            height: 3px;
            background: linear-gradient(to right, transparent, #FFD700, transparent);
            margin: 20px 0;
        }
        .footer {
            text-align: center;
            font-size: 1em;
            margin-top: 20px;
            color: #FFD700;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
set_modern_ui()

st.markdown('<div class="title-container">🛡 Secure Image Steganography Portal</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Encryption Function
def hide_message(image_path, message, password):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        return None, "Error: Invalid image file!"
    
    full_message = password + "|" + message
    d = {chr(i): i for i in range(256)}
    n, m, z = 1, 0, 0
    msg_length = len(full_message)
    
    max_length = (img.shape[0] * img.shape[1] * 3) - 2
    if msg_length > max_length:
        return None, "Error: Message too long for this image!"
    
    img[0, 0, 0] = np.uint8(msg_length % 256)
    img[0, 0, 1] = np.uint8((msg_length // 256) % 256)

    for i in range(msg_length):
        img[n, m, z] = np.uint8(d[full_message[i]])
        m += 1
        if m >= img.shape[1]:
            m = 0
            n += 1
        z = (z + 1) % 3
    
    encrypted_image_path = "encrypted_image.png"
    cv2.imwrite(encrypted_image_path, img)
    return encrypted_image_path, "Message hidden successfully!"

# Decryption Function
def reveal_message(image_path, password):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        return "Error: Invalid image file!"
    
    d = {i: chr(i) for i in range(256)}
    msg_length = int(img[0, 0, 0]) + (int(img[0, 0, 1]) * 256)
    message = ""
    n, m, z = 1, 0, 0

    for i in range(msg_length):
        if n >= img.shape[0]:
            break
        message += d[int(img[n, m, z])]
        m += 1
        if m >= img.shape[1]:
            m = 0
            n += 1
        z = (z + 1) % 3
    
    if "|" not in message:
        return "Error: Decryption failed!"
    
    stored_password, secret_message = message.split("|", 1)
    return f"Decrypted Message: {secret_message}" if stored_password == password else "Error: Incorrect password!"

st.subheader("🔒 Hide a Secret Message")
uploaded_file = st.file_uploader("Choose an image for encryption", type=["png", "jpg", "bmp"])
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_image_path = temp_file.name
    st.image(temp_image_path, caption="Uploaded Image for Encryption", use_container_width=True)
    message = st.text_area("Enter your secret message")
    password = st.text_input("Enter a password", type="password")
    if st.button("Encrypt and Save 🔐"):
        with st.spinner("Encrypting..."):
            if temp_image_path and password:
                encrypted_image_path, result = hide_message(temp_image_path, message, password)
                if encrypted_image_path:
                    st.image(encrypted_image_path, caption="Encrypted Image", use_container_width=True)
                    with open(encrypted_image_path, "rb") as file:
                        st.download_button(label="Download Encrypted Image 💾", data=file, file_name="encrypted_image.png", mime="image/png")
                st.success(result)
            else:
                st.error("Please upload an image and enter a password!")

st.subheader("🔓 Reveal a Secret Message")
decrypt_file = st.file_uploader("Choose an image for decryption", type=["png", "jpg", "bmp"])
if decrypt_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_file.write(decrypt_file.read())
        decrypt_image_path = temp_file.name
    st.image(decrypt_image_path, caption="Uploaded Image for Decryption", use_container_width=True)
    decrypt_password = st.text_input("Enter the password to decrypt", type="password")
    if st.button("Decrypt Message 🔓"):
        with st.spinner("Decrypting..."):
            if decrypt_image_path and decrypt_password:
                decrypted_message = reveal_message(decrypt_image_path, decrypt_password)
                st.info(decrypted_message)
            else:
                st.error("Please upload an encrypted image and enter the correct password!")

# Add a help section
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
with st.expander("Help ❓"):
    st.markdown(
        """
        **How to use this app:**
        1. **Encrypt a message:**
            - Upload an image.
            - Enter your secret message.
            - Enter a password.
            - Click "Encrypt and Save 🔐".
            - Download the encrypted image.
        2. **Decrypt a message:**
            - Upload the encrypted image.
            - Enter the password.
            - Click "Decrypt Message 🔓".
            - View the decrypted message.
        """
    )

# Add a footer
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="footer">This project demonstrates secure image steganography techniques for hiding and revealing secret messages within images.</div>', unsafe_allow_html=True)
