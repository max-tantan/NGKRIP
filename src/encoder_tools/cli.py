import sys
from .autodecoder import auto_decode

# Kode \033[36m untuk warna Cyan, \033[0m untuk mereset warna kembali normal
GREEN_CYAN = "\033[36m"
RESET = "\033[0m"

BANNER = GREEN_CYAN + """
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
""" + RESET

def main(argv=None):
    # Izinkan pemakaian sebagai entry point package maupun pemanggilan langsung
    # dari kode lain yang ingin menyuntikkan argumen sendiri.
    argv = sys.argv[1:] if argv is None else argv
    print(BANNER)

    if not argv:
        print('Cara pakai: NG-decode "teks"')
        return 1

    teks = " ".join(argv)
    hasil = auto_decode(teks)

    if not hasil:
        print(f"[-] Gagal menebak format untuk '{teks}'.")
    else:
        print(f"[+] Berhasil menebak '{teks}':")
        for nama_format, teks_asli in hasil.items():
            print(f"    -> {nama_format}: {teks_asli}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
