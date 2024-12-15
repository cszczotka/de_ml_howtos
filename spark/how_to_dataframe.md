### How to replace some value in data frame column

This is case where is payload column we want to replace some string 'undefined' by 'null'

```python
eventhub = eventhub.withColumn("payload", F.regexp_replace("payload", "undefined", "null")) 
```

### How to create single column dataframe

```python

df = spark.createDataFrame([1,2,3,-1], IntegerType()).toDF("col1")
df2 = = spark.createDataFrame(["a","b","c"], StringType()).toDF("col1")
```

### How to create few column dataframe

```python
from pyspark.sql.types import StructField, LongType, StringType, IntegerType, DateType, TimestampType, DoubleType, FloatType, StructType
from datetime import date
def load_scoring_dataset(p_mdl_name, p_spark):
    schema = StructType([       
        StructField('id', StringType(), True),
        StructField('eff_dt', DateType(), True)
    ])
    
    data = [(1000, date(2024,8,7)), 
            (1001, date(2024,8,7)), 
            (1002, date(2024,8,7))]
    
    df = p_spark.createDataFrame(data, schema).toDF('id', 'eff_dt')
    return df

def score_model(mdl_name, df, mdl_role_tp_value, spark):
    return
```

### Hpw to create dataframe using rdd

```python
# Creating DataFrames - Use RDD
from pyspark.sql.types import StructType, IntegerType, StringType

# Data as a list of tuples
data = [("James", 34), ("Anna", 20), ("Lee", 30)]

# Use RDD
rdd = spark.sparkContext.parallelize(data)
schema = StructType([
    StructField("Name", StringType(), True),
    StructField("Age", IntegerType(), True)
])
df = spark.createDataFrame(rdd, schema=schema)
df.show()
```