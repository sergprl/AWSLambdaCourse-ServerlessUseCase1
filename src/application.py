import json
import boto3
client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('table01-09142026')

def lambda_handler(event, context):
    response = client.get_object(
        Bucket='bucket01-09142026',
        Key='DynamoDB_Samplefile.json',
    )
    
    file_data = response['Body'].read() # byte
    data_string = file_data.decode('utf-8') # string
    data_json = json.loads(data_string) # json
    print(data_json)
    print(type(data_json))

    # insert into dynamodb
    response = table.put_item(
        Item=data_json,
    )