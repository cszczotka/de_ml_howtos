Number of collumns for statistic collection -  delta.dataSkippingNumIndexedCols

```sql
CREATE TABLE transactions (
  id BIGINT,
  country STRING,
  month DATE,
  transactionTime TIMESTAMP,
  senderId INT,
  recipientId INT,
  amount DECIMAL,
  note STRING
)
CLUSTER BY (country, month)

```

```python
```

Get current date and format to string
```python
from datetime import datetime
backup_date = datetime.now().strftime("%d-%m-%Y")
```