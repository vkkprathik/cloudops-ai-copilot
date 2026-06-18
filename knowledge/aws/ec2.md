# Amazon EC2

Amazon Elastic Compute Cloud (EC2) provides virtual servers in AWS.

Common EC2 Troubleshooting:

## SSH Connection Failed

Check:

- Security Group port 22
- Public IP assigned
- Internet Gateway attached
- Route Table configured
- Network ACL allows SSH
- Correct PEM key used

AWS CLI:

aws ec2 describe-instances

aws ec2 describe-security-groups

## CPU High

Check:

top

htop

CloudWatch Metrics

Scale instance if required.
