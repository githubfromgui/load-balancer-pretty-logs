from resources import resource_interface as interface

class LoadBalancerCloudWatchLogs(object):
    
    def __init__(self, log_classes: dict):
        for log_class in log_classes:
            if not isinstance(log_class, interface.InterfaceResource): raise Exception('Incorrect Interface for: ', log_class)
            
        for log_class in log_classes:
            if not log_class.is_resource_created():
                log_class.create_resource()