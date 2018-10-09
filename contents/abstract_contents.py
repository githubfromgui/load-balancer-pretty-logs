from abc import ABCMeta, abstractmethod
from lb_types import factory_load_balancer_type as factory_lb_type
 
class AbstractContentsClass:
    __metaclass__ = ABCMeta

    def __init__(self, s3_class, load_balancer_type):
        self.s3_class           = s3_class
        self.load_balancer_type = factory_lb_type.FactoryLoadBalancerType(load_balancer_type)
        super().__init__()
        
    @abstractmethod
    def get_content(self) -> dict:
        pass