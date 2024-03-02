import pytest

from vegapy.service.networks.constants import Network
from vegapy.service.service_trading_data import TradingDataService


@pytest.mark.networks
@pytest.mark.parametrize(
    "network",
    [
        Network.NETWORK_MAINNET,
        Network.NETWORK_TESTNET,
        Network.NETWORK_STAGNET,
    ],
)
def test_network_public(network: Network):
    assert network.config.exists()


@pytest.mark.networks
@pytest.mark.parametrize(
    "network",
    [
        Network.NETWORK_LOCAL,
    ],
)
def test_network_local(network: Network):
    assert network.config is None
