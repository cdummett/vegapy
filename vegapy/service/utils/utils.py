from vegapy.service.utils.market import MarketUtils

# from vegapy.service.utils.asset import AssetUtils


class Utils:
    def __init__(self, core_service, data_service):
        self.__market = MarketUtils(core_service, data_service)
        # self.__asset = AssetUtils(core_service, data_service)

    @property
    def market(self):
        return self.__market

    @property
    def market(self):
        return self.__market
