FROM apache/airflow:2.4.1

RUN pip install s3fs boto3 pandas
# use  $ docker build . --tag extending_airflow 