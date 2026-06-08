# ⚖️ NalaGoodman's Encoder-Tools

```text
   ▄▄      ▄▄▄  ▄   ▄▄▄▄   ▄▄▄▄   ▄▄▄   ▄▄▄▄▄▄      ▄▄▄▄▄▄  ▄▄▄▄▄▄ 
   ██▄    ██▀   ▀██████▀  █▀ ██  ██    █▀██▀▀▀█▄  █▀ ██   █▀██▀▀▀█▄
   ███▄   ██      ██   ▄     ██ ██       ██▄▄▄█▀     ██     ██▄▄▄█▀
   ██ ▀█▄██      ██  ██     █████       ██▀▀█▄      ██     ██▀▀▀   
   ██   ▀██      ██  ██     ██ ██▄    ▄ ██  ██      ██    ▄ ██     
 ▀██▀    ██      ▀█████   ▀██▀  ▀██▄  ▀██▀  ▀██▀  ▄▄██▄▄ ▀██▀      
                  ▄   ██                                         
                  ▀████▀                                         
====================================================================
               ⚖️  Nala Goodman | Attorney at Code
====================================================================
```
> *"Did you know that you have rights? The Constitution says you do, and so do your encrypted strings! Don't let those CTF sheriffs lock your data away in Base64 or Hex without due process."* 
> — **Nala Goodman, Attorney at Code**

---

`N-decode` & `N-encode` adalah perangkat taktis CLI (*Command Line Interface*) ringan yang dirancang khusus untuk para praktisi *cybersecurity*, pemain CTF, dan *developer* yang butuh keadilan cepat di terminal. 

Jika terminal Anda tertangkap basah membawa *string* mencurigakan, Anda tidak butuh detektif—**Anda butuh Nala Goodman!**

---

## ⚡ FITUR UTAMA (Urusan Hukum yang Kami Selesaikan)

*   **N-decode (The Auto-Defender):** Sistem tebakan otomatis berteknologi tinggi. Masukkan teks acak apa saja, dan *tool* ini akan mendeteksi serta membebaskannya dari jeratan **Base64, Hexadecimal, URL Encode,** hingga **ROT13** secara instan. Tanpa eror, tanpa basa-basi.
*   **N-encode (The Cover-Up):** Butuh menyembunyikan barang bukti (*payload*) dengan cepat sebelum dikirim lewat jaringan? Amankan teks biasa Anda ke berbagai format enkoding dalam sekali pencet.

---

## 🛠️ CARA INSTALASI (Bebas Jaminan)

Karena Anda menggunakan Linux modern, pastikan Anda berada di dalam *Virtual Environment* Anda, lalu instal *tools* ini dalam mode pengembangan:

```bash
# Clone repositori ini
git clone [https://github.com/username_githubmu/encoder-tools.git](https://github.com/username_githubmu/encoder-tools.git)
cd encoder-tools

# Aktifkan venv Anda (Contoh untuk Fish Shell)
source .venv/bin/activate.fish

# Eksekusi instalasi
pip install -e .

#Cara pakai Decode
N-decode "NDM1NDQ2N2I2ODM0NjM2YjMzN2I3ZA=="

Outputnya : 
[+] Berhasil menebak 'NDM1NDQ2N2I2ODM0NjM2YjMzN2I3ZA==':
    ➔ Base64: 4354467b6834636b33727d
    ➔ Hex: CTF{h4ck3r}

#Cara Pakai Encode
N-encode "Halo Hakim"

Outputnya :
[+] Hasil Encode untuk 'Halo Hakim':
    ➔ Base64: SGFsbyBIYWtpbQ==
    ➔ Hex: 48616c6f2048616b696d
    ➔ URL Encode: Halo%20Hakim
    ➔ ROT13: Unyb Unxvz

#Installasi 

1. Untuk pengguna Linux biasa (lewat pipx agar aman dan global)
    " pipx install NGKRIP "

2. Atau jika di dalam Virtual Environment (venv)
    " pip install NGKRIP "

"Sebab jika Anda tidak punya auto-decoder yang bagus, Anda bisa terjebak di tantangan selamanya. Ingat: Better Call Nala!" 

