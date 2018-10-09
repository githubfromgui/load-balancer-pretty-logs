from abc import ABCMeta, abstractmethod
 
class AbstractTypes:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_dict(self, current_file_line) -> dict:
        pass