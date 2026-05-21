# Meng-import fungsi dari library buatanmu sendiri!
from encoder_tools.autodecoder import auto_decode

print("=== Uji Coba CTF Auto-Decoder ===")

# Tes 1: Base64 (Harusnya menghasilkan 'Hello CTF')
teks_b64 = "SGVsbG8gQ1RG"
print(f"\n[?] Mencoba decode: {teks_b64}")
print(f"Hasil: {auto_decode(teks_b64)}")

# Tes 2: Hexadecimal (Harusnya menghasilkan 'Nala')
teks_hex = "4e616c61"
print(f"\n[?] Mencoba decode: {teks_hex}")
print(f"Hasil: {auto_decode(teks_hex)}")

# Tes 3: ROT13 (Harusnya menghasilkan 'Halo Dunia')
teks_rot13 = "Unyb Qhavn"
print(f"\n[?] Mencoba decode: {teks_rot13}")
print(f"Hasil: {auto_decode(teks_rot13)}")