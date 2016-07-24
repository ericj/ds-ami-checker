# Overview
This script is used to check each AMI id listed in DeepSecurity CloudFormation [template](https://github.com/deep-security/cloudformation/blob/master/DeepSecurity/Marketplace/DSM96MP.template) exists or not.
It can also validate CloudFormation template format.


# Pre-requisites
- Python [boto3](https://boto3.readthedocs.io/en/latest/) AWS SDK
```bash
pip install boto3 --user
```
- Have your AWS API credential in ~/.aws/credentials 
```
[default]
aws_access_key_id = AKIAIVRP2MQYMPXXXXXX
aws_secret_access_key = tj+ikes3Jm6OEbsDTv3F6eip2aJPh1RVjiwemrXXXX
```

# Usage
- Clone this repo
- Execute script to check, default will check DeepSecurity CloudFormation [template](https://github.com/deep-security/cloudformation/blob/master/DeepSecurity/Marketplace/DSM96MP.template), you can modify AMI_TEMPLATE to other URL or local file.
```bash
python ds-ami-checker.py
```

# TODO
- Let AMI_TEMPLATE parameter configurable
- Load other quick-start templates and find the exact AMI_TEMPLATE automatically
