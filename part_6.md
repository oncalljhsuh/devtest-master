# Part 6: Cloud computing

This sections tests some general cloud computing knowledge to do with AWS and cloud infra in general.
It is expected that you will need to find the answers to some of these questions via Google.

Please write your answers in this file.

### Question 6.1

Which AWS region is the closest to Melbourne?
Answer)Sydney. Availability Zones 3.

### Question 6.2

What is the name of a cheap AWS EC2 instance that offers _at least_ 12 CPU cores and 16GB of RAM?
Answer) a1.4xlarge
What are its specs (CPU cores, RAM) and cost per hour?
Answer) Linux, 16CPU 32Gib, USD 0.3357 per hour with 1 year reservation term OR USD 0.5328 per hour with monthly On-Demand Instance.

How much will it cost to run this instance for two weeks?
Answer) USD 0.3357 * 2 weeks * 7 days * 24 hours =  USD 112.8 with 1 year reservation term

### Question 6.3

Provide the AWS CLI command to copy all the contents of a S3 bucket to another S3 bucket on the same account.
The source bucket may contain nested files within "folders".

Source bucket: s3://mysource
Destination bucket: s3://mydest

```bash
# Your command here
aws s3 sync s3://mysource s3://mydest
```

### Question 6.4

Link to a section of library documentation showing how to stop an AWS EC2 instance using a Python client library (can be a howto, API reference, or tutorial).
Answer) https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.stop_instances

### Question 6.5

Describe, in 1-3 sentences

- What an AMI is and why it is useful for running EC2 instances
Answer) An Amazon Machine Image (AMI) is a special type of virtual appliance that provides the information required to launch an instance.
        This is useful because you can launch multiple instances from a single AMI when you need multiple instances with the same configuration.
- What IAM is and why it is useful when administering AWS
Answer) AWS Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely.
        This is useful because you can create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources using IAM.
- Where you would add your SSH public key onto an EC2 instance in order to log in as the "ubuntu" user
Answer) Create a user data script including username and ssh-authorized-keys, then pass this script to cloud-init.

### Question 6.6

