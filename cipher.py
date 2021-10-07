from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import os
import binascii


class FileCipher:

    MODE = AES.MODE_CBC
    IV = Random.new().read(AES.block_size)
    KEY = None

    filepath = None
    content = None
    password = None

    def __init__(self, filepath, password):
        self.filepath = filepath
        self.content = self.file_get_contents(filepath)
        self.password = password.encode('utf-8')
        self.KEY = SHA256.new(self.password).digest()

    def encrypt(self):
        aes = AES.new(self.KEY, self.MODE, IV=self.IV)
        data = self.IV + aes.encrypt(self.pad_string(self.content))
        data = binascii.hexlify(data).decode('utf-8')  # bytes to string
        self.write('encrypt', self.filepath, data)
        return data

    def decrypt(self):
        self.content = binascii.unhexlify(self.content.encode('utf-8'))  # string to bytes
        self.IV = self.content[:AES.block_size]
        aes = AES.new(self.KEY, self.MODE, IV=self.IV)
        data = aes.decrypt(self.content[AES.block_size:])
        data = self.unpad_string(data).decode("utf-8")
        self.write('decrypt', self.filepath, data)
        return data

    @staticmethod
    def write(action, file, data=None):
        filename = os.path.splitext(file)
        no_ext = filename[0].replace('-encrypted', '').replace('-decrypted', '')
        if action == 'encrypt':
            filepath = "{}-encrypted{}".format(no_ext, filename[1])
        else:
            filepath = "{}-decrypted{}".format(no_ext, filename[1])
        with open(filepath, 'w') as file:
            file.write(data)

    @staticmethod
    def pad_string(content, chunk_size=AES.block_size):
        pad = chunk_size - len(content) % chunk_size
        content += chr(pad) * pad
        return content

    @staticmethod
    def unpad_string(content):
        pad = content[-1]
        return content[:-pad]

    @staticmethod
    def file_get_contents(filename):
        with open(filename) as f:
            return f.read()