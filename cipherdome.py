from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import os, time
from pathlib import Path
import threading
import string
import random
import base64


# nonce 16
# pass 32

class CipherClass():
    def __init__(self):
        self._filesize = 0
        self._tokenlen = 1024 * 1024 * 10
        self._filetoken = 0
        self._is_active = False
        self._init_time = 0
        self._hilo = None
        self._mode = ""

    @property
    def is_active(self):
        return self._is_active

    @property
    def mode(self):
        return self._mode

    @property
    def porcent(self) -> float:
        if not self._is_active or self._filesize == 0:
            return 100
        per = 100 * self._filetoken / self._filesize
        return round(per, 2)

    @property
    def velocity(self) -> float:
        if not self._is_active or self._filesize == 0:
            return 0
        timepas = time.time() - self._init_time
        distpas = self._filesize - self._filetoken
        return round(distpas / timepas, 2)

    def _Ciphersys(self, pw, nonce=None, isencode=True):
        if not nonce:
            nonce = get_random_bytes(16)
        if isinstance(pw, str):
            pw = pw.encode()
        clave = PBKDF2(pw, nonce, dkLen=32, count=1000, hmac_hash_module=SHA256)
        cipher = AES.new(clave, AES.MODE_CTR, nonce=nonce[:8])
        return cipher, nonce

    def _GetKeyGCM(self, pw, salt=None):
        if salt is None:
            salt = b'\xf2)B\xdb\xb1 `\xae\x0fx'
        if isinstance(pw, str):
            pw = pw.encode()
        return PBKDF2(pw, salt, dkLen=32, count=100, hmac_hash_module=SHA256)

    def CipherFernet(self, pw, text):
        clave = self._GetKeyGCM(pw)
        cipher = AES.new(clave, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(text.encode())
        return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

    def DecipherFernet(self, pw, text):
        try:
            clave = self._GetKeyGCM(pw)
            datos = base64.b64decode(text)
            nonce = datos[:16]
            tag = datos[16:32]
            ciphertext = datos[32:]
            cipher = AES.new(clave, AES.MODE_GCM, nonce=nonce)
            return cipher.decrypt_and_verify(ciphertext, tag).decode()
        except Exception:
            return ""

    def CipherTxt(self, pw, txt, nonce=None):
        cpsys, nonce = self._Ciphersys(pw, nonce)
        if isinstance(txt, str):
            txt = txt.encode("utf-8")
        cp = cpsys.encrypt(txt)
        return nonce + cp

    def DecipherTxt(self, pw, ciphbin):
        nonce = ciphbin[:16]
        cpsys, _ = self._Ciphersys(pw, nonce, False)
        return cpsys.decrypt(ciphbin[16:])

    # ---------- Cifrado de archivos ----------
    def CipherFile(self, pw, filein, pathout):
        while True:
            flistnom = random.choices(string.ascii_letters, k=15)
            fname = ''.join(i for i in flistnom) + ".bin"
            fileout = os.path.join(pathout, fname)
            if not Path(fileout).is_file():
                break

        def ciphilo(pw):
            pwpass = b'\x9fd\x1c\x98\xfaG\xf57\xa4\xdc\xf82\xb7\xad\xa7\nq\xf1\xf2\xd8\x17\xc2\xc2\x81+\x00\xdb<\xa2\x85\xfc)'
            cpsys, nonce = self._Ciphersys(pw)
            if isinstance(pw, str):
                pw = pw.encode("utf-8")
            lpw = len(pw)
            for i in range(0, 32 - lpw):
                pw += chr((125 + lpw * i) % 128).encode("ascii")
            hashfile = self.CipherTxt(pwpass, pw, nonce)
            fn = os.path.basename(filein)
            flenname = len(fn)
            fname_enc = b""
            for i in range(0, flenname):
                fname_enc += chr((ord(fn[i]) + flenname + i) % 128).encode("utf-8")
            flenname_b = bytes([flenname])
            with open(fileout, "wb") as fo:
                fo.write(hashfile + nonce + flenname_b + fname_enc)
                with open(filein, "rb") as fi:
                    while True:
                        firead = fi.read(self._tokenlen)
                        if not firead:
                            break
                        cipchunk = cpsys.encrypt(firead)
                        fo.write(cipchunk)
                        self._filetoken += len(firead)
                self._filesize = 0
                self._filetoken = 0
                self._is_active = False
                self._init_time = 0
                self._hilo = None
                self._mode = ""

        f = Path(filein)
        if not (f.exists() and f.is_file()):
            return "error file no fount"
        self._filesize = os.path.getsize(filein)
        self._filetoken = 0
        self._is_active = True
        self._mode = "cipher"
        if self._filesize < 5 * self._tokenlen:
            ciphilo(pw)
        else:
            self._hilo = threading.Thread(target=ciphilo, args=(pw,), daemon=True)
            self._hilo.start()

        return fileout

    def DecipherFile(self, pw, filein, pathout):
        def decihilo():
            with open(filein, "rb") as fi:
                fi.read(48)
                nonce = fi.read(16)
                cpsys, _ = self._Ciphersys(pw, nonce, False)
                lfnom = int(fi.read(1)[0])
                nom = fi.read(lfnom).decode("utf-8")
                fname = ""
                for i in range(0, lfnom):
                    fname += chr((ord(nom[i]) - lfnom - i) % 128)
                fname = os.path.join(pathout, fname)
                with open(fname, "wb") as fo:
                    while True:
                        firead = fi.read(self._tokenlen)
                        if not firead:
                            break
                        cipchunk = cpsys.decrypt(firead)
                        fo.write(cipchunk)
                        self._filetoken += len(firead)
                    self._filesize = 0
                    self._filetoken = 0
                    self._is_active = False
                    self._init_time = 0
                    self._hilo = None
                    self._mode = ""

        if not self.CheckFile(pw, filein):
            return None
        self._filesize = os.path.getsize(filein)
        self._filetoken = 0
        self._is_active = True
        self._init_time = time.time()
        self._mode = "decipher"
        if self._filesize < 5 * self._tokenlen:
            decihilo()
        else:
            self._hilo = threading.Thread(target=decihilo, daemon=True)
            self._hilo.start()

    def CheckFile(self, pw, file):
        pwpass = b'\x9fd\x1c\x98\xfaG\xf57\xa4\xdc\xf82\xb7\xad\xa7\nq\xf1\xf2\xd8\x17\xc2\xc2\x81+\x00\xdb<\xa2\x85\xfc)'
        f = Path(file)
        if not (f.exists() and f.is_file()):
            return False
        if os.path.getsize(f) < 80:
            return False
        with open(f, "rb") as fi:
            nonce = fi.read(16)
            fhash = fi.read(32)
            if isinstance(pw, str):
                pw = pw.encode("utf-8")
            lpw = len(pw)
            for i in range(0, 32 - lpw):
                pw += chr((125 + lpw * i) % 128).encode("ascii")
            hash = self.CipherTxt(pwpass, pw, nonce)
        return hash == nonce + fhash

    def CheckPath(self, pw, path):
        res = []
        if path == "":
            path = os.path.dirname(__file__)
        for i in os.scandir(path):
            try:
                if i.is_file():
                    name = self.GetFileName(pw, i)
                    if name != "":
                        xdir = os.path.join('', i)
                        res.append((name, xdir))
            finally:
                pass
        return res

    def GetFileName(self, pw, file):
        if not self.CheckFile(pw, file):
            return ""
        with open(file, "rb") as f:
            f.read(64)
            lfnom = int(f.read(1)[0])
            nom = f.read(lfnom).decode("utf-8")
            fname = ""
            for i in range(0, lfnom):
                fname += chr((ord(nom[i]) - lfnom - i) % 128)
            return fname


cipher = CipherClass()


if __name__ == '__main__':
    cip = cipher.CipherTxt("pass", "Prueba de cifrado")
    plaintxt = cipher.DecipherTxt("pass", cip)
    print(plaintxt)

    # Prueba del sustituto de Fernet (AES-GCM)
    token = cipher.CipherFernet("pass", "Texto secreto")
    print(token)
    print(cipher.DecipherFernet("pass", token))