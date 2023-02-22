<!-- @format -->

# AWS S3 Presigned URL Generator

This is a simple Python script that generates a presigned url for an object in S3.

## Prerequisites

- Python 3.6 or higher
- AWS credentials with access to S3

  - If you don't have AWS credentials, you can create a free account [here](https://aws.amazon.com/free/).
  - Configure AWS credentials with `aws configure` command. You can find more information [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html).

## Disclaimer

Before you use this, make sure to understand the difference between

- GET, PUT request to the generated presigned url to S3. This will retrieve/upload the object to S3 from the presigned url straight without any additional steps.
- POST request with form data to the presigned url to S3. This will upload the object to S3, but you'll have to do additional steps by forming a proper form data and sending it to the presigned url.

## Usage GET/PUT request to the generated presigned url to S3:

1. Create virtual environment: `python3 -m venv env`
2. Activate virtual environment: `source env/bin/activate`
3. Install requirements: `pip install -r requirements.txt`. Optionally, you can check the installed packages with `pip list`
4. Generate the presigned url: `python get_presigned_url.py`
5. Use the presigned URL to retrieve/upload a file to S3. GET/PUT request methods.

### Output

Outputs a presigned url. Example:
`https://mybucketname.s3.amazonaws.com/uploads/path-to-file/file-name?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AAAAAAAAAA123456%2F20230222%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Date=20230222T075718Z&X-Amz-Expires=120&X-Amz-SignedHeaders=host&X-Amz-Signature=02b60ec8eb2af625648dd10a4400d1ea01495a95ab403a186a200fe34ffe1a63`

## Usage POST request to the generated presigned url to S3:

1. Create virtual environment: `python3 -m venv env`
2. Activate virtual environment: `source env/bin/activate`
3. Install requirements: `pip install -r requirements.txt`. Optionally, you can check the installed packages with `pip list`
4. Generate the presigned url: `python get_presigned_post.py`
5. Use the key-value pairs defined in the output to create form data fields
6. Make POST request to the `url` in the output with the form data fields

### Output

Outputs a JSON data with url and fields.

- `url`: Presigned url endpoint
- `fields`: Form data fields that you need to send to the presigned url endpoint.
  Example:
  ````
  {
    "url": "https://bucketname.s3.amazonaws.com/",
    "fields": {
        "Content-Type": "image/*", // only images
        "key": "uploads/content/user-image.png",
        "x-amz-algorithm": "AWS4-HMAC-SHA256",
        "x-amz-credential": "AAAA1AAAAAAA11AAAA6/20230222/us-west-1/s3/aws4_request",
        "x-amz-date": "20230222T073320Z",
        "policy": "eyJleHBpcmF0aW9uIjogIjIwMjMtMDItMjJUMDc6MzU6MjBaIiwgImNvbmRpdGlvbnMiOiBbWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsIDAsIDIwOTcxNTJdLCB7IkNvbnRlbnQtVHlwZSI6ICJpbWFnZS8qIn0sIHsiYnVja2V0IjogImVhemVsLWlvIn0sIHsia2V5IjogInVwbG9hZHMvdXNlcl9nZW5lcmF0ZWRfY29udGVudC91c2VyLWltYWdlLnBuZyJ9LCB7IngtYW16LWFsZ29yaXRobSI6ICJBV1M0LUhNQUMtU0hBMjU2In0sIHsieC1hbXotY3JlZGVudGlhbCI6ICJBS0lBNUlSTVRYTFJDNzRBQU1FNi8yMDIzMDIyMi9hcC1ub3J0aGVhc3QtMi9zMy9hd3M0X3JlcXVlc3QifSwgeyJ4LWFtei1kYXRlIjogIjIwMjMwMjIyVDA3MzMyMFoifV19",
        "x-amz-signature": "f486dcc93fe1a22707e4b27a0814d49adb366842597008980cb8895969ad304e"
    }
  }
  ````

## Explanation

- `get_presigned_url.py` ->`get_presigned_url(get_presigned_url(bucket_name, object_name, expiration=120)`

  - `bucket_name`: Name of the bucket where the object is stored in S3. You should replace this with your bucket name.
  - `object_name`: Name of the object you want to access/upload/update/etc. You should replace this with your object name.
    - Note that `/` will create a folder in the bucket that you provide
    - For example: `object_name = "folder1/folder2/folder3/file.txt"` will create a folder structure like this: folder1 > folder2 > folder3 > file.txt
  - `expiration`: Expiration time of the presigned url in seconds. Default is 120 seconds.

- `get_presigned_post.py` -> `get_presigned_post(get_presigned_url(bucket_name, object_name, expiration=120)`

  - `bucket_name`: Name of the bucket where the object is stored in S3. You should replace this with your bucket name.
  - `object_name`: Name of the object you want to access/upload/update/etc. You should replace this with your object name.
    - Note that `/` will create a folder in the bucket that you provide
    - For example: `object_name = "folder1/folder2/folder3/file.txt"` will create a folder structure like this: folder1 > folder2 > folder3 > file.txt
  - `expiration`: Expiration time of the presigned url in seconds. Default is 120 seconds.

## AWS Lambda

If you want to use this script in AWS Lambda, after configuring your Lambda function, depending on your needs copy `the get_presigned_url()` or `get_presigned_post()` into your lambda function.
