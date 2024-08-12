Create secret scope
Open page - https://your-workspace/#secrets/createScope

```python
eventhub_connection_string = dbutils.secrets.get(f"xxx-{param_environment}-orch-kv-scope", f"{param_eventhub}-sas")

```