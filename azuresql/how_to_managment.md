Select db users
```sql
select name as username,
       create_date,
       modify_date,
       type_desc as type,
       authentication_type_desc as authentication_type
from sys.database_principals
where type not in ('A', 'G', 'R', 'X')
      and sid is not null
order by username;
```


Register Manage Identity ( for example which repesent ADF ) as external user:

```sql
CREATE USER [adf-mi] FROM EXTERNAL PROVIDER;
 
EXEC sys.sp_addrolemember   
    @rolename = N'db_datareader',  
    @membername = [adf-mi]
 
EXEC sys.sp_addrolemember   
    @rolename = N'db_datawriter',  
    @membername = [adf-mi]  
 
 
-- If your managed service needs owner permissions 
EXEC sys.sp_addrolemember   
    @rolename = N'db_owner',  
    @membername = [adf-mi]
```