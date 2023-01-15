import boto3

#How to list Objects in S3 Bucket

s3_resource=boto3.client('s3')

objects=s3_resource.list_objects(Bucket='bucketname')['Contents']


if len(objects)>0:
    print('object exists')
    
for object in objects:
    print(object['Key'])
