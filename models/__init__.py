# -*- coding: utf-8 -*-#
# !/usr/bin/env python
"""SQLAlchemy models for the application

In a smaller application you could have all models in this file, but we 
assumed this will grow and have there split things up, in which case you 
should import you sub model at the bottom of this module.
"""

import sys

from sqlalchemy import Column, BigInteger, Sequence

if not hasattr(sys, 'frozen'):
    # needed when having multiple versions of SA installed
    try:
        # only do this if pkg_resources are installed
        import pkg_resources

        pkg_resources.require("sqlalchemy>=0.6")  # get latest version
    except ImportError:
        pass

import sqlalchemy as sa
import sqlalchemy.orm as sao
import sqlalchemy.sql as sasql
import sqlalchemy.ext.declarative as sad
from sqlalchemy.ext.hybrid import hybrid_property

maker = sao.sessionmaker(autoflush=True, autocommit=False)
DBSession = sao.scoped_session(maker)


class ReprBase(object):
    """Extend the base class

    Provides a nicer representation when a class instance is printed.

    Found on the SA wiki, not included with TG

    """
    grid = Column(BigInteger, Sequence('grid_seq'), primary_key=True)

    def __repr__(self):
        return "%s(%s)" % (
            (self.__class__.__name__),
            ', '.join(["%s=%r" % (key, getattr(self, key))
                       for key in sorted(self.__dict__.keys())
                       if not key.startswith('_')]))


Base = sad.declarative_base(cls=ReprBase)
metadata = Base.metadata


def init_model(engine):
    """Call me before using any of the tables or classes in the model."""
    DBSession.configure(bind=engine)


# you could have your models defined within this module, for larger applications
# it is probably nicer to work with to have them in separate modules and
# import them as shown below.
#
# remember to define __ALL__ in each module

# Import your model modules here.
from .person import *
from .products import *
