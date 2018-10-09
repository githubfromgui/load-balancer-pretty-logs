from contents import abstract_contents as abstract
import json
import time

class ContentJson(abstract.AbstractContentsClass):
    def get_content(self):
        contents    = self.s3_class.get_file_content()
        logEvents   = []

        for line in contents.splitlines():
            logEvents.append(
                {
                    'timestamp': int(round(time.time() * 1000)),
                    'message': json.dumps(
                        self
                        .load_balancer_type
                        .get()
                        .get_dict(line)    
                    )
                }
            );
        
        return logEvents
