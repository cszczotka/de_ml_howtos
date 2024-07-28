Get params from notebook ( without widgets)

```python

params = dbutils.notebook.entry_point.getCurrentBindings()
workspace = 'dbw-npa-dev-westeu-001' if params['workspace'] == None else params['workspace']
backup_location = '/Volumes/sandbox/target/backup' if params['backup_location'] == None else params['backup_location']

```