import pytest

from vegapy.service.service_trading_data import TradingDataService
from tests.fixtures import (
    logger,
    tds,
    parties,
    perpetual_markets,
)


@pytest.mark.trading_data_service
def test_list_funding_payments_party_id(tds: TradingDataService, parties):
    party_id_filter = parties[1]
    for funding_payment in tds.list_funding_payments(
        party_id=party_id_filter,
        max_pages=1,
    ):
        assert funding_payment.party_id == party_id_filter


@pytest.mark.trading_data_service
def test_list_funding_payments_market_id(
    tds: TradingDataService, parties, perpetual_markets
):
    party_id_filter = parties[1]
    market_id_filter = perpetual_markets[0]
    for funding_payment in tds.list_funding_payments(
        party_id=party_id_filter,
        market_id=market_id_filter,
        max_pages=1,
    ):
        assert funding_payment.party_id == party_id_filter
