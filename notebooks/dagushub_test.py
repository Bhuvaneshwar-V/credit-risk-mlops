import mlflow
import dagshub

mlflow.set_tracking_uri("https://dagshub.com/Bhuvaneshwar-V/credit-risk-mlops.mlflow")

dagshub.init(repo_owner='Bhuvaneshwar-V', repo_name='credit-risk-mlops', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)