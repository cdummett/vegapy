import pytest

from vegapy.service.service_trading_data import TradingDataService
from tests.fixtures import tds, network_parameters

import vegapy.protobuf.protos as protos
from typing import List


@pytest.mark.trading_data_service
def test_get_network_parameter(
    tds: TradingDataService,
    network_parameters: List[protos.vega.vega.NetworkParameter],
):
    for network_parameter in network_parameters:
        assert (
            network_parameter.value
            == tds.get_network_parameter(key=network_parameter.key).value
        )
