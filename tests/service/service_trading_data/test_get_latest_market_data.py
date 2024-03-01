import pytest

from vegapy.service.service_trading_data import TradingDataService
from tests.fixtures import tds, markets

import vegapy.protobuf.protos as protos


@pytest.mark.trading_data_service
def test_get_latest_market_data(tds: TradingDataService, markets):
    market_id_filter = markets[0]
    market_data = tds.get_latest_market_data(market_id=market_id_filter)
    assert market_data.market == market_id_filter
