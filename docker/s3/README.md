---
title: Object Storage with AWS S3
---

This is an example project that uses boto3 + Python to read from an AWS S3 bucket. It shows how you can configure your project to access S3 and other AWS resources from [Jetify Cloud](https://cloud.jetify.com)

## Setting up S3

If you don't already have an S3 bucket configured, you will need an [AWS account](https://docs.aws.amazon.com/SetUp/latest/UserGuide/setup-overview.html) + IAM user with access to your S3 buckets. Once your account is setup, you can create an S3 Bucket using the following steps:

1. From the **Services** selector in your AWS Console, select **Storage**, then **S3**
2. On the S3 Dashboard, click **Create Bucket**, and give your bucket a name and default region
3. If your files do not need to be accessed by external, public users, leave the **Block all Public Access** button checked. Otherwise configure the permissions to match your needs
4. Once you've finished configuring the bucket, click **Create Bucket**
5. Copy the ARN and save it somewhere secure. 

Once the bucket is created, you'll also need to configure [Bucket Access Policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html) and an [IAM User Policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/walkthrough1.html) to allow your user to securely access the bucket. Consult the S3 documentation for more details on how to configure the correct policy for your needs.

## Connecting Jetify Cloud to your S3 Account

If you want your Jetify Cloud App to push and pull objects from your S3 Bucket, you can use Jetify Secrets to set your AWS Access Key ID and Secret in your environment:

* Go to the Jetify Dashboard for your project, and navigate to Secrets. Create the following Secrets in the `Prod` environment: 
  * `AWS_ACCESS_KEY_ID`: The access key for your AWS account
  * `AWS_SECRET_ACCESS_KEY`: The secret key for your AWS account
  * `AWS_BUCKET_NAME`: The name of the bucket that you will be accessing.

When you deploy your application, Devbox will automatically set these secrets as env variables in your environment. You can use these secrets with any AWS client library (such as boto3 for Python) or via the AWS CLI/SDK itself.

## Running the Project Locally

You can connect your project to Jetify Cloud by running `devbox auth login` to sign in via the browser, and then link the project to Jetify Secrets by running `devbox secrets init`. For more details, follow the [Jetify Secrets Guide](https://www.jetify.com/devbox/docs/cloud/secrets/secrets_cli/)

Once connected, you can start the service locally by running: 

```bash
devbox run pip-install
devbox run serve-gunicorn
```
