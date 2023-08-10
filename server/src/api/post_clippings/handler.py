def lambda_handler(event):
    print('The event from the lambda handler', event)

    return {
        'statusCode': 200,
        'body': 'Hello from Lambda'
    }
