from vegapy.service.service_core import CoreService
from vegapy.service.service_trading_data import TradingDataService

from vegapy.service.utils.utils import Utils

from enum import Enum


class Service:
    def __init__(self, network: str, find_best: bool = True):
        # Compartmentalise APIs
        class API:
            def __init__(self, network: str):
                # TODO: Implement core service APIs
                self.__data = TradingDataService(network, find_best=find_best)
                self.__core = CoreService()

            @property
            def data(self):
                return self.__data

            @property
            def core(self):
                return self.__core

        self.api = API(network=network)

        # Compartmentalise utility methods
        self.utils = Utils(
            core_service=self.api.core, data_service=self.api.data
        )


if __name__ == "__main__":
    service = Service(network="mainnet")
