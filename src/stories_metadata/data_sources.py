import pyspark.sql.types as T


stories = {
    "partition_by": None,
    "schema": T.StructType([
        T.StructField("id", T.LongType()),
        T.StructField("last_modified_ts", T.TimestampType()),
        T.StructField("content", T.StringType()),
    ])
}


stories_metadata = {
    "partition_by": ("dt",),
    "schema": T.StructType([
        T.StructField("id", T.LongType()),
        T.StructField("language", T.StringType()),
        T.StructField("dt", T.DateType(), nullable=False)
    ])
}
