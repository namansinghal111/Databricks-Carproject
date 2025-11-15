import dlt

#INGESTING SALSE DATA
@dlt.table(
  comment="sales_bronze"
)
def sales_bronze():
    df = spark.readStream.format("cloudFiles")\
                .option("cloudFiles.format","csv")\
                .load("/Volumes/databricksansh/bronze/bronze_volume/sales/")
    return df

import dlt

#INGESTING STORES DATA
@dlt.table(
  comment="stores_bronze"
)
def stores_bronze():
    df = spark.readStream.format("cloudFiles")\
                .option("cloudFiles.format","csv")\
                .load("/Volumes/databricksansh/bronze/bronze_volume/stores/")
    return df

#INGESTING PRODUCTS DATA
@dlt.table(
  comment="products_bronze"
)
def products_bronze():
    df = spark.readStream.format("cloudFiles")\
                .option("cloudFiles.format","csv")\
                .load("/Volumes/databricksansh/bronze/bronze_volume/products/")
    return df

#INGESTING CUSTOMERS DATA
@dlt.table(
  comment="customers_bronze"
)
def customers_bronze():
    df = spark.readStream.format("cloudFiles")\
                .option("cloudFiles.format","csv")\
                .load("/Volumes/databricksansh/bronze/bronze_volume/customers/")
    return df