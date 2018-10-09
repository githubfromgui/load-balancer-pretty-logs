from resources  import resource_log_group as re_log_group
from resources  import resource_log_stream as re_log_stream
from resources  import resource_log_event as re_log_event
from resources  import resource_names as re_names
from contents   import contents_json as ct
from s3         import s3_class as s3

import boto3
import load_balancer_cloud_watch_logs as lb_cw_logs

def lambda_handler(event, context):
    try:
        # S3 Class
        s3_class = s3.S3Class(
            boto3.client('s3'),
            event['Records'][0]['s3']['bucket']['name'],
            event['Records'][0]['s3']['object']['key']
        )
        
        group_name = '/load-balancer-pretty-logs/'

        # Resource names
        names = re_names.ResourceNames(
            group_name,
            s3_class.get_bucket_name()
        )
        
        # Log Group
        log_group    = re_log_group.LogGroup(
            boto3.client('logs'),
            names
        )
        
        # Log Stream
        log_stream   = re_log_stream.LogStream(
            boto3.client('logs'),
            names    
        )
        
        # Log Event
        log_event    = re_log_event.LogEvent(
            boto3.client('logs'),
            names,
            ct.ContentJson(s3_class, 'application')
        )
         
        # Register the log formatted   
        lb_cw_logs.LoadBalancerCloudWatchLogs([
            log_group,
            log_stream,
            log_event
        ])

    except Exception as e:
        print("Error:", e)

    return
    