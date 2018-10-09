from resources import resource_interface as interface

class LogGroup(interface.InterfaceResource):
    def __init__(self, cloud_watch_logs, resource_names):
        self.cloud_watch_logs  = cloud_watch_logs
        self.resource_names    = resource_names
        
    def is_resource_created(self) -> bool:
        response = self.cloud_watch_logs.describe_log_groups(
            logGroupNamePrefix=self.resource_names.get_log_group_name()
        )
        
        if response['logGroups']:
            return True
            
        return False
        
        
    def create_resource(self) -> None:
        self.cloud_watch_logs.create_log_group(
            logGroupName=self.resource_names.get_log_group_name()
        )
        
        return
        
