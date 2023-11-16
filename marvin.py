import json
import boto3

def lambda_handler(event, context):
    # Extract the SNS message from the event
    sns_message = json.loads(event['Records'][0]['Sns']['Message'])

    # Get necessary information from the SNS message
    subject = sns_message.get('Subject', 'AWS Marketplace Event')
    message = sns_message.get('Message', 'No message provided.')
    recipients = ['email@example.com', 'another_email@example.com']  # Add your email addresses

    # Send emails to recipients using Amazon SNS
    sns_client = boto3.client('sns')

    for recipient in recipients:
        response = sns_client.publish(
            TopicArn='your_sns_topic_arn',  # Replace with your SNS topic ARN
            Message=message,
            Subject=subject,
            MessageAttributes={
                'email': {
                    'DataType': 'String',
                    'StringValue': recipient
                }
            }
        )

        print(f"Email sent to {recipient}. MessageId: {response['MessageId']}")

    # Return a response if needed
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function executed successfully!')
    }
