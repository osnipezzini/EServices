from enum import Enum

__all__ = ['PersonType']


class PersonType(Enum):
    CLIENT = 0,
    WORKER = 1,
    PROVIDER = 2,
    PUBLIC_ORGANIZATION = 3,


class ProductType(Enum):
    PRODUCT = 0,
    SERVICE = 1,
    FUEL = 2


class DBDriver(Enum):
    SQLite = 0,
    PostgreSQL = 1,
    MySQL = 2
