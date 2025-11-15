import dlt
from pyspark.sql.functions import col
# Create a streaming table

@dlt.table(
    name = 'sales_stg'
)

def sales_stg():
    df = spark.readStream.option("skipChangeCommits",True)\
        .table("databricksansh.silver.sales_enr")
    return df
"""
#CREATE MATERIALIZED VIEW IF NOT EXISTS demo_stream_table AS SELECT * FROM databricksansh.silver.sales_enr
@dlt.table(
    name = 'demo_mat_view'
)

def demo_mat_view():
    df = spark.read.table("databricksansh.silver.sales_enr")
    return df

#TEMPORARY TABLE (VIEW)
@dlt.view(
    name = 'demo_temp_view'
)
def demo_temp_view():
    df = spark.read.table("databricksansh.silver.sales_enr")
    return df

# TEMPORARY STREAM VIEW
@dlt.view(
    name = 'demo_temp_stream_view'
)
def demo_temp_stream_view():
    df = spark.readStream.table("databricksansh.silver.sales_enr")
    return df
"""

#create a mat view
@dlt.table(
    name = "sales_enr"
)
def sales_enr():
    df = spark.read.table("sales_stg")
    df.withColumn("priceAfterDiscount",col("total_amount")-col("discount"))
    return df

# create a mat view
@dlt.table(
    name = "sales_cur"
)
def sale_enr():
    df = spark.read.table("sales_enr")
    return df




