import json
import boto3
import datetime
import uuid

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

BUCKET_NAME = "aishu-log-bucket-12345"
TABLE_NAME = "LogsTable"
TOPIC_ARN = "arn:aws:sns:ap-south-1:956123261758:log-alerts"

table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    print("Received event:", event)

    body = json.loads(event.get("body", "{}"))
    message = body.get("message", "No message received")

    timestamp = str(datetime.datetime.utcnow())
    log_id = str(uuid.uuid4())

    log_data = {
        "logId": log_id,
        "timestamp": timestamp,
        "message": message
    }

    # Store in S3
    file_name = f"log-{timestamp}.json"
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=json.dumps(log_data)
    )

    # Store in DynamoDB
    table.put_item(Item=log_data)

    # 🚨 ALERT CONDITION
    if "error" in message.lower():
        try:
            sns.publish(
                TopicArn=TOPIC_ARN,
                Message=f"Error detected: {message}",
                Subject="Log Alert"
            )
            print("SNS alert sent")
        except Exception as e:
            print("SNS Error:", str(e))

    return {
        "statusCode": 200,
        "body": json.dumps({
            "status": "success",
            "message": message
        })
    }