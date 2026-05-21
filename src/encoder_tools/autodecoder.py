import base64
import urllib.parse
import codecs

def auto_decode(text):
    text = str(text).strip()
    results = {}

    # Coba Base64
    try:
        padded_text = text + '=' * (-len(text) % 4)
        decoded_b64 = base64.b64decode(padded_text).decode('utf-8')
        if decoded_b64 and decoded_b64.isprintable():
            results['Base64'] = decoded_b64
    except Exception:
        pass

    # Coba Hexadecimal
    try:
        decoded_hex = bytes.fromhex(text).decode('utf-8')
        if decoded_hex.isprintable():
            results['Hex'] = decoded_hex
    except Exception:
        pass

    # Coba URL Encode
    try:
        decoded_url = urllib.parse.unquote(text)
        if decoded_url != text and decoded_url.isprintable():
            results['URL Encode'] = decoded_url
    except Exception:
        pass

    # Coba ROT13
    try:
        decoded_rot13 = codecs.decode(text, 'rot_13')
        if decoded_rot13.isprintable():
            results['ROT13'] = decoded_rot13
    except Exception:
        pass

    return results