from resources import resource_interface as interface

class LogStream(interface.InterfaceResource):
    def __init__(self, cloud_watch_logs, resource_names):
        self.cloud_watch_logs  = cloud_watch_logs
        self.resource_names    = resource_names

    def is_resource_created(self) -> bool:
        response = self.cloud_watch_logs.describe_log_streams(
            logGroupName=self.resource_names.get_log_group_name(),
            logStreamNamePrefix=self.resource_names.get_log_stream_name()
        )
        
        if response['logStreams']:
            return True

        return False

    def create_resource(self) -> None:
        self.cloud_watch_logs.create_log_stream(
            logGroupName=self.resource_names.get_log_group_name(),
            logStreamName=self.resource_names.get_log_stream_name()
        )
        
        return
    