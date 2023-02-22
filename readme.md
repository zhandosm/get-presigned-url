<!-- @format -->

# AWS S3 Presigned URL Generator

This is a simple Python script that generates a presigned url for an object in S3.

## Prerequisites

- Python 3.6 or higher
- AWS credentials with access to S3

  - If you don't have AWS credentials, you can create a free account [here](https://aws.amazon.com/free/).
  - Configure AWS credentials with `aws configure` command. You can find more information [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html).

## Run the code

1. Create virtual environment: `python3 -m venv env`
2. Activate virtual environment: `source env/bin/activate`
3. Install requirements: `pip install -r requirements.txt`. Optionally, you can check the installed packages with `pip list`
4. Generate the presigned url: `python main.py`

## Note

- `get_presigned_url(get_presigned_url(bucket_name, object_name, expiration=120)`

  - `bucket_name`: Name of the bucket where the object is stored in S3. You should replace this with your bucket name.
  - `object_name`: Name of the object you want to access/upload/update/etc. You should replace this with your object name.
    - Note that `/` will create a folder in the bucket that you provide
    - For example: `object_name = "folder1/folder2/folder3/file.txt"` will create a folder structure like this: folder1 > folder2 > folder3 > file.txt
  - `expiration`: Expiration time of the presigned url in seconds. Default is 120 seconds.

## AWS Lambda

If you want to use this script in AWS Lambda, after configuring your Lambda function, you can follow the steps below:

1. Copy the `get_presigned_url()` function in `main.py` and paste it in the your Lambda function.
2. Specify the the details in the funciton according to your needs.
3. Use the `get_presigned_url()` function in your Lambda function however you want to generate the presigned url.
