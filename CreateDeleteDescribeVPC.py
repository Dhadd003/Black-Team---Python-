import boto3

#CreateVPC

client=boto3.client("ec2")
client.create_VPC(CidrBlock="10.0.0.0/16")
    
#DeleteVPC

client=boto3.client("ec2")
client.delete_vpc(VpcId="VPCId")

#DescribeVPC

client=boto3.client('ec2')

#DescribeALL
x=client.describe_vpcs()
no_of_vpcs=x["Vpcs"]
len(no_of_vpcs)
for vpc in no_of_vpcs:
  print(vpc["VpcId"])

 #DescribeOneVPC 

x=client.describe_vpcs("VPCId")

