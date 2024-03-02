import pytest

from vegapy.service.service_trading_data import TradingDataService
from tests.fixtures import tds, markets

import vegapy.protobuf.protos as protos
import datetime


@pytest.mark.trading_data_service
def test_get_market_data_history_by_id_market_id(
    tds: TradingDataService, markets
):
    market_id = (
        "4e9081e20e9e81f3e747d42cb0c9b8826454df01899e6027a22e771e19cc79fc"
    )
    for market_data in tds.get_market_data_history_by_id(
        market_id=market_id, max_pages=1
    ):
        assert market_data.market == market_id


@pytest.mark.trading_data_service
def test_get_market_data_history_by_id_start_timestamp(
    tds: TradingDataService, markets
):
    market_id = (
        "4e9081e20e9e81f3e747d42cb0c9b8826454df01899e6027a22e771e19cc79fc"
    )
    start_timestamp = int(
        (datetime.datetime.now() - datetime.timedelta(days=1)).timestamp()
        * 1e9
    )
    for market_data in tds.get_market_data_history_by_id(
        market_id=market_id, start_timestamp=start_timestamp, max_pages=1
    ):
        assert market_data.timestamp > start_timestamp


@pytest.mark.trading_data_service
def test_get_market_data_history_by_id_end_timestamp(
    tds: TradingDataService, markets
):
    market_id = (
        "4e9081e20e9e81f3e747d42cb0c9b8826454df01899e6027a22e771e19cc79fc"
    )
    end_timestamp = int(
        (datetime.datetime.now() - datetime.timedelta(days=1)).timestamp()
        * 1e9
    )
    for market_data in tds.get_market_data_history_by_id(
        market_id=market_id, end_timestamp=end_timestamp, max_pages=1
    ):
        assert market_data.timestamp < end_timestamp
