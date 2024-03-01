import logging

from enum import Enum
from pathlib import Path

logger = logging.getLogger(__name__)


class Network(Enum):
    NETWORK_LOCAL = 0
    NETWORK_MAINNET = 1
    NETWORK_TESTNET = 2
    NETWORK_STAGNET = 3

    @property
    def config(self) -> Path:
        if self.value == 0:
            return None
        return (
            Path(__file__).parent / f"{self.name.lower().split('_')[1]}.toml"
        )