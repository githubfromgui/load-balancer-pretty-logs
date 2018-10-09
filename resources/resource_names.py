
class ResourceNames():
   def __init__(self, log_group_name: str, log_stream_name: str):
        self.log_group_name    = log_group_name
        self.log_stream_name   = log_stream_name
        
   def get_log_group_name(self) -> str:
       return self.log_group_name
       
   def get_log_stream_name(self) -> str:
       return self.log_stream_name
        
