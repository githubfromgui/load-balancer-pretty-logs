from lb_types import abstract_types as abstract

# SOURCE: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html
class ApplicationType(abstract.AbstractTypes):
    def get_dict(self, current_file_line) -> dict:
        line = current_file_line.decode("utf8").split(" ")
        
        return {
            "type"                        : line[0],
            "timestamp"                   : line[1],
            "elb"                         : line[2],
            
            # Breakdown IP and PORT
            "client_ip"                   : line[3].split(':')[0],
            "client_ip_port"              : line[3].split(':')[1],
            "target"                      : line[4].split(':')[0],
            "target_ip_port"              : line[4].split(':')[1],
            
            "request_processing_time"     : line[5],
            "target_processing_time"      : line[6],
            "response_processing_time"    : line[7],
            "elb_status_code"             : line[8],
            "target_status_code"          : line[9],
            "received_bytes"              : line[10],
            "sent_bytes"                  : line[11],
            
            # Contact all the request string
            "request"                     : line[12].replace('"', '') + " " + line[13] + " " + line[14].replace('"', ''),
            
            "user_agent"                  : line[15].replace('"', ''),
            "ssl_cipher"                  : line[16].replace('"', ''),
            "ssl_protocol"                : line[17],
            "target_group_arn"            : line[18],
            "trace_id"                    : line[19],
            "domain_name"                 : line[20].replace('"', ''),
            "chosen_cert_arn"             : line[21].replace('"', ''),
            "matched_rule_priority"       : line[22].replace('"', ''),
            "request_creation_time"       : line[23],
            "actions_executed"            : line[24],
            "redirect_url"                : line[25].replace('"', '')   
        }