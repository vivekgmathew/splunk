class MySQLIngestor:

    def __init__(self, spark, conf):
        self._spark = spark
        self._conf = conf

    def read(self):
        print("MySQl Read")


    def write(self):
        print("MySQL Write")