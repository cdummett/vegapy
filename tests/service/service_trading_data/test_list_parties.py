import pytest

from vegapy.service.service_trading_data import TradingDataService
from tests.fixtures import tds, parties

import vegapy.protobuf.protos as protos


@pytest.mark.trading_data_service
def test_list_parties(tds: TradingDataService):
    tds.list_parties(max_pages=1)


@pytest.mark.trading_data_service
def test_list_parties_party_id(tds: TradingDataService, parties):
    party_id_filter = parties[0]
    for party in tds.list_parties(party_id=party_id_filter, max_pages=1):
        assert party.id == party_id_filter
