## How to create volume


```sql
%sql
CREATE EXTERNAL LOCATION `el_libs` URL 'abfss://libs@xxx.dfs.core.windows.net' WITH (STORAGE CREDENTIAL `sandbox-external-storage`)


CREATE EXTERNAL VOLUME sandbox.target.libs LOCATION 'abfss://libs@xxx.dfs.core.windows.net/python' COMMENT 'Volume for Python libraries'
```