import pytest

from vegapy.service.service_trading_data import TradingDataService
from tests.fixtures import tds, markets, start_timestamp, end_timestamp

import vegapy.protobuf.protos as protos
import datetime


@pytest.mark.trading_data_service
def test_get_market_data_history_by_id_market_id(
    tds: TradingDataService, markets
):
    market_id = markets[0]
    for market_data in tds.get_market_data_history_by_id(
        market_id=market_id, max_pages=1
    ):
        assert market_data.market == market_id


@pytest.mark.trading_data_service
def test_get_market_data_history_by_id_start_timestamp(
    tds: TradingDataService, markets, start_timestamp
):
    market_id = markets[0]
    for market_data in tds.get_market_data_history_by_id(
        market_id=market_id, start_timestamp=start_timestamp, max_pages=1
    ):
        assert market_data.timestamp > start_timestamp


@pytest.mark.trading_data_service
def test_get_market_data_history_by_id_end_timestamp(
    tds: TradingDataService, markets, end_timestamp
):
    market_id = markets[0]
    for market_data in tds.get_market_data_history_by_id(
        market_id=market_id, end_timestamp=end_timestamp, max_pages=1
    ):
        assert market_data.timestamp < end_timestamp
