from vegapy.service.service_trading_data import TradingDataService
from tests.fixtures import tds, markets

import vegapy.protobuf.protos as protos


def test_get_latest_market_depth(tds: TradingDataService, markets):
    market_id_filter = markets[0]
    market_depth = tds.get_latest_market_depth(market_id=market_id_filter)
    assert market_depth.market_id == market_id_filter
