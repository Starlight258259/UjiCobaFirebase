import os
from dotenv import load_dotenv  # Import dotenv
import firebase_admin
from firebase_admin import credentials, firestore
import logging

# === Setup Logging ===
logging.basicConfig(level=logging.ERROR, filename='firebase_error.log', filemode='a', format='%(asctime)s - %(message)s')

# === Load Environment Variables ===
load_dotenv()  # Memuat file .env

# === Path ke File Kredensial Firebase JSON ===
firebase_cred_path = os.getenv("FIREBASE_CREDENTIALS")

try:
    # Cek apakah file kredensial ada
    if not firebase_cred_path or not os.path.exists(firebase_cred_path):
        raise FileNotFoundError(f"File kredensial '{firebase_cred_path}' tidak ditemukan.")

    # Inisialisasi Firebase (hanya jika belum diinisialisasi)
    if not firebase_admin._apps:
        cred = credentials.Certificate(firebase_cred_path)
        firebase_admin.initialize_app(cred)

    # Inisialisasi Firestore
    db = firestore.client()
    logging.info("Firebase dan Firestore berhasil diinisialisasi.")

except Exception as e:
    logging.error(f"Error inisialisasi Firebase: {e}")
    db = None
