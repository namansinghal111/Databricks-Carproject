import dlt
from pyspark.sql.functions import *

# GOLD STREAMING - VIEW on TOP OF SILVER VIW
@dlt.view(
    name = 'customers_gold_view'
)
def customers_gold_view():
    df = spark.readStream.table("customers_silver_view")
    return df

# CREATING FACT TABLE (WITH AUTO CDC)
dlt.create_streaming_table(name="dim_customers")

dlt.create_auto_cdc_flow(
    target = 'dim_customers',
    source = 'customers_gold_view',
    keys = ['customer_id'],
    sequence_by=col('processDate'),
    stored_as_scd_type = 2,
    except_column_list = ['processDate']
)



