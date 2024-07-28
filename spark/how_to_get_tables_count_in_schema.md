```python
source_catalog = 'xxx'
source_schema = 'yyy'

###
databases = [f'{source_catalog}.{source_schema}']
tables = [
    f"{row['tableName']}"
    for db_rows in [
        spark.sql(f'show tables in {db}').collect() for db in databases
    ] 
    for row in db_rows
]
print(tables)

###


for  table in tables:
    count = spark.sql(f'select count(*) from {source_catalog}.{source_schema}.{table}').collect().__getitem__(0)
    print(f'{table} - {count}')

    

```