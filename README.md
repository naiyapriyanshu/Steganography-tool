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
- Upload an image for encryption.
- Enter your secret message.
- Enter a password.
- Click "Encrypt and Save 🔐".
- Download the encrypted image.

2. 🔓 **Decryption (Retrieving the Message)**
- Upload the encrypted image.
- Enter the password.
- Click "Decrypt Message 🔓".
- View the decrypted message.

3. 🔮 **Future Scope**
- Implement AES encryption for additional security.
- Extend the project to video & audio steganography.

4. 📜 **License**
This project is open-source under the MIT License.

🚀 Contributions & Feedbacks are Welcome!
