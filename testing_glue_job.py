import sys

from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions

from pyspark.context import SparkContext

# Ingestion Framework Imports
from igfw import IngestionType
from igfw import IngestionFactory
from igfw import Configuration

# Get the arguments config file path and execution environment from command line arguments
args = getResolvedOptions(sys.argv, ['conf', 'env'])

# Get the spark session
spark = GlueContext(SparkContext.getOrCreate()).sparkSession

# Load the configuration information from YAML file
conf = Configuration(args['conf'], args['env'])

# Create Respective ingestion objects by dependency injecting
# spark session and configuration objects
mysql_ingestor = IngestionFactory\
    .get_ingestion_object(spark,
                          conf,
                          IngestionType.MYSQL)


s3_ingestor = IngestionFactory\
    .get_ingestion_object(spark,
                          conf,
                          IngestionType.S3)

# Read data from MySQL
df = mysql_ingestor.read()

# Write data to s3
s3_ingestor.write(df)



