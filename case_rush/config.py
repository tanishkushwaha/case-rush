"""
Provides a Config class for loading and accessing values from config.toml.
"""

from typing import Any, Literal
import tomli
import tomli_w

from case_rush.paths import CONFIG_DIR

CONFIG_FILE_PATH = CONFIG_DIR / "config.toml"
DEFAULT_CONFIG: dict[str, Any] = {
    "drop_rates": {
        "legendary": 0.02,
        "epic": 0.06,
        "rare": 0.12,
        "uncommon": 0.3,
        "common": 0.5,
    },
    "delays": {"case_opening": 5, "claim_cooldown": 3600},
}


class Config:
    _data: dict[str, Any] | None = None

    @classmethod
    def _load(cls) -> Any:
        if cls._data is None:
            # Add a try catch here
            try:
                with open(CONFIG_FILE_PATH, "rb") as file:
                    cls._data = tomli.load(file)
            except FileNotFoundError:
                cls.reset()
                with open(CONFIG_FILE_PATH, "rb") as file:
                    cls._data = tomli.load(file)

        return cls._data

    @classmethod
    def get_drop_rates(cls) -> dict[str, float]:
        conf = cls._load()

        return conf.get("drop_rates")

    @classmethod
    def get_delays(cls) -> dict[Literal["case_opening", "claim_cooldown"], int]:
        conf = cls._load()

        return conf.get("delays")

    @staticmethod
    def reset():
        with open(CONFIG_FILE_PATH, "wb") as file:
            tomli_w.dump(DEFAULT_CONFIG, file)
