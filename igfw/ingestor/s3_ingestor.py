from delta.tables import DeltaTable
from .base_ingestor import BaseIngestor


class S3Ingestor(BaseIngestor):

    def __init__(self, spark, conf):
        self._spark = spark
        self._conf = conf

    def read(self):
        df = self._spark.read.format(self._conf['format']).load(self._conf['s3_path'])
        return df

    def write(self, df):
        self._spark.write.format(self._conf['format']).mode("overwrite").save(self._conf['s3_path'])
        delta_table = DeltaTable.forPath(self._spark, self._conf['s3_path'])
        delta_table.generate("symlink_format_manifest")




