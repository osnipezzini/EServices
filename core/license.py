import os

from elibs import dict_to_prop

from core import BASEDIR


class License:
    def __init__(self):
        self.license_file = os.path.join(BASEDIR, 'eservices.key')
        self.key = None
        self.company = None
        self.valid_date = None

    def load(self):
        if self.check():
            from core import decrypt
            import json

            try:
                file = open(self.license_file)
                rd = file.read()
                dec_cfg = decrypt(rd)
                return dict_to_prop(json.loads(dec_cfg))
            except Exception as e:
                print(e)
                from core import log
                log.error(e)

    def check(self):
        if os.path.exists(self.license_file):
            return True
        return False

    def save(self, config=dict):
        from core import encrypt
        import json
        enc_cfg = encrypt(json.dumps(config))
        print(config)
        try:
            with open(self.license_file, 'w', encoding='UTF8') as file:
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
        import wmi
        c = wmi.WMI()
        for s in c.Win32_Processor():
            key = s.ProcessorId

        chunk = ''
        serial = ''
        count = 0
        for char in key:
            serial += char
            chunk += char
            count += 1
            if len(chunk) == 4 and not (len(key) == count):
                serial += '-'
                chunk = ''

        self.key = serial.upper()
        return self.key

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
        rs = requests.post(
            'https://ellitedev.herokuapp.com/api/v1/register/',
            data=params
        )
        r = rs.json()
        if rs.status_code == 200:
            if self.save(r):
                return True, r['Company']
        return False, r['error']
