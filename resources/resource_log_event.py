from resources import resource_interface as interface
from contents import abstract_contents as abstract
import time

class LogEvent(interface.InterfaceResource):
    def __init__(self, cloud_watch_logs, resource_names, content_class):
        if not isinstance(content_class, abstract.AbstractContentsClass): raise Exception('Incorrect AbstractClass for ContentClass in LogEvent!')

        self.cloud_watch_logs  = cloud_watch_logs
        self.resource_names    = resource_names
        self.content_class     = content_class

    def is_resource_created(self) -> bool:
        return False

    def create_resource(self) -> None:
        previous_log = self.cloud_watch_logs.describe_log_streams(
            logGroupName=self.resource_names.get_log_group_name(),
            logStreamNamePrefix=self.resource_names.get_log_stream_name()
        )
        
        if 'uploadSequenceToken' in previous_log['logStreams'][0]:
            self.cloud_watch_logs.put_log_events(
                logGroupName=self.resource_names.get_log_group_name(),
                logStreamName=self.resource_names.get_log_stream_name(),
                logEvents=self.content_class.get_content(),
                sequenceToken=previous_log['logStreams'][0]['uploadSequenceToken']
            )
        # If it is the FIRST TIME, we do not need the Sequence Token
        else:
            self.cloud_watch_logs.put_log_events(
                logGroupName=self.resource_names.get_log_group_name(),
                logStreamName=self.resource_names.get_log_stream_name(),
                logEvents=self.content_class.get_content()
            )

        return
    