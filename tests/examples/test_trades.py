import pytest
import subprocess

from vegapy.service.networks.constants import Network


@pytest.mark.examples
@pytest.mark.parametrize(
    "network_flag",
    [
        "mainnet",
        "stagnet",
        "testnet",
    ],
)
def test_trades_network_flag(network_flag):
    try:
        subprocess.run(
            [
                "python",
                "-m",
                "examples.trades",
                "-n",
                network_flag,
                "-m",
                "BTC",
            ],
            check=True,
            timeout=0.5,
        )
    except subprocess.TimeoutExpired:
        return
    assert False


@pytest.mark.examples
@pytest.mark.parametrize(
    "config_path_flag",
    [
        str(Network.NETWORK_MAINNET.config),
        str(Network.NETWORK_STAGNET.config),
        str(Network.NETWORK_TESTNET.config),
    ],
)
def test_trades_network_config_flag(config_path_flag):
    try:
        subprocess.run(
            [
                "python",
                "-m",
                "examples.trades",
                "-n",
                "local",
                "-c",
                config_path_flag,
            ],
            check=True,
            timeout=0.5,
        )
    except subprocess.TimeoutExpired:
        return
    assert False


@pytest.mark.examples
@pytest.mark.parametrize(
    "market_flag",
    [
        "BTC",
        "BTC USD",
        "BTC USD PERP",
    ],
)
def test_trades_market_flag(market_flag):
    try:
        subprocess.run(
            [
                "python",
                "-m",
                "examples.trades",
                "-m",
                market_flag,
            ],
            check=True,
            timeout=0.5,
        )
    except subprocess.TimeoutExpired:
        return
    assert False


@pytest.mark.examples
@pytest.mark.parametrize(
    "overlay_flag",
    [
        "--size",
        "--price",
        "--volume",
        "--maker_fee",
        "--liquidity_fee",
        "--infrastructure_fee",
    ],
)
def test_trades_overlay_flag(overlay_flag):
    try:
        subprocess.run(
            [
                "python",
                "-m",
                "examples.trades",
                overlay_flag,
            ],
            check=True,
            timeout=0.5,
        )
    except subprocess.TimeoutExpired:
        return
    assert False
