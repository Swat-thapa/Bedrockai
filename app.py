import boto3
import json

prompt= input("Input your workflow query:")


bedrock=boto3.client(service_name="bedrock-runtime")


params = {
  "modelId": "anthropic.claude-3-haiku-20240307-v1:0",
  "contentType": "application/json",
  "accept": "application/json",
  "body": json.dumps({
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 1000,
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": prompt
          }
        ]
      }
    ]
  })
}

response = bedrock.invoke_model(**params)

body = json.loads(response['body'].read())

from pprint import pprint
pprint(body)