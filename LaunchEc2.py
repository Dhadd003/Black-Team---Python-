import boto3

#LaunchEC2Instance

ec2_resource=boto3.resource("ec2")
ec2_resource.create_instances(ImageId='ami-07c8bc5c1ce9598c3',
      InstanceType='t2.micro',
    MaxCount=1,
      MinCount=1)
[ec2.Instance(id='i-0013315584b8da3f3')]
