import base64
import urllib.parse
import codecs

def auto_encode(text):
        """
        Menerima string biasa dan mengubahnya ke berbagai format.
        """
        text = str(text)
        results = {}

        # 1. Menjadi Base64
        try:
            encoded_b64 = base64.b64encode(text.encode('utf-8')).decode('utf-8')
            results['Base64'] = encoded_b64
        except Exception:
            pass

        # 2. Menjadi Hexadecimal
        try:
            encoded_hex = text.encode('utf-8').hex()
            results['Hex'] = encoded_hex
        except Exception:
            pass

        # 3. Menjadi URL Encode
        try:
            encoded_url = urllib.parse.quote(text)
            results['URL Encode'] = encoded_url
        except Exception:
            pass

        # 4. Menjadi ROT13
        try:
            encoded_rot13 = codecs.encode(text, 'rot_13')
            results['ROT13'] = encoded_rot13
        except Exception:
            pass

        return results