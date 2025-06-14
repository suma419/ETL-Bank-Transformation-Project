import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')
    response = glue.start_job_run(JobName='bank-transform-job')
    return {
        'statusCode': 200,
        'body': 'Glue ETL job started',
        'runId': response['JobRunId']
    }
