# -*- coding: utf-8 -*-#
# !/usr/bin/env python
"""base_app for EServices"""
import os
import sys
import wx

from elibs import join_path
from .enums import *
import models as database

__all__ = ['PersonType', 'get_icon', 'BASEDIR', 'log', 'BaseApp']

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# logging
import logging.config

logSQLFile = os.path.join(BASEDIR, 'sqllog.txt')
logConfigFile = os.path.join(BASEDIR, 'logging.conf')
if os.path.exists(logConfigFile):
    # load config from config file, see logging.conf for configuration settings
    logging.config.fileConfig(logConfigFile)
else:
    # or just do a basic config
    format = '%(name)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s'
    logging.basicConfig(format=format, level=logging.NOTSET)

log = logging.getLogger(__package__)

ICON = os.path.join(BASEDIR, 'share', 'images', 'logo_system.ico')


def _displayHook(obj):
    if obj is not None:
        print(repr(obj))


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
        
        # dbFile = os.path.abspath(os.path.join(pPath, 'devdata.sqlite'))
        dbFile = "postgres://postgres:Dw@6458995@localhost:5432/my_app"
        # define the db driver name here or get it from a configuration file
        dbDriver = "postgresql"
        dbUrl = database.sa.engine.url.URL(dbDriver, database=dbFile)
        log.debug("db: %s\n\n" % dbUrl)

        self.session = self.connectToDatabase(dbFile)

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
