import os
import sagemaker
from sagemaker.tensorflow import TensorFlow

BUCKET_NAME_SOURCE = os.environ.get('SRC_BKT_NAME')
BUCKET_NAME_OUTPUT = os.environ.get('OUTPUT_BKT')
PREFIX = 'input/data/'

inputs = 's3://' + BUCKET_NAME_SOURCE + '/' + PREFIX

abalone_estimator = TensorFlow(entry_point='abalone.py',
                               role=os.environ.get('SM_ROLE'),
                               framework_version='2.1.0',
                               output_path='s3://' + BUCKET_NAME_OUTPUT,
                               training_steps= 100,                                  
                               evaluation_steps= 100,
                               hyperparameters={'learning_rate': 0.001},
                               train_instance_count=1,
                               train_instance_type='ml.c4.xlarge')

abalone_estimator.fit(inputs)