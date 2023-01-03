# Priority list for MLTemplate

This file is meant to serve as a way to prioritize the changes that we want to implement first into the mltemplate

## What is there to prioritize?

1. Utilities
  - PR after every file (Except mlflow_model and numpy_json_encoder.py)
  - Finish up documentation for each part before PR
  - humio.py
  - keyvault.py
  - mlflow_model.py
  - numpy_json_encoder.py
  - simple_config_loader.py
  - Add todo's for documentation (README.md, utilities.md?, In files)
2. Mlflow steps (Sidelines with Configuration at points)
  - Update utilities specific values
  - Add todo's for documentation (In files, README.md, Pipeline.md)
2. Configuration file (Steps structure in commented sections)
  - TODOS as values for filling in
  - Empty values with correct key names
  - sectioned the different parts of the configuration
  - Add todo's for documentation (configuration.md, In Files)
3. Mlflow Project file and Conda environment file
  - Add todo's for documentation (In files, README.md, Pipeline.md)
4. run.py
  - Add todo's for documentation
5. Finish all documentation

Later:
- Mlflow snippet tutorial Readme
- Tutorial for how to configure the template

## Guidelines to follow:

[Google MLOps](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning#mlops_level_1_ml_pipeline_automation)
Branching strategy: Branch made from main for each* file(*in most cases)
PR: Include definition of what the files are, changes made and notes