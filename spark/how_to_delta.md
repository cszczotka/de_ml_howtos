#### Create external delta table from csv in S3 
```python
source = "s3://xxxdatalake/raw/cust_data_processed_parquet/*.parquet"
df = spark.read.parquet(source)

df.write.format("delta").mode("overwrite").option("path", 's3://xxxdatalake/bronze/default/cust_data').saveAsTable("bronze.default.cust_data") 

```