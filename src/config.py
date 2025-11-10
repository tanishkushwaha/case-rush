from typing import Any
import tomli
import tomli_w

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

    @staticmethod
    def reset():
        default_config: dict[str, Any] = {
            "drop_rates": {
                "legendary": 0.2,
                "epic": 0.06,
                "rare": 0.12,
                "uncommon": 0.25,
                "common": 0.5,
            },
            "delays": {"case_opening": 5},
        }

        with open(CONFIG_FILE_PATH, "wb") as file:
            tomli_w.dump(default_config, file)
