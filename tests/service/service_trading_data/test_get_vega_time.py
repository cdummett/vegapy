import pytest

from vegapy.service.service_trading_data import TradingDataService
from tests.fixtures import tds

import vega_python_protos.protos as protos


@pytest.mark.trading_data_service
def test_get_vega_time(tds: TradingDataService):
    timestamp = tds.get_vega_time()
    assert isinstance(timestamp, int)
    assert timestamp > 0
