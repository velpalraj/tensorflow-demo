import os
import boto3

s3_resource = boto3.resource('s3')

BUCKET_NAME_SOURCE = os.environ.get('SRC_BKT_NAME')
BUCKET_NAME_OUTPUT = os.environ.get('OUTPUT_BKT')
PREFIX = 'input/data/'

s3_resource.Bucket(BUCKET_NAME_SOURCE).upload_file("data/abalone_train.csv", PREFIX + 'abalone_train.csv')
s3_resource.Bucket(BUCKET_NAME_SOURCE).upload_file("data/abalone_train.csv", PREFIX + 'abalone_predict.csv')
s3_resource.Bucket(BUCKET_NAME_SOURCE).upload_file("data/abalone_train.csv", PREFIX + 'abalone_test.csv')