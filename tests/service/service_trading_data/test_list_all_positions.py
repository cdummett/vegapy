import pytest

from vegapy.service.service_trading_data import TradingDataService
from tests.fixtures import tds, markets, parties

import vegapy.protobuf.protos as protos


@pytest.mark.trading_data_service
def test_list_all_positions(tds: TradingDataService):
    tds.list_all_positions(max_pages=1)


@pytest.mark.trading_data_service
def test_list_all_positions_party_id(tds: TradingDataService, parties):
    party_ids_filter = parties[:2]
    for position in tds.list_all_positions(
        party_ids=party_ids_filter, max_pages=1
    ):
        assert position.party_id in party_ids_filter


@pytest.mark.trading_data_service
def test_list_all_positions_market_id(tds: TradingDataService, markets):
    market_ids_filter = markets[:2]
    for position in tds.list_all_positions(
        market_ids=market_ids_filter, max_pages=1
    ):
        assert position.market_id in market_ids_filter
