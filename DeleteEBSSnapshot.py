import boto3

#Delete EBS Volume Snapshot

ec2_client=boto3.client("ec2")
ec2_client.delete_snapshot(SnapshotId='snap-0937bebed9fe4564e')
