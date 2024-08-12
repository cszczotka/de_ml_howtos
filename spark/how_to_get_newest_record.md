### How to keep most recent record
```python
from datetime import date

rdd = sc.parallelize([
    [1, date(2016, 1, 7), 13.90],
    [1, date(2016, 1, 16), 14.50],
    [2, date(2016, 1, 9), 10.50],
    [2, date(2016, 1, 28), 5.50],
    [3, date(2016, 1, 5), 1.50]
])

df = rdd.toDF(['id','date','price'])
df.show()

 

df.createOrReplaceTempView("entries")  

output = sqlContext.sql('''
    SELECT 
        *
    FROM (
        SELECT 
            *,
            dense_rank() OVER (PARTITION BY id ORDER BY date DESC) AS rank
        FROM entries
    ) vo WHERE rank = 1
''');

output.show();

```

### Example of difference between row_number, dens_rank and rank

```sql
%sql
 SELECT a,
        b,
        row_number() OVER(PARTITION BY a ORDER BY b) as row_number,
        dense_rank() OVER(PARTITION BY a ORDER BY b) dense_rank,
        rank() OVER(PARTITION BY a ORDER BY b) as rank
    FROM VALUES ('A1', 2), ('A1', 1), ('A2', 3), ('A1', 1), ('A1', 1) tab(a, b)

```

