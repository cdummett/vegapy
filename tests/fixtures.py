import logging

from typing import List
import vegapy.protobuf.protos as protos

from vegapy.service.networks.constants import Network
from vegapy.service.service_trading_data import TradingDataService


from pytest import fixture

logger = logging.getLogger(__name__)

DEFAULT_NETWORK = Network.NETWORK_TESTNET


@fixture(scope="session")
def tds():
    client = TradingDataService(network=DEFAULT_NETWORK)
    yield client


@fixture(scope="session")
def markets(tds: TradingDataService) -> List[str]:
    return [market.id for market in tds.list_markets(max_pages=1)]


@fixture(scope="session")
def perpetual_markets(tds: TradingDataService) -> List[str]:
    return [
        market.id
        for market in tds.list_markets(max_pages=1)
        if market.tradable_instrument.instrument.perpetual is not None
    ]


@fixture(scope="session")
def future_markets(tds: TradingDataService) -> List[str]:
    return [
        market.id
        for market in tds.list_markets(max_pages=1)
        if market.tradable_instrument.instrument.future is not None
    ]


@fixture(scope="session")
def spot_markets(tds: TradingDataService) -> List[str]:
    return [
        market.id
        for market in tds.list_markets(max_pages=1)
        if market.tradable_instrument.instrument.spot is not None
    ]


@fixture(scope="session")
def assets(tds: TradingDataService) -> List[str]:
    return [asset.id for asset in tds.list_assets(max_pages=1)]


@fixture(scope="session")
def parties(tds: TradingDataService) -> List[str]:
    return [party.id for party in tds.list_parties(max_pages=1)]


@fixture(scope="session")
def orders(tds: TradingDataService) -> List[protos.vega.vega.Order]:
    return tds.list_orders(max_pages=1)


@fixture(scope="session")
def governance_data(
    tds: TradingDataService,
) -> List[protos.vega.governance.GovernanceData]:
    return tds.list_governance_data(max_pages=1)


@fixture(scope="session")
def start_timestamp(tds: TradingDataService) -> int:
    return int(tds.get_vega_time() - (1 * 60 * 60 * 1e9))


@fixture(scope="session")
def end_timestamp(tds: TradingDataService) -> int:
    return int(tds.get_vega_time() - (2 * 60 * 60 * 1e9))
