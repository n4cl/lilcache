import dataclasses
from datetime import datetime

@dataclasses.dataclass
class Content:
    body: object = dataclasses.field(default_factory=object)
    generate_time: datetime = dataclasses.field(default_factory=datetime)


@dataclasses.dataclass
class BaseCache:
    expired: int = 0
    data: dict = dataclasses.field(default_factory=dict)

    def get_data(self):
        pass

    def set_data(self, key: str, content: object) -> None:
        self.data[key] = Content(body=content, generate_time=datetime.now())

    def clear_data(self, key):
        del self.data[key]

    def clear_all(self):
        self.data = {}
