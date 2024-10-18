
from pqcrypto.kem.kyber512 import generate_keypair, encapsulate, decapsulate


publieke_sleutel, prive_sleutel = generate_keypair()

print("Publieke sleutel:", publieke_sleutel)
print("Privé sleutel:", prive_sleutel)

zin = "Dit is een geheime boodschap."


ciphertext, symmetrische_sleutel = encapsulate(publieke_sleutel)

print("Ciphertext:", ciphertext)
print("Symmetrische sleutel:", symmetrische_sleutel)

ontsleutelde_sleutel = decapsulate(ciphertext, prive_sleutel)

print("Ontsleutelde sleutel:", ontsleutelde_sleutel)

if symmetrische_sleutel == ontsleutelde_sleutel:
    print("De boodschap is succesvol ontsleuteld!")
else:
    print("Er is een fout opgetreden bij het ontsleutelen.")
