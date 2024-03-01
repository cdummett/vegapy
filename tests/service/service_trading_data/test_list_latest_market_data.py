import pytest

from vegapy.service.service_trading_data import TradingDataService
from tests.fixtures import tds

import vegapy.protobuf.protos as protos


@pytest.mark.trading_data_service
def test_get_latest_market_data(tds: TradingDataService):
    markets_data = tds.list_latest_market_data()
