import os
import random

from elibs import dict_to_prop

from core import BASEDIR


class License:
    def __init__(self):
        self.config_file = os.path.join(BASEDIR, 'eservices.key')
        self.key = None

    def load(self):
        if self.check():
            from core import decrypt
            import json

            try:
                with open(self.config_file, 'w', encoding='UTF8') as file:
                    rd = file.read()
                    dec_cfg = json.loads(decrypt(rd))
                    return dict_to_prop(dec_cfg)
            except Exception as e:
                from core import log
                log.error(e)

    def check(self):
        if os.path.exists(self.config_file):
            return True
        return False

    def save(self, config=dict):
        from core import encrypt
        import json
        enc_cfg = encrypt(json.dumps(config))
        try:
            with open(self.config_file, 'w', encoding='UTF8') as file:
                file.write(enc_cfg)
            return True
        except Exception as e:
            from core import log
            log.error(e)
            return False

    def verify(self):
        score = 0
        check_digit = self.key[0]
        check_digit_count = 0
        chunks = self.key.split('-')
        for chunk in chunks:
            if len(chunk) != 4:
                return False
            for char in chunk:
                if char == check_digit:
                    check_digit_count += 1
                score += ord(char)
        if score == 1772 and check_digit_count == 5:
            return True
        return False

    def generate(self):
        key = ''
        chunk = ''
        check_digit_count = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'
        while True:
            while len(key) < 25:
                char = random.choice(alphabet)
                key += char
                chunk += char
                if len(chunk) == 4:
                    key += '-'
                    chunk = ''
            self.key = key[:-1]
            if self.verify():
                return self.key.upper()
            else:
                key = ''

    def get(self, machine, cpf, password):
        """Constructs and sends a :class:`Request <Request>`.

            :param machine: machine name.
            :param cpf: CPF/CNPJ used for register.
            :param password:  Password used just for authentication.
        """
        import requests
        params = dict(
            machine=machine,
            serialKey=self.key,
            cpf=cpf,
            password=password
        )
        rs = requests.get(
            'https://ellitedev.herokuapp.com/api/v1/register',
            params=params
        )
        r = rs.json()
        if self.save(r):
            return True, r[0]['name']
        return False, 'Not Registered'
