# -*- coding: utf-8 -*-#
# !/usr/bin/env python
"""base_app for EServices"""
import os
import sys
from logging.handlers import TimedRotatingFileHandler

import wx
from elibs import join_path, check_path

import models as database
from .enums import *

__all__ = ['PersonType', 'get_icon', 'BASEDIR', 'log', 'BaseApp']
APP_NAME = 'EServices'
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# logging
import logging.config

LOGPATH = os.path.join(BASEDIR, 'log')
check_path(LOGPATH)
log = logging.getLogger(__name__)
logSQLFile = os.path.join(BASEDIR, 'log', 'sqllog.txt')
logConfigFile = os.path.join(BASEDIR, 'share', 'logging.conf')
if os.path.exists(logConfigFile):
    # load config from config file, see logging.conf for configuration settings
    logging.config.fileConfig(logConfigFile)
else:
    # or just do a basic config
    LOGFILE = join_path(LOGPATH, f"{APP_NAME}.log")

    handler = TimedRotatingFileHandler(
        filename=LOGFILE, when='midnight', backupCount=30)
    log.addHandler(handler)

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)-5.5s [%(name)s] %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )
    handler.setFormatter(formatter)
    if os.environ.get('ASLOGLEVEL'):
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.DEBUG)
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    log.addHandler(console)
    # format = '%(name)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s'
    # logging.basicConfig(format=format, level=logging.NOTSET)

ICON = os.path.join(BASEDIR, 'share', 'images', 'logo_system.ico')


def _displayHook(obj):
    if obj is not None:
        print(repr(obj))


def get_db_url():
    # dbFile = os.path.abspath(os.path.join(pPath, 'devdata.sqlite'))
    dbFile = "postgres://postgres:Dw@6458995@localhost:5432/my_app"
    # define the db driver name here or get it from a configuration file
    dbDriver = "postgresql"
    dbUrl = database.sa.engine.url.URL(dbDriver, database=dbFile)
    dbUrl = 'postgres://postgres:@localhost/my_app'
    log.debug("db: %s\n\n" % dbUrl)
    return dbUrl


def get_icon():
    icon = wx.Icon()
    icon.CopyFromBitmap(wx.Bitmap(ICON, wx.BITMAP_TYPE_ANY))
    return icon


class BaseApp(wx.App):
    def __init__(self, *args):
        super(BaseApp, self).__init__(args)
        log.debug('start init')

        # work around for Python stealing "_"
        sys.displayhook = _displayHook

        self._dataNeedsSaving = False

        self.session = self.connectToDatabase(get_db_url())

        self.doAppConfig()
        log.debug('end init')

    # ----------------------------------------------------------------------
    def doAppConfig(self):
        """
        Get application configuration from file
        """
        appName = "EServices"
        # configuration folder

    # ----------------------------------------------------------------------
    def connectToDatabase(self, dburl):
        """
        Connect to our database and return a Session object

        :param dburl: a valid SQLAlchemy URL string
        """

        log.debug("connect db")
        engine = database.sa.create_engine(dburl, echo=False)
        database.init_model(engine)
        session = database.DBSession()
        self.setupDatabase(session, engine)
        return session

    # ----------------------------------------------------------------------
    def setupDatabase(self, session, engine):
        """Setup the db, note that this will not upgrade already existing tables"""
        log.debug("setup db")
        database.metadata.create_all(engine)
        log.debug("db created")
