__all__ = ["Serializable", "json_dump", "read_json"]

import json
from collections.abc import ItemsView


class Serializable:
    def __init__(self, **kwargs: dict) -> None:
        super().__init__(**kwargs)

    # when serialize and writing to a file tuples are perserved.
    def encode(self, obj: object) -> object:
        if isinstance(obj, tuple):
            return {"__tuple__": True, "obj": obj}
        elif isinstance(obj, list):
            return [self.encode(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: self.encode(value) for key, value in obj.items()}
        return obj

    # get all attribute that will be serialized.
    def get_serializable_items(self) -> ItemsView[str, object]:
        return {key: value for key, value in self.__dict__.items() if key[0] != "_"}.items()

    def serialize(self) -> dict:
        return {key: self.encode(value) for key, value in self.get_serializable_items()}


# dump object to json file
def json_dump(filename: str, data: dict | Serializable, **options: dict) -> dict:
    with open(filename, "w", encoding=options.get("encoding", "utf-8")) as file:
        data = {key: value.serialize() if isinstance(value, Serializable) else value for key, value in data.items()}
        json.dump(
            data.serialize() if isinstance(data, Serializable) else data,
            file,
            sort_keys=options.get("sort_keys", True),
            indent=options.get("indent", 2),
        )
    file.close()
    return data


# read json file
def read_json(filename: str, **options) -> dict:
    with open(filename, "r", encoding=options.get("encoding", "utf-8")) as file:
        data = json.load(file, object_hook=lambda obj: tuple(obj["obj"]) if "__tuple__" in obj else obj)
    file.close()
    return data
