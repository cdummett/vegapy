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
def test_market_data_network_flag(network_flag):
    try:
        subprocess.run(
            [
                "python",
                "-m",
                "examples.market_data",
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
def test_market_data_network_config_path(config_path_flag):
    try:
        subprocess.run(
            [
                "python",
                "-m",
                "examples.market_data",
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
def test_market_data_market_flag(market_flag):
    try:
        subprocess.run(
            [
                "python",
                "-m",
                "examples.market_data",
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
        "--mark_price",
        "--last_traded_price",
        "--indicative_price",
        "--mid_price",
        "--best_bid_price",
        "--best_ask_price",
        "--price_bounds",
        "--trading_mode",
        "--mark_price_sources",
    ],
)
def test_market_data_overlay_flag(overlay_flag):
    try:
        subprocess.run(
            [
                "python",
                "-m",
                "examples.market_data",
                overlay_flag,
            ],
            check=True,
            timeout=0.5,
        )
    except subprocess.TimeoutExpired:
        return
    assert False
