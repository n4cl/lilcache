import dataclasses

@dataclasses.dataclass
class BaseCache:
    expired: int = 0

    def get_data(self):
        pass

    def set_data(self, key):
        pass

    def clear_data(self, key):
        pass

    def clear_all(self):
        pass
