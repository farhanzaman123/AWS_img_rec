import json
import boto3

def lambda_handler(event, context):
    rekognition=boto3.client("rekognition")
    s3=boto3.client("s3")
    fileObj=s3.get_object(Bucket="img2bucketfarhan",Key="lion_2.jpg")
    response=rekognition.detect_labels(Image={"S3Object":{"Bucket":"img2bucketfarhan","Name":"lion_2.jpg"}})
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
