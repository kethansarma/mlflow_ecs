import boto3


# client = boto3.client('ecr-public', region_name="us-east-1")
# response = client.describe_repositories(
#     registryId= '095690621767'
#
# )
client = boto3.client('ecs')
response = client.run_task(
    launchType='FARGATE',
    networkConfiguration={
        'awsvpcConfiguration': {
            'subnets': [
                'subnet-eb36ddc1',
                'subnet-2f1d9f65'
            ],
        'assignPublicIp': 'ENABLED'
        }
    },
    cluster='fargate-cluster',
    count=1,
    taskDefinition='fargate-pytask-definition'
)
# response = client.start_task(
#     cluster='fargate-cluster',
#     taskDefinition='fargate-pytask-definition:2',
#     containerInstances=['arn:aws:ecs:us-west-2:095690621767:cluster/fargate-cluster']
# )
print(response)