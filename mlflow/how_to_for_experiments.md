### Get list of experiments


```python
from mlflow.tracking import MlflowClient

all_experiment_ids = []

client = MlflowClient()
all_experiments = client.search_experiments()   
for exp in all_experiments:
    print(f"{exp.experiment_id} {exp.name} {exp._artifact_location}")
    all_experiment_ids.append(exp.experiment_id) 
```

### Get model flow version
```python
```