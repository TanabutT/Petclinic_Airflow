from settings_dags import aws_access_key_id , aws_secret_access_key , aws_session_token
# INSERT RECORDS
# COPY s3 to Redshift
load_owners = """COPY %s FROM 's3://petclinic13/previous_parquet/owners.parquet'
	ACCESS_KEY_ID '%s'
	SECRET_ACCESS_KEY '%s'
	SESSION_TOKEN '%s'
	FORMAT AS parquet""" % ( 'owners', aws_access_key_id , aws_secret_access_key , aws_session_token)

load_phistory = """COPY %s FROM 's3://petclinic13/previous_parquet/phistory.parquet'
	ACCESS_KEY_ID '%s'
	SECRET_ACCESS_KEY '%s'
	SESSION_TOKEN '%s'
	FORMAT AS parquet""" % ( 'phistory', aws_access_key_id , aws_secret_access_key , aws_session_token)

load_pdetail = """COPY %s FROM 's3://petclinic13/previous_parquet/pdetail.parquet'
	ACCESS_KEY_ID '%s'
	SECRET_ACCESS_KEY '%s'
	SESSION_TOKEN '%s'
	FORMAT AS parquet""" % ( 'pdetail', aws_access_key_id , aws_secret_access_key , aws_session_token)

load_pets = """COPY %s FROM 's3://petclinic13/previous_parquet/pets.parquet'
	ACCESS_KEY_ID '%s'
	SECRET_ACCESS_KEY '%s'
	SESSION_TOKEN '%s'
	FORMAT AS parquet""" % ( 'pets', aws_access_key_id , aws_secret_access_key , aws_session_token)

loadinto_table_queries = [     
    load_owners
    ,load_phistory
    ,load_pdetail
    ,load_pets
    ]
