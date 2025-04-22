### How to read csv and convert columns to lowercase

```python
from functools import reduce

df = spark.read.option("header", "true").csv("/Volumes/priv/data_files/test.csv", inferSchema=True, sep=";")

df = reduce(lambda chain, column: chain.withColumnRenamed(*column),
            map(lambda field: (field.name, str.lower(field.name)),
                df.schema.fields),
            df)

df.display()
```