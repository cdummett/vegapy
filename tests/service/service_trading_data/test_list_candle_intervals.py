import pytest

from vegapy.service.service_trading_data import TradingDataService
from tests.fixtures import tds, markets

import vegapy.protobuf.protos as protos


@pytest.mark.trading_data_service
def test_list_candle_intervals(tds: TradingDataService, markets):
    market_id = markets[0]
    for interval_to_candle_id in tds.list_candle_intervals(
        market_id=market_id
    ):
        assert isinstance(
            interval_to_candle_id,
            protos.data_node.api.v2.trading_data.IntervalToCandleId,
        )
