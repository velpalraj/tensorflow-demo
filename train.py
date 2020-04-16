import os
import sagemaker
import boto3
from sagemaker.tensorflow import TensorFlow

iam_client = boto3.client('iam')
s3_resource = boto3.resource('s3')

BUCKET_NAME_SOURCE = 'kevhuyn-source'
BUCKET_NAME_OUTPUT = 'kevhuyn-output'
PREFIX = 'input/data/'

role = iam_client.get_role(RoleName='AmazonSageMaker-ExecutionRole-20190802T115918')['Role']['Arn']

s3_resource.Bucket(BUCKET_NAME_SOURCE).upload_file("data/abalone_train.csv", PREFIX + 'abalone_train.csv')
s3_resource.Bucket(BUCKET_NAME_SOURCE).upload_file("data/abalone_train.csv", PREFIX + 'abalone_predict.csv')
s3_resource.Bucket(BUCKET_NAME_SOURCE).upload_file("data/abalone_train.csv", PREFIX + 'abalone_test.csv')

inputs = 's3://' + BUCKET_NAME_SOURCE + '/' + PREFIX

abalone_estimator = TensorFlow(entry_point='abalone.py',
                               role=role,
                               framework_version='2.1.0',
                               model_dir='s3://' + BUCKET_NAME_OUTPUT,
                               training_steps= 100,                                  
                               evaluation_steps= 100,
                               hyperparameters={'learning_rate': 0.001},
                               train_instance_count=1,
                               train_instance_type='ml.c4.xlarge')

abalone_estimator.fit(inputs)