import sys

from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Data Catalog table
DataCatalogtable_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="data_lake_demo",
    table_name="bronze_tickit_ems_venue",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.getSink(
    path="s3://open-data-lake-demo-eu-central-1/tickit/silver/venue/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="S3bucket_node3",
)
S3bucket_node3.setCatalogInfo(
    catalogDatabase="data_lake_demo", catalogTableName="silver_tickit_ems_venue"
)
S3bucket_node3.setFormat("glueparquet")
S3bucket_node3.writeFrame(DataCatalogtable_node1)
job.commit()
