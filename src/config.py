from typing import Any
import tomli

CONFIG_FILE_PATH = "config.toml"


class Config:
    _data: dict[str, Any] | None = None

    @classmethod
    def _load(cls) -> Any:
        if cls._data is None:
            with open(CONFIG_FILE_PATH, "rb") as file:
                cls._data = tomli.load(file)

        return cls._data

    @classmethod
    def get_drop_rates(cls) -> dict[str, float]:
        conf = cls._load()

        return conf.get("drop_rates")

    @classmethod
    def get_delays(cls) -> dict[str, int]:
        conf = cls._load()

        return conf.get("delays")
