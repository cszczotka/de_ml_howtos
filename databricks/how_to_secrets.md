### Create secret scope

Open page - https://your-workspace/#secrets/createScope

```python
eventhub_connection_string = dbutils.secrets.get(f"xxx-{param_environment}-orch-kv-scope", f"{param_eventhub}-sas")

```

### How to read REDACTED value

invisible_sep = bytes.fromhex("E281A3").decode("utf-8")
secret = dbutils.secrets.get("scope", "secret")
plaintextSecret = secret.replace("", invisible_sep)
print(secret)  # would print "[REDACTED]"
print(plaintextSecret)  # would print "intg"



### How to add new secret 

databricks secrets put-secret sscope-kv-npa-dwb-dev-westeu-1 kafka-truststore-password -p xxx
