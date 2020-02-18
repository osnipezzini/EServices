import os

from elibs import dict_to_prop

from core import BASEDIR


class Config:
    def __init__(self):
        self.config_file = os.path.join(BASEDIR, 'config.db')

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
        except Exception as e:
            from core import log
            log.error(e)
