import dlt

#CREATE AN EMPTY STREAMING TABLE
@dlt.create_streaming_table(
    name = 'databricksansh.dlt_schema.append_table'
)


#CREATING FLOW 1
@dlt.append_flow(
    target='databricksansh.dlt_schema.append_table'
)
def flow_1():
    df = spark.read.format("cloudFiles")\
                    .option("cloudFIles.formant","csv")\
                    .load("/Volumes/databricksansh/bronze/autovl/flow1/")
    return df


#CREATING FLOW 2
@dlt.append_flow(
    target='databricksansh.dlt_schema.append_table'
)
def flow_2():
    df = spark.read.format("cloudFiles")\
                    .option("cloudFIles.formant","csv")\
                    .load("/Volumes/databricksansh/bronze/autovl/flow2/")
    return df
