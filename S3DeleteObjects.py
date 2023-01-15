import boto3

s3_resource=boto3.client('s3')

#Delete Single Object

s3_resource.delete_object(Bucket='bucketname', Key='keyname')

#Delete Multiple Objects

import os
import glob

#Find All Objects from Bucket

s3_resource.list_objects(Bucket='bucketname')["Contents"]
len(objects)

#Iteration
for object in objects:
    print(object['Key'])
    s3_resource.delete_object(Bucket='bucketname', Key=object['Key'])
