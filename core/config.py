import os

from elibs import dict_to_prop

from core import BASEDIR, log
from core import enums


class Config:
    def __init__(self):
        self.config_file = os.path.join(BASEDIR, 'config.db')
        self.db_host = None
        self.db_port = None
        self.db_name = None
        self.db_user = None
        self.db_password = None
        self.db_driver = None
        self.db_file = None

    def __str__(self):
        if self.db_driver == enums.DBDriver.PostgreSQL:
            password = ':' + self.db_password if self.db_password is not None else ''
            port = ':' + self.db_port if self.db_port is not None else ''
            db_conn = f"postgres://{self.db_user}{password}@{self.db_host}{port}/{self.db_name}"
            return db_conn

    def load(self):
        from core import decrypt
        import json
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file) as file:
                    rd = file.read()
                    dec_cfg = json.loads(decrypt(rd))
                    cfg = dict_to_prop(dec_cfg)
                    self.db_host = cfg.host
                    self.db_port = cfg.port if cfg.port != '' else None
                    self.db_name = cfg.name
                    self.db_user = cfg.user
                    self.db_password = cfg.password if cfg.password != '' else None
                    if cfg.driver == 'PostgreSQL':
                        self.db_driver = enums.DBDriver.PostgreSQL
                    if cfg.driver == 'MySQL':
                        self.db_driver = enums.DBDriver.MySQL
                    if cfg.driver == 'SQLite':
                        self.db_driver = enums.DBDriver.SQLite
                    return True
            except Exception as e:
                log.error(e)
        return False

    def check(self):
        if os.path.exists(self.config_file):
            try:
                self.load()
                return True
            except Exception as e:
                os.remove(self.config_file)
                log.error(e)
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
