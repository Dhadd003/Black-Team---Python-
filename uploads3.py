import boto3

#upload single file

s3_resource=boto3.client(s3)
s3_resource.upload_file(
    Filename='test.txt',
    Bucket='mybucket-boto3',
    Key='test.txt')

#upload multiple files

import os
import glob

cwd = os.cwd()
cwd = cwd + '/upload/'
files = glob.glob(cwd + '*.png')
print(files)

#for file in files

s3_resource = boto3.resource('s3')
s3_resource.upload_file(
Filename='test',
Bucket='mybucket-boto3',
Key='test')    
