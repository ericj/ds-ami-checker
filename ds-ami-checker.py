import urllib2
import json
import boto3

AMI_TEMPLATE = "https://raw.githubusercontent.com/deep-security/cloudformation/master/DeepSecurity/Marketplace/DSM96MP.template"
code = 0

try:
    if 'http' not in AMI_TEMPLATE:
        print "Load file: " + AMI_TEMPLATE
        with open(AMI_TEMPLATE) as fp:
            data = json.load(fp)
            fp.close()
    else:
        print "Load url: " + AMI_TEMPLATE
        data = urllib2.urlopen(AMI_TEMPLATE)
        data = json.load(data)
except Exception as e:
    print "Parse json file failed."
    print(vars(e))
    exit(1)

dsm_ami = data['Mappings']['DSMAMI']

for region in dsm_ami:
    ami_list = []
    ami_dict = dict()
    for ami_type, ami_id in dsm_ami[region].items():
        ami_list.append(ami_id)
        ami_dict = dsm_ami[region]

    ec2 = boto3.client('ec2', region_name=region)
    try:
        ec2.describe_images(ImageIds=ami_list)
        for ami_type in ami_dict:
            print('Checking {0:>15} {1:>7}:{2} ok'.format(region, ami_type, ami_dict[ami_type]))
    except Exception as e:
        print "Checking %s %s" %(region, e.message)
        code = 1

if code == 0:
    print "Result: success, no error found."
else:
    print "Result: error detected."

exit(code)
