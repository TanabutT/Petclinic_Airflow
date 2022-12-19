from typing import List
import os
import glob
import json
from os import getenv
# from sql_queries import *
from _get_files import _get_files
from _con_upload_to_s3 import _con_upload_to_s3
# from _s3_transform_with_spark import _s3_transform_with_spark
from _create_Redshift import _create_Redshift
from _create_tables_process import _create_tables_process
from _read_bucket_landing_transform_to_cleaned import _read_bucket_landing_transform_to_cleaned
from _describe_cluster import _describe_cluster
from _insert_data import _insert_data
from _insert_data_parquet import _insert_data_parquet

from airflow import DAG
from airflow.utils import timezone
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.amazon.aws.sensors.redshift_cluster import RedshiftClusterSensor


# REDSHIFT_CLUSTER_IDENTIFIER = getenv("REDSHIFT_CLUSTER_IDENTIFIER", "redshift-cluster-1")

with DAG (
    "elt_parquet",
    start_date=timezone.datetime(2023, 12, 16),
    schedule="@daily", # use cron " * * * * *"
    tags=["workshop"],
    catchup=False,
) as dag:

    get_files = PythonOperator(
        task_id="get_files",
        python_callable=_get_files,
        op_kwargs={
            "filepath" : "/opt/airflow/dags/data",
        }
    )

    # create_Redshift = PythonOperator(
    #     task_id="create_Redshift",
    #     python_callable=_create_Redshift,
        
    # )
  
    con_upload_to_s3 = PythonOperator(
        task_id="con_upload_to_s3",
        python_callable=_con_upload_to_s3,
    )

    read_transform = PythonOperator(
        task_id="read_bucket_landing_transform_to_cleaned",
        python_callable=_read_bucket_landing_transform_to_cleaned,
    )

    # s3_transform_with_spark = PythonOperator(
    #     task_id="s3_transform_with_spark",
    #     python_callable=_s3_transform_with_spark,
    #     op_kwargs={
    #         "filepath" : "/opt/airflow/dags/data",
    #     }
    # )
    # ti = context["ti"]
    # # Get list of files from filepath
    # ClusterIdentifier = ti.xcom_pull(task_ids="create_Redshift", key="return_value")

    describe_cluster = PythonOperator(
        task_id="describe_cluster",
        python_callable=_describe_cluster,
    )

    wait_for_cluster = RedshiftClusterSensor(
        task_id='wait_for_cluster',
        cluster_identifier='redshift-cluster-petclinic',
        target_status='available',
        aws_conn_id='redshift_petclinic' # input connections at admin section in airflow ui and put here
    )

    create_tables_process = PythonOperator(
        task_id="create_tables_process",
        python_callable=_create_tables_process,
       
    )

    # insert_data = PythonOperator(
    #     task_id="insert_data",
    #     python_callable=_insert_data,
       
    # )

    insert_data_parquet = PythonOperator(
        task_id="insert_data_parquet",
        python_callable=_insert_data_parquet,
       
    )
      
    get_files >> con_upload_to_s3 >> read_transform >> wait_for_cluster >> describe_cluster >> create_tables_process >> insert_data_parquet
    # create_Redshift >> wait_for_cluster 