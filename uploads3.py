import boto3

#How to Upload Single File

s3_resource=boto3.client(s3)
s3_resource.upload_file(
    Filename='test.txt',
    Bucket='mybucket-boto3',
    Key='test.txt')

#How to Upload Multiple Files

import os
import glob

cwd=os.cwd()
cwd=cwd + '/upload/'
files=glob.glob(cwd + '*.png')
print(files)

#For File in Files

s3_resource=boto3.resource('s3')
s3_resource.upload_file(
Filename='test',
Bucket='mybucket-boto3',
Key='test')    
