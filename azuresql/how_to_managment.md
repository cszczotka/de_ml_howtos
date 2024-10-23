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


### How to show uses and roles

```sql
SELECT
DP1.name AS DatabaseRoleName
,ISNULL(DP2.name, 'No members') AS DatabaseUserName
,DP2.principal_id
,DP2.create_date
FROM sys.database_role_members AS DRM
RIGHT OUTER JOIN sys.database_principals AS DP1 ON DRM.role_principal_id = DP1.principal_id
LEFT OUTER JOIN sys.database_principals AS DP2 ON DRM.member_principal_id = DP2.principal_id
WHERE DP1.type = 'R'
ORDER BY DP1.name, ISNULL(DP2.name, 'No members');
```