import logging
import boto3
from botocore.exceptions import ClientError
import json

# Example 1. get_object, put_object methods


def get_presigned_post(bucket_name, object_name, expiration=120):
    aws_profile = 'default'
    region_name = 'us-west-1'

    required_fields = {
        'Content-Type': 'image/*'  # Only allow images
    }
    required_conditions = [
        ['content-length-range', 0, 2097152],  # 2MB
        {'Content-Type': 'image/*'}  # Only allow images
    ]

    boto3.setup_default_session(profile_name=aws_profile)

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3', region_name=region_name,
                             config=boto3.session.Config(signature_version='s3v4',))
    try:
        presigned_url = s3_client.generate_presigned_post(
            Bucket=bucket_name,
            Key=object_name,
            Fields=required_fields,
            Conditions=required_conditions,
            ExpiresIn=expiration
        )
    except ClientError as e:
        print(e)
        logging.error(e)
        return "Error"

    # print(presigned_url)
    print(json.dumps(presigned_url, indent=4))
    return presigned_url


bucket_name = 'eazel-io'
file_name = 'user-image.png'
object_name = f"uploads/content/{file_name}"

get_presigned_post(bucket_name, object_name)

# SAMPLE OUTPUT
# {
#     "url": "https://bucketname.s3.amazonaws.com/",
#     "fields": {
#         "Content-Type": "image/*",
#         "key": "uploads/content/user-image.png",
#         "x-amz-algorithm": "AWS4-HMAC-SHA256",
#         "x-amz-credential": "AAAA1AAAAAAA11AAAA6/20230222/us-west-1/s3/aws4_request",
#         "x-amz-date": "20230222T073320Z",
#         "policy": "eyJleHBpcmF0aW9uIjogIjIwMjMtMDItMjJUMDc6MzU6MjBaIiwgImNvbmRpdGlvbnMiOiBbWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsIDAsIDIwOTcxNTJdLCB7IkNvbnRlbnQtVHlwZSI6ICJpbWFnZS8qIn0sIHsiYnVja2V0IjogImVhemVsLWlvIn0sIHsia2V5IjogInVwbG9hZHMvdXNlcl9nZW5lcmF0ZWRfY29udGVudC91c2VyLWltYWdlLnBuZyJ9LCB7IngtYW16LWFsZ29yaXRobSI6ICJBV1M0LUhNQUMtU0hBMjU2In0sIHsieC1hbXotY3JlZGVudGlhbCI6ICJBS0lBNUlSTVRYTFJDNzRBQU1FNi8yMDIzMDIyMi9hcC1ub3J0aGVhc3QtMi9zMy9hd3M0X3JlcXVlc3QifSwgeyJ4LWFtei1kYXRlIjogIjIwMjMwMjIyVDA3MzMyMFoifV19",
#         "x-amz-signature": "f486dcc93fe1a22707e4b27a0814d49adb366842597008980cb8895969ad304e"
#     }
# }

# Use the key-value pairs defined in the out to create form data fields
# Make POST request to the url in the output with the form data fields
