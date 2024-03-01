import pytest

from vegapy.service.service_trading_data import TradingDataService
from tests.fixtures import tds, assets

import vegapy.protobuf.protos as protos


@pytest.mark.trading_data_service
def test_list_assets(tds: TradingDataService):
    tds.list_assets(max_pages=1)


@pytest.mark.trading_data_service
def test_list_assets_asset_id(tds: TradingDataService, assets):
    asset_id_filter = assets[0]
    for asset in tds.list_assets(asset_id=asset_id_filter, max_pages=1):
        assert asset.id == asset_id_filter
