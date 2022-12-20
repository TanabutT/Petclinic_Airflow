import os

import pandas as pd
from settings_dags import aws_access_key_id , aws_secret_access_key , aws_session_token

def _read_bucket_landing_transform_to_cleaned(): 

    AWS_S3_BUCKET= "petclinic13/PetClinic_landing"
    AWS_S3_BUCKET_cleaned = "petclinic13/cleaned_zone_parquet"
    pets_key = "P9-Pets.csv"
    owners_key = "P9-Owners.csv"
    pdetail_key = "P9-ProceduresDetails.csv"
    phistory_key = "P9-ProceduresHistory1.csv"

    pets_df = pd.read_csv(
        f"s3://{AWS_S3_BUCKET}/{pets_key}",
        storage_options={
            "key": aws_access_key_id,
            "secret": aws_secret_access_key,
            "token": aws_session_token,
        },
        header=0,
    )

    owners_df = pd.read_csv(
        f"s3://{AWS_S3_BUCKET}/{owners_key}",
        storage_options={
            "key": aws_access_key_id,
            "secret": aws_secret_access_key,
            "token": aws_session_token,
        },
        header=0,
    )

    pdetail_df = pd.read_csv(
        f"s3://{AWS_S3_BUCKET}/{pdetail_key}",
        storage_options={
            "key": aws_access_key_id,
            "secret": aws_secret_access_key,
            "token": aws_session_token,
        },
        header=0,
    )

    phistory_df = pd.read_csv(
        f"s3://{AWS_S3_BUCKET}/{phistory_key}",
        storage_options={
            "key": aws_access_key_id,
            "secret": aws_secret_access_key,
            "token": aws_session_token,
        },
        header=0,
    )
    # print(pets_df.drop(columns=["Name"]))

    # clean and transform to parquet
    pets_key_pq = "pets.csv"
    owners_key_pq = "owners.csv"
    pdetail_key_pq = "pdetails.csv"
    phistory_key_pq = "phistory.csv"

    pets_df.drop(columns=["Name"]).to_csv(f"s3://{AWS_S3_BUCKET_cleaned}/{pets_key_pq}",
        storage_options={
            "key": aws_access_key_id,
            "secret": aws_secret_access_key,
            "token": aws_session_token,
        },index=False)
    owners_df.to_csv(f"s3://{AWS_S3_BUCKET_cleaned}/{owners_key_pq}",
        storage_options={
            "key": aws_access_key_id,
            "secret": aws_secret_access_key,
            "token": aws_session_token,
        },index=False)
    pdetail_df.to_csv(f"s3://{AWS_S3_BUCKET_cleaned}/{pdetail_key_pq}",
        storage_options={
            "key": aws_access_key_id,
            "secret": aws_secret_access_key,
            "token": aws_session_token,
        },index=False)
    
    # datetime issue fixed before write back into s3 bucker cleaned zone
    phistory_df['Date'] = phistory_df['Date'].astype('datetime64[ns]')

    phistory_df.to_csv(f"s3://{AWS_S3_BUCKET_cleaned}/{phistory_key_pq}",
        storage_options={
            "key": aws_access_key_id,
            "secret": aws_secret_access_key,
            "token": aws_session_token,
        },index=False)


#     #list file in bucket after upload
#     response = s3.list_objects(  Bucket='petclinic13',   
#                             MaxKeys=4)  
#                             # Prefix='P9')
#     print(response)

def main():
    _read_bucket_landing_transform_to_cleaned_parquet()
    

if __name__ == "__main__":
    main()