from lb_types import application_type as app_type

class FactoryLoadBalancerType():
    def __init__(self, load_balancer_type):
        self.load_balancer_type = load_balancer_type
        
    def get(self):
        if self.load_balancer_type == 'application':
            return app_type.ApplicationType()
        # Return the type below
        # depending of your Load Balancer...