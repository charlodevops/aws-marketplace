##Here's an example of a Lambda function in Python that checks for new AWS Marketplace subscriptions:


import boto3
import json

def lambda_handler(event, context):
    # Initialize the AWS SDK client for AWS Marketplace
    marketplace_client = boto3.client('marketplacecommerceanalytics')

    # Query AWS Marketplace for new subscriptions
    response = marketplace_client.generate_data_set(
        DataSetType='customer_subscriber_data',
        DataSetPublicationDate='TODAY',
        RoleName='<YourRoleName>'  # Replace with the name of your IAM role
    )

    # Check if a new subscription is available
    if 'DataSetRequestId' in response:
        # A new subscription is initiated, send an alert
        sns_client = boto3.client('sns')
        topic_arn = '<YourSNSTopicARN>'  # Replace with your SNS topic ARN

        message = {
            'Subject': 'New AWS Marketplace Subscription Alert',
            'Message': 'A new AWS Marketplace subscription has been initiated.'
        }

        sns_client.publish(
            TopicArn=topic_arn,
            Message=json.dumps(message)
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function executed successfully!')
    }




import json
import boto3

def lambda_handler(event, context):
    sns = boto3.client('sns')
    topic_arn = 'arn:aws:sns:us-west-2:289670889007:AWS-Marketplace-Subscriptions'
    
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



