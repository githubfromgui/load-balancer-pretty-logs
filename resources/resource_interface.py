from abc import ABCMeta, abstractmethod

# Interface
class InterfaceResource:
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_resource_created(self) -> bool: raise NotImplementedError("isResourceCreated method needs to be implemented!")
    
    @abstractmethod
    def create_resource(self) -> None: raise NotImplementedError("createResource method needs to be implemented!")
