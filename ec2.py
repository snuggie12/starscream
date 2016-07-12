#!/usr/bin/python

import boto3
from flask import Flask

client = boto3.client('ec2')
app = Flask(__name__)

@app.route("/instances")
def list_instances():
	instance_array = []
	instances = client.describe_instances()

	for instance in instances['Reservations'][0]['Instances']:
		instance_string = 'Instance ID: ' + instance['InstanceId']
		name = [ x['Value'] for x in instance['Tags'] if x['Key'] == 'Name']
		name_string = 'Name: ' + name[0]
		instance_array += instance_string + name_string
	return instance_array
	
