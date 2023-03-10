import logging
import boto3

# Example 1. get_object, put_object methods


def get_presigned_url(bucket_name, object_name, expiration=120):
    # if you have multiple profiles, you can specify one here, otherwise leave it as default
    aws_profile = 'default'
    region_name = 'us-west-1'  # preferred aws region
    client_method = 'get_object'  # 'put_object' etc.

    boto3.setup_default_session(profile_name=aws_profile)

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3', region_name=region_name,
                             config=boto3.session.Config(signature_version='s3v4',))
    try:
        presigned_url = s3_client.generate_presigned_url(client_method,
                                                         Params={'Bucket': bucket_name,
                                                                 'Key': object_name},
                                                         ExpiresIn=expiration)
    except Exception as e:
        print(e)
        logging.error(e)
        return "Error"

    print(presigned_url)
    return presigned_url


# This is how you call the function
file_path = 'uploads/path-to-file'
file_name = 'file-name'

bucket_name = 'mybucketname'
object_name = file_path + '/' + file_name
expiration = 120

# uncomment this line to test
get_presigned_url(bucket_name, object_name, expiration)

# SAMPLE OUTPUT: url
# https://mybucketname.s3.amazonaws.com/uploads/path-to-file/file-name?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AAAAAAAAAA123456%2F20230222%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Date=20230222T075718Z&X-Amz-Expires=120&X-Amz-SignedHeaders=host&X-Amz-Signature=02b60ec8eb2af625648dd10a4400d1ea01495a95ab403a186a200fe34ffe1a63

# Use the presigned URL to retrieve/upload a file to S3
