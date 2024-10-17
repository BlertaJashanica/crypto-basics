from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from secretsharing import SecretSharer
import os
import base64

# 1. De zin die je wilt versleutelen
plaintext = b"Dit is een geheime boodschap."

# 2. Genereer een willekeurige AES-sleutel (32 bytes voor AES-256)
aes_key = os.urandom(32)

# 3. Versleuteling van de plaintext met AES-256 in CBC-modus
def encrypt_message(message, key):
    padder = padding.PKCS7(128).padder()
    padded_message = padder.update(message) + padder.finalize()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()
    return base64.b64encode(iv + ciphertext).decode('utf-8')

ciphertext = encrypt_message(plaintext, aes_key)
print(f"Ciphertext: {ciphertext}")

# 4. Shamir Secret Sharing toepassen op de AES-sleutel
shares = SecretSharer.split_secret(
    aes_key.hex(), 2, 3  # Minimaal 2 van de 3 shares zijn nodig om de sleutel te reconstrueren
)

# 5. Output van de shares
print(f"Share 1: {shares[0]}")
print(f"Share 2: {shares[1]}")
print(f"Share 3: {shares[2]}")
