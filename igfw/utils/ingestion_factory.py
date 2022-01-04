from ..utils.ingestion_type import IngestionType
from ..ingestor.s3_ingestor import S3Ingestor
from ..ingestor.postgre_ingestor import PostgreIngestor
from ..ingestor.sybase_ingestor import SybaseIngestor
from ..ingestor.mysql_ingestor import MySQLIngestor
from ..ingestor.oracle_ingestor import OracleIngestor


class IngestionFactory:

    @staticmethod
    def get_ingestion_object(spark, conf, ingestion_type):
        if ingestion_type == IngestionType.S3:
            return S3Ingestor(spark, conf)
        elif ingestion_type == IngestionType.MYSQL:
            return MySQLIngestor(spark, conf)
        elif ingestion_type == IngestionType.ORACLE:
            return OracleIngestor(spark, conf)
        elif ingestion_type == IngestionType.POSTGRES:
            return PostgreIngestor(spark, conf)
        elif ingestion_type == IngestionType.SYBASE:
            return SybaseIngestor(spark, conf)
        else:
            return S3Ingestor(spark, conf)
