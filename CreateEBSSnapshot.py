import boto3

#Create AWS EBS Volume from snapshot:

ec2_client=boto3.client("ec2")
ec2_client.create_volume(AvailabilityZone='us-east-2c',
      Encrypted=True,
      Size=12,
      SnapshotId='snap-0937bebed9fe4564e',
      VolumeType='gp2')
