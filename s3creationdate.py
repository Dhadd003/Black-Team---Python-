import boto3

#S3 Creation Date 

s3_resource=boto3.client('s3')
s3_resource.list_buckets()
bucket_name=s3_resource.list_buckets()['Buckets'][0]['Name']
creation_date=s3_resource.list_buckets()['Buckets'][0]['CreationDate']
for bucket in s3_resource.list_buckets()['Buckets']:
    print(bucket)


