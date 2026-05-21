import sys

from .autoencoder import auto_encode

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
    argv = sys.argv[1:] if argv is None else argv
    print(BANNER)

    if not argv:
        print('Cara pakai: NG-encode "teks"')
        return 1

    teks = " ".join(argv)
    hasil = auto_encode(teks)

    if not hasil:
        print(f"[-] Gagal meng-encode '{teks}'.")
    else:
        print(f"[+] Berhasil meng-encode '{teks}':")
        for nama_format, teks_hasil in hasil.items():
            print(f"    -> {nama_format}: {teks_hasil}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
