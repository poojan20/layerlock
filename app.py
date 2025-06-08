import streamlit as st
from fpdf import FPDF
import hashlib
from io import BytesIO

# Set page title, icon (favicon), and layout
st.set_page_config(
    page_title="LayerLock - Secure Text Encryptor",
    page_icon="icon.png",  # change to your favicon file path
    layout="centered",
)

# --- Style for army/secret intelligence theme ---
st.markdown(
    """
    <style>
    body {
        background-color: #0b1d0b;
        color: #7fff00;  /* Neon green */
        font-family: 'Courier New', monospace;
    }
    .stButton>button {
        background-color: #154215;
        color: #7fff00;
        border-radius: 5px;
        border: 1px solid #7fff00;
    }
    .stButton>button:hover {
        background-color: #7fff00;
        color: #0b1d0b;
        border: 1px solid #0b1d0b;
    }
    .stTextInput>div>input, .stSelectbox>div>div>select {
        background-color: #0b1d0b;
        color: #7fff00;
        border: 1px solid #7fff00;
        font-family: 'Courier New', monospace;
    }
    .stMarkdown {
        font-family: 'Courier New', monospace;
    }
    .css-1kyxreq {
        background-color: #0b1d0b !important;
    }
    .css-1d391kg {
        color: #7fff00 !important;
    }
    </style>
    """, unsafe_allow_html=True
)

# Encryption function
def encrypt_text(text):
    key = hashlib.sha256(text.encode()).hexdigest()[:10]
    encrypted = ''.join(chr(ord(c) ^ ord(k)) for c,k in zip(text, key*len(text)))
    return encrypted, key

# Decryption function
def decrypt_text(encrypted, key):
    try:
        decrypted = ''.join(chr(ord(c) ^ ord(k)) for c,k in zip(encrypted, key*len(encrypted)))
        return decrypted
    except Exception as e:
        return None

# PDF creation function
from io import BytesIO
from fpdf import FPDF

def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Courier", size=12)
    pdf.multi_cell(0, 10, text)
    
    pdf_str = pdf.output(dest='S').encode('latin1')  # get PDF as bytes string
    pdf_output = BytesIO(pdf_str)  # wrap in BytesIO
    pdf_output.seek(0)
    return pdf_output


st.title("LayerLock — Secure Text Encryptor")
st.write("Enter text to encrypt it into a secret file, or decrypt your encrypted file using your secret key.")

mode = st.radio("Choose Mode", ("Encrypt", "Decrypt"))

if mode == "Encrypt":
    plain_text = st.text_area("Enter text to encrypt", height=150)
    import streamlit.components.v1 as components

if st.button("Encrypt"):
    if not plain_text.strip():
        st.error("Please enter some text to encrypt.")
    else:
        encrypted_text, key = encrypt_text(plain_text)
        pdf_file = create_pdf(encrypted_text)
        st.success("Encryption successful!")

        st.markdown("### 🔑 Your 10-character Secret Key:")
        st.code(key, language='')

        # 🔘 Copy to clipboard button (HTML + JS)
        copy_button = f"""
        <script>
        function copyToClipboard(text) {{
            navigator.clipboard.writeText(text).then(function() {{
                console.log('Copied to clipboard');
            }}, function(err) {{
                console.error('Could not copy text: ', err);
            }});
        }}
        </script>
        
        """
        components.html(copy_button, height=50)

        st.download_button(
            label="Download Encrypted PDF",
            data=pdf_file,
            file_name="encrypted_text.pdf",
            mime="application/pdf",
        )


elif mode == "Decrypt":
    uploaded_file = st.file_uploader("Upload Encrypted PDF", type=["pdf"])
    secret_key = st.text_input("Enter your 10-character secret key")

    if st.button("Decrypt"):
        if not uploaded_file:
            st.error("Please upload the encrypted PDF file.")
        elif not secret_key or len(secret_key) != 10:
            st.error("Please enter a valid 10-character secret key.")
        else:
            try:
                from PyPDF2 import PdfReader
                reader = PdfReader(uploaded_file)
                encrypted_text = ""
                for page in reader.pages:
                    encrypted_text += page.extract_text()
                decrypted_text = decrypt_text(encrypted_text, secret_key)
                if decrypted_text is None:
                    st.error("Decryption failed. Invalid key or corrupted file.")
                else:
                    st.success("Decryption successful!")
                    st.text_area("Decrypted Text", decrypted_text, height=200)
            except Exception as e:
                st.error(f"Error reading PDF: {str(e)}")
