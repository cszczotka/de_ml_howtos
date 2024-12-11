Run on master db
```sql
CREATE LOGIN sqluser-dbw-dev-westeu-001-read  WITH PASSWORD = 'xxx'
```

Run on your db


```sql
CREATE USER [sqluser-dbw-dev-westeu-001-read]  FOR LOGIN [sqluser-dbw_dev-westeu-001-read]  WITH DEFAULT_SCHEMA = dbo;
```
