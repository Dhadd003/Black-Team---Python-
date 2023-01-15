import boto3

#CreateMultipleEc2s

ec2_resource=boto3.resource("ec2")
ec2_resource.create_instances(ImageId='ami-03657b56516ab7912',
      InstanceType='t2.micro',
    MaxCount=4,
      MinCount=3)
