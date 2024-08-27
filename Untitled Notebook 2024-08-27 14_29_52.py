# Databricks notebook source
# Mount to ADLS - this mounting method is not suitable for production, Service Principle method must be used. The reason it can't be used is EntraID must be accessed to create a service principle, currently, EntraID is not available to this account.
account_key = dbutils.secrets.get('training-db-secret-scope', 'mount-sas-account-key')
account_token = dbutils.secrets.get('training-db-secret-scope', 'mount-sas-account-token')
dbutils.fs.mount(
  source = "wasbs://databricks-incremental@trainingsamp.blob.core.windows.net",
  mount_point = "/mnt/trainingsamp/databricks-incremental/",
  extra_configs = {account_key:account_token}
)

# dbutils.fs.unmount("/mnt/trainingsamp/databricks-incremental/")

