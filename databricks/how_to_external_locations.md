
Show external locations

```sql
%sql
SHOW EXTERNAL LOCATIONS;
```

```sql
%sql
DESCRIBE EXTERNAL LOCATION ext_snow01_dev;
```

```sql
%sql
SHOW GRANTS `AZ_CDPM_Solution-Architects` ON EXTERNAL LOCATION ext_snow01_dev;
```

```sql
%sql
 GRANT READ FILES, WRITE FILES, CREATE EXTERNAL TABLE ON EXTERNAL LOCATION `ext_snow01_dev` TO `AZ_CDPM_Solution-Architects
 ```
