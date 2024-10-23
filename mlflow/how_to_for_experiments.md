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

### Get runId artefacts

```python
from mlflow.store.artifact.runs_artifact_repo import RunsArtifactRepository
RunsArtifactRepository("runs:/44d40c3e551f498d9810631a588a5a46").list_artifacts('model')
```

### Get runId properties
```python
mlflow.get_run('44d40c3e551f498d9810631a588a5a46').to_dictionary()
```
