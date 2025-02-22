# 🖼️ Secure Image Steganography Portal

🔒 **Hide secret messages inside images using Steganography**  

## 📌 Overview
This project implements **steganography** to embed **secret messages inside images** by manipulating pixel values in the **RGB color channels**. This enables **secure communication** while keeping the hidden data undetectable to the human eye.

## 🚀 Features
✅ Hide text messages inside images without visual distortion  
✅ Password-protected **encryption & decryption**  
✅ Uses **Python & OpenCV** for image processing  
✅ Supports **JPG, BMP, PNG** formats  
✅ **Streamlit-based web interface**  

## 🛠️ Technologies Used
- **Python 3.11**  
- **Streamlit** – Web application framework  
- **OpenCV (cv2)** – Image processing  
- **NumPy** – Data manipulation  

## 📂 Project Structure
📁 stegano/  
│-- stego_app.py # Main script for the Streamlit app  
│-- README.md # Documentation  
│-- .gitignore # Files to ignore in Git  

## 📥 Installation & Setup
1. **Clone the repository**
   git clone https://github.com/yourusername/stegano.git
   cd stegano
   
2. **Install the required packages**
   pip install -r requirements.txt

3. **Run the Streamlit app**
   streamlit run stego_app.py

## 🖼️ Usage
1. 🔑 **Encryption (Hiding a Message)**
  1. Upload an image for encryption.
  2. Enter your secret message.
  3. Enter a password.
  4. Click "Encrypt and Save 🔐".
  5. Download the encrypted image.

2. 🔓 **Decryption (Retrieving the Message)**
  1. Upload the encrypted image.
  2. Enter the password.
  3. Click "Decrypt Message 🔓".
  4. View the decrypted message.

3. 🔮 **Future Scope**
  1. Implement AES encryption for additional security.
  2. Extend the project to video & audio steganography.

4. 📜 **License**
This project is open-source under the MIT License.

🚀 Contributions & Feedbacks are Welcome!
