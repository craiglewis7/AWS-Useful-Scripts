#!/usr/bin/env python

import os
import boto
import sys

#MUST!!!
#Amend the variables below to match your AWS Credentials
REGION=''
ACCESS=''
SECRET=''

def ec2delete(imageid=None):
    conn = boto.ec2.connect_to_region('$REGION', aws_access_key_id='$ACCESS', aws_secret_access_key='$SECRET') 
    conn.deregister_image(imageid, delete_snapshot=True)

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()

    options, args = parser.parse_args()
    sys.stderr.write("Deleting %s and snapshots\n" %  str(args))
    ec2delete(args)
