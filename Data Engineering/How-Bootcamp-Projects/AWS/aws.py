#%%
import boto3
from botocore import exceptions
import logging
from botocore.exceptions import ClientError
from dotenv import load_dotenv
from os import access, getenv

# %%
load_dotenv('/home/serpa/Documents/AWS/.env')

# %%
getenv('AWS_ID')
getenv('AWS_KEY')
# %%

s3_client = boto3.client(
    's3',
    aws_access_key_id=getenv('AWS_ID'),
    aws_secret_access_key=getenv('AWS_KEY')
)
# %%

def CriarBucket(nome=str):
    try:
        s3_client.create_bucket(Bucket=nome)
    except ClientError as e:
        logging.error(e)
        return False
    return True

#%%
#quando criamos um bucket não pode ter um outro igual no mundo
CriarBucket('bucket-s4lv3-s3')
        
        

# %%
