# LayerLock 🔐

LayerLock is a secure text encryption and decryption tool built with Python and Streamlit. It allows you to encrypt any text, export the encrypted version as a PDF along with a unique 10-character key, and later decrypt the file using that key.

---

## 🚀 Features

- 🔒 Text encryption using SHA-256
- 📄 Encrypted text PDF generation
- 🔑 Unique 10-character key generation
- 📥 Decryption using PDF + key
- 🖥️ Simple, responsive Streamlit UI
- 📋 Copy-to-clipboard support for key

---

## 🛠️ Requirements

Install required packages:

```bash
pip install streamlit fpdf
```

---

## 💻 How to Run

```bash
streamlit run app.py
```

---

## 📁 File Structure

```
layerlock/
├── app.py          # Main Streamlit app
├── README.md       # Project documentation
```

---

## ⚠️ Important Note

LayerLock uses SHA-256 hashing for encryption. Since SHA-256 is a one-way function, the app mimics decryption by comparing stored hashes. This is not suited for real-world sensitive data encryption but is excellent for learning and demonstration purposes.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤝 Contributions

Contributions, issues, and feature requests are welcome. Feel free to fork the repo and submit pull requests.
