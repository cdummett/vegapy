import pytest

from vegapy.service.service_trading_data import TradingDataService
from tests.fixtures import (
    logger,
    tds,
    perpetual_markets,
    start_timestamp,
    end_timestamp,
)

import vegapy.protobuf.protos as protos
import datetime


@pytest.mark.trading_data_service
def test_list_funding_period_data_points_market_id(
    tds: TradingDataService, perpetual_markets
):
    market_id_filter = perpetual_markets[0]
    funding_period_data_points = tds.list_funding_period_data_points(
        market_id=market_id_filter,
        max_pages=1,
    )
    for funding_period_data_point in funding_period_data_points:
        assert funding_period_data_point.market_id == market_id_filter


@pytest.mark.trading_data_service
def test_list_funding_period_data_points_start_timestamp(
    tds: TradingDataService, perpetual_markets, start_timestamp
):
    market_id_filter = perpetual_markets[0]
    for funding_period_data_point in tds.list_funding_period_data_points(
        market_id=market_id_filter,
        start_timestamp=start_timestamp,
        max_pages=1,
    ):
        assert funding_period_data_point.timestamp > start_timestamp


@pytest.mark.trading_data_service
def test_list_funding_period_data_points_end_timestamp(
    tds: TradingDataService, perpetual_markets, end_timestamp
):
    market_id_filter = perpetual_markets[0]
    for funding_period_data_point in tds.list_funding_period_data_points(
        market_id=market_id_filter,
        end_timestamp=end_timestamp,
        max_pages=1,
    ):
        assert funding_period_data_point.timestamp < end_timestamp


def test_list_funding_period_data_points_source_filter(
    tds: TradingDataService, perpetual_markets
):
    market_id_filter = perpetual_markets[0]
    source_filter = (
        protos.vega.events.v1.events.FundingPeriodDataPoint.Source.values()[1]
    )
    for funding_period_data_point in tds.list_funding_period_data_points(
        market_id=market_id_filter,
        source=source_filter,
        max_pages=1,
    ):
        assert funding_period_data_point.data_point_type == source_filter


def test_list_funding_period_data_points_seq(
    tds: TradingDataService, perpetual_markets
):
    market_id_filter = perpetual_markets[0]
    seq_filter = 0
    for funding_period_data_point in tds.list_funding_period_data_points(
        market_id=market_id_filter,
        seq=seq_filter,
        max_pages=1,
    ):
        assert funding_period_data_point.seq == seq_filter
