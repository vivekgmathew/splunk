from enum import Enum


class IngestionType(Enum):
    S3 = 1
    ORACLE = 2
    MYSQL = 3
    POSTGRES = 4
    SYBASE = 5

