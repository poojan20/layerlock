LayerLock 🔐
A secure text encryption and decryption app built with Streamlit. It allows you to encrypt any text, download it as a PDF, and decrypt it using a unique key.

🔧 Features
Text Encryption: Encrypts any text using SHA-256 hashing.

PDF Generation: Saves the encrypted content into a downloadable PDF.

Key-Based Decryption: Decrypt using the PDF + 10-character key.

Streamlit UI: Interactive, responsive interface with easy navigation.

Clipboard Support: One-click copy for the decryption key.

📦 Requirements
Python 3.8+

streamlit

fpdf

hashlib

base64

io

Install dependencies using:

bash
Copy
Edit
pip install streamlit fpdf
🚀 How to Run
bash
Copy
Edit
streamlit run app.py
🛡️ Limitations
SHA-256 is a one-way hash and cannot be decrypted. The app simulates encryption/decryption by storing the original message temporarily, which may not be suitable for high-security use.

📁 Folder Structure
Copy
Edit
layerlock/
├── app.py
├── encrypted_text.pdf
├── README.md
└── ...
📌 Notes
Ideal for educational purposes and lightweight secure storage.

Extendable to support more robust encryption (AES, RSA).

📄 License
MIT License – use freely with attribution.