from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64

def decrypt_message(ciphertext, key):
   
    ciphertext = base64.b64decode(ciphertext)

    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]


    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    padded_message = decryptor.update(actual_ciphertext) + decryptor.finalize()

   
    unpadder = padding.PKCS7(128).unpadder()
    message = unpadder.update(padded_message) + unpadder.finalize()

    return message


original_ciphertext = "zL3jxqf1UYmQw6nB31/Zg8m8JMD1a83pKGQrDh0JlTnqAsYPTA/ls9kF0Ta34Sek"  # gegenereerde ciphertext
recovered_key = bytes.fromhex("909c456491a747be156a8626877cabb9a9826a680a10a37f7f8e22fa2166164a")  # gereconstrueerde sleutel in

# Decrypted message
decrypted_message = decrypt_message(original_ciphertext, recovered_key)
print(f"Gedecrypteerde boodschap: {decrypted_message.decode('utf-8')}")