Create a new SSH key and paste both the public and private key into this file.
Answer1-Public) ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCs1dQWUtobGsFehxCbr5t79Xm3pFsAVUe2flPzxKjtjRjXH4OEo5tUzoMvyzLqT/LssVm9HV40wrhwC1toXzT8iS0FS5c4zdPl4GIs/MVvD7faxfy2nGJ3ecz8cG58xwnAlBOn2VIvlhtBIWB3IIE4V4DLCFkW0BbepeVAgslP38YKDJNdmOs+vrcjroJSp+IlbwtFbHpYQ1A1SyK22E2lGtAnVwqZSLCyTVqWrjDxyHDpa4qMWG1H8stOK7nzv+ozys7t/vVrDisr8evTH6KgC/qk0SkSPqzR1PiODDNOfoQ9+4FF0mLLmGSG6wxWcijDxX9PWMESAr2AtuWnhhgr l446@DESKTOP-JFPIKRE
Answer2-Private)
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEArNXUFlLaGxrBXocQm6+be/V5t6RbAFVHtn5T88So7Y0Y1x+D
hKObVM6DL8sy6k/y7LFZvR1eNMK4cAtbaF80/IktBUuXOM3T5eBiLPzFbw+32sX8
tpxid3nM/HBufMcJwJQTp9lSL5YbQSFgdyCBOFeAywhZFtAW3qXlQILJT9/GCgyT
XZjrPr63I66CUqfiJW8LRWx6WENQNUsitthNpRrQJ1cKmUiwsk1alq4w8chw6WuK
jFhtR/LLTiu587/qM8rO7f71aw4rK/Hr0x+ioAv6pNEpEj6s0dT4jgwzTn6EPfuB
RdJiy5hkhusMVnIow8V/T1jBEgK9gLblp4YYKwIDAQABAoIBACS1xjZ3opvfMvNA
/OYUhpHtscyvvCR1+KVqb6p3Ouo57ezDZMvndDavJm4gWtAp6w8bHFRuyHOsaEBk
KSYiEr8Q498cDyKhlUBeSHwFtGnCjOqK4wJmdQOrez6jItSd8hRVX1dncW1qFJ/g
1vx2ivvMmi6Ft2aBDFp+IhNxtBCivaqWJce07nwetsVNLQmlMnUW8Q6A4dlLRojN
FEyisPBH7X0Pif125gdrG6mBsQzdrrfGjv2sdIIY4kL0hII865QJuLerWfjw0qD3
EBWNuJcGLh3poPccMq6X+MdQpdl5NDWuLscQwnwHrCAcBd7PFcDRpfEuJ37Joq6C
VzAiHQECgYEA1+w1YkdnmdqTEr0L97BqL+7Q6O+cWL4hqOWekr7bdB6+mzui+NYo
K4tg9gw2jXiuJyhSyCp1L9wvVBys0ME059/9flXn3yW7NlTjbd9YTaJe2MyKiFZv
tbtS//gW9tdpYAIidBTHmz4WFNmO7zhFkGw1vdB/xXs2x9EvUWrSCc8CgYEAzOpG
tPORbLzKx6MtrhznQenwaXG7O5p6hWWtNEcDXi2gg7BRqMTgTwpcJvUJGX63gBc3
PLa3WyrIF+6TXxGPdookLdjAQJB0Sdik1f8AKC1eLYooC9P9Ru0dyhtgGiVMNZ1+
7Zwonh9Fi4/I4JjJWRRV9TtjapQgrXGk5knGDuUCgYBQlmxmPdhA5/80YzJwQ3ue
YDfAeI2V4YCWlPzWMD2f3UmujleJIATmG6MYsf46VuxI2RfsdUw/jKJtdjZZw4KH
eGYYHN/pvR9ea9hmTZGbiBp2OAEMWZZf8YZM2r9XaZZ+qs1JHehR3J5JMdnTFuF/
waNdMNA/WHldoolSjdfOqQKBgHpPhDDSCYWMEsWiwstgeTDAwD1QI1/qTyN8kyvX
D02RknPINJW2HeVP271tGSdcmY8dTF0y+rKyEIkoYFKomqc4wWuUKvzevGqvo4QQ
FznkCojIJCsbN9yz/8n5GR3CEYEXJwIQ6bWoGMy64D4fNF+1YbFk52xgSjj80l6a
vlt5AoGAL4SYzfvYaRKdG7kwMsmuMf0RYTM5LTTwiJdF5NyGF/xIBPJcfw8eu6E/
5J4tuZ5f8vyxhly8aYiqwj4hvhMRQ9imki0G6ae0uPbGOrmz2kRCkElIbUDiArKr
QA+f/n2eNKtvZp1bURF202qnsrsKc3WyAtjiyr69eGL4i2ugs5o=
-----END RSA PRIVATE KEY-----

### Question 6.7

Write a bash one liner to create a new file called `foo.txt` which contains the text "Hello World!", followed by a newline

```bash
# Your command here
echo -e "Hello World!\n" > foo.txt
```

### Question 6.8

Write a bash one liner to create a new file which contains the text "Hello World!", followed by a newline, on a remote machine via SSH.

Remote machine hostname is `foo.com` and the user is `bar`. Assume you have all your SSH keys set up correctly on your machine and the target server.

```bash
# Your command here
ssh bar@foo.com 'echo -e "Hello World!\n" > foo.txt'
```

### Question 6.9

Buildkite it a self-hosted CI system. Referring to the documentation via Google, is it possible to run a scheduled build at 2pm every Tuesday? Please link to the URL of the documentation where you found your answer.
Answer) Yes, it is possible. https://buildkite.com/docs/pipelines/scheduled-builds

### Question 6.10

GitHub Actions is a CI system provided by GitHub, Referring to the documentation via Google, what is an environment variable that you could use to determine whether your bash script is running inside a Github Action?
Answer) job.status of job context

What kind of value would indicate that your script is running inside a GitHub Action?
Answer) success
