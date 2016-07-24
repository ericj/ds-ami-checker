import urllib2
import json
import boto3

AMI_TEMPLATE = "https://raw.githubusercontent.com/deep-security/cloudformation/master/DeepSecurity/Marketplace/DSM96MP.template"

try:
    if 'http' not in AMI_TEMPLATE:
        print "load file: " + AMI_TEMPLATE
        with open(AMI_TEMPLATE) as fp:
            data = json.load(fp)
            fp.close()
    else:
        print "load url: " + AMI_TEMPLATE
        data = urllib2.urlopen(AMI_TEMPLATE)
        data = json.load(data)
except Exception as e:
    print "parse json file failed."
    print(vars(e))
    exit()

dsm_ami = data['Mappings']['DSMAMI']

for region in dsm_ami:
    ami_list = []
    for ami_type, ami_id in dsm_ami[region].items():
        ami_list.append(ami_id)

    ec2 = boto3.client('ec2', region_name=region)
    try:
        ec2.describe_images(ImageIds=ami_list)
        print 'checking ' + region + ' ' + ' '.join(ami_list) + ' Ok'
    except Exception as e:
        print region + ': ' + e.message
