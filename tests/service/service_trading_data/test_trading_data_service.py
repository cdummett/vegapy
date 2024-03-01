import pytest

from vegapy.service.networks.constants import Network
from vegapy.service.service_trading_data import TradingDataService


@pytest.mark.networks
@pytest.mark.trading_data_service
@pytest.mark.parametrize(
    "network",
    [
        Network.NETWORK_MAINNET,
        Network.NETWORK_TESTNET,
        Network.NETWORK_STAGNET,
    ],
)
def test_trading_data_service(network):
    tds = TradingDataService(network=network)
    tds.ping()
