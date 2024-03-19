import pytest

from vegapy.service.service_trading_data import TradingDataService
from tests.fixtures import tds

import vegapy.protobuf.protos as protos


@pytest.mark.trading_data_service
def test_list_network_parameters(
    tds: TradingDataService,
):
    for network_parameter in tds.list_network_parameters(max_pages=1):
        assert isinstance(network_parameter, protos.vega.vega.NetworkParameter)
