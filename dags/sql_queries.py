from settings_dags import aws_access_key_id , aws_secret_access_key , aws_session_token
# DROP TABLES
# actualy cascade no need to use if drop sql queries order is correct
pets_table_drop = "DROP TABLE IF EXISTS pets;"
owners_table_drop = "DROP TABLE IF EXISTS owners CASCADE;"
phistory_table_drop = "DROP TABLE IF EXISTS phistory CASCADE;"
pdetail_table_drop = "DROP TABLE IF EXISTS pdetail CASCADE;"


# CREATE TABLES
owners_table_create = ("""CREATE TABLE IF NOT EXISTS owners( 
     OwnerID text primary key
    ,Name text
    ,Surname text
    ,StreetAddress text
    ,City text
    ,State text
    ,StateFull text
    ,ZipCode text      
);
""")

phistory_table_create = ("""CREATE TABLE IF NOT EXISTS phistory(
    PetID text
    ,Date text
    ,ProcedureType text
    ,ProcedureSubcode text
    
);
""")

pdetail_table_create = """CREATE TABLE IF NOT EXISTS pdetail 
 (
    ProcedureType text 
    ,ProcedureSubcode text
    ,Description text
    ,Price text 
    
);
"""

pets_table_create = """CREATE TABLE IF NOT EXISTS pets
 (
    PetID text primary key
    ,Kind text
    ,Gender text
    ,Age text
    ,OwnerID text  
);

 """




# INSERT RECORDS
# COPY s3 to Redshift
load_owners = """COPY %s FROM 's3://petclinic13/cleaned_zone_parquet/owners.csv'
	ACCESS_KEY_ID '%s'
	SECRET_ACCESS_KEY '%s'
	SESSION_TOKEN '%s'
	FORMAT AS csv
    IGNOREHEADER 1""" % ( 'owners', aws_access_key_id , aws_secret_access_key , aws_session_token)

load_phistory = """COPY %s FROM 's3://petclinic13/cleaned_zone_parquet/phistory.csv'
	ACCESS_KEY_ID '%s'
	SECRET_ACCESS_KEY '%s'
	SESSION_TOKEN '%s'
	FORMAT AS csv
    IGNOREHEADER 1""" % ( 'phistory', aws_access_key_id , aws_secret_access_key , aws_session_token)

load_pdetail = """COPY %s FROM 's3://petclinic13/cleaned_zone_parquet/pdetail.csv'
	ACCESS_KEY_ID '%s'
	SECRET_ACCESS_KEY '%s'
	SESSION_TOKEN '%s'
	FORMAT AS csv
    IGNOREHEADER 1""" % ( 'pdetail', aws_access_key_id , aws_secret_access_key , aws_session_token)

load_pets = """COPY %s FROM 's3://petclinic13/cleaned_zone_parquet/pets.csv'
	ACCESS_KEY_ID '%s'
	SECRET_ACCESS_KEY '%s'
	SESSION_TOKEN '%s'
	FORMAT AS csv
    IGNOREHEADER 1""" % ( 'pets', aws_access_key_id , aws_secret_access_key , aws_session_token)


# QUERY LISTS

create_table_queries = [     
    owners_table_create
    ,phistory_table_create
    ,pdetail_table_create
    ,pets_table_create
    ]
    # order in drop table should drop fact first all constrain will free and no need to use casecade
drop_table_queries = [
    pets_table_drop
    ,owners_table_drop
    ,phistory_table_drop 
    ,pdetail_table_drop    
    ]

loadinto_table_queries = [     
    load_owners
    ,load_phistory
    ,load_pdetail
    ,load_pets
    ]
