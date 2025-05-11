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
### Zip artefacts

```python

import mlflow
import os
import zipfile

run_id = "50a2ccb6679f4ff2975d37955fc4c9b3"
artifact_path = "main_model" 

local_path = mlflow.artifacts.download_artifacts(run_id=run_id, artifact_path=artifact_path, dst_path="models/main_model")

print(local_path)

output_zip_file = "main_model_artifact.zip"
folder_to_zip = "models/main_model"   

with zipfile.ZipFile(output_zip_file, 'w') as zipf:
    for root, dirs, files in os.walk(folder_to_zip):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, folder_to_zip)
            zipf.write(file_path, arcname)

```