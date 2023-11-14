import json
import boto3

def lambda_handler(event, context):
    sns = boto3.client('sns')
    topic_arn = 'YOUR_SNS_TOPIC_ARN'
    
    # Extract relevant information from the CloudWatch Event
    message = json.loads(event['Records'][0]['Sns']['Message'])
    
    # Customize the alert message
    alert_message = f"New AWS Marketplace subscription initiated: {message['eventName']}"

    # Publish the alert to the SNS topic
    sns.publish(TopicArn=topic_arn, Message=alert_message)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Alert sent successfully!')
    }
