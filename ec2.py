#!/usr/bin/python

import boto3

ec2 = boto3.resource('ec2')

client = boto3.client('ec2')

instances = client.describe_instances()

for instance in instances['Reservations'][0]['Instances']:
	print 'Instance ID: ' + instance['InstanceId']
	name = [ x['Value'] for x in instance['Tags'] if x['Key'] == 'Name']
	print 'Name: ' + name[0]