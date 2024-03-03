import argparse
import pathlib
import datetime

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from vegapy.service.service import Service
from vegapy.service.networks.constants import Network
from vegapy.visualisations.overlay import (
    overlay_mark_price,
    overlay_last_traded_price,
    overlay_indicative_price,
    overlay_mid_price,
    overlay_best_bid_price,
    overlay_best_ask_price,
    overlay_price_bounds,
    overlay_trading_mode,
    overlay_mark_price_sources,
)
from vegapy.utils import datetime_to_timestamp


# TODO: Tidy up the help formatter for the argument parser
PARSER = argparse.ArgumentParser()

# Service options
PARSER.add_argument(
    "-n",
    "--network",
    default="mainnet",
    help="Network to create service for. Specify testnet, stagnet, or mainnet.",
)
PARSER.add_argument(
    "-c",
    "--config",
    type=str,
    default=None,
    help="Specify path to network config file.",
)
PARSER.add_argument(
    "-p",
    "--pages",
    type=int,
    default=None,
    help="Specify maximum number of pages paginated API requests will return.",
)

# Data options
PARSER.add_argument(
    "-m",
    "--market",
    nargs="+",
    default=["BTC"],
    help="Specify substrings to match against market codes.",
)

PARSER.add_argument(
    "--start_datetime",
    type=datetime.datetime.fromisoformat,
    help="Specify datetime to retrieve data from (format: YYYY-MM-DD:HH:mm:ss).",
)
PARSER.add_argument(
    "--end_datetime",
    type=datetime.datetime.fromisoformat,
    help="Specify datetime to retrieve data to (format: YYYY-MM-DD:HH:mm:ss).",
)


# Overlay options
PARSER.add_argument(
    "--mark_price",
    action="store_true",
    help="Overlay historic mark price on plot.",
)
PARSER.add_argument(
    "--last_traded_price",
    action="store_true",
    help="Overlay last traded price on plot.",
)
PARSER.add_argument(
    "--indicative_price",
    action="store_true",
    help="Overlay historic indicative price on plot.",
)
PARSER.add_argument(
    "--mid_price",
    action="store_true",
    help="Overlay historic mid price on plot.",
)
PARSER.add_argument(
    "--best_bid_price",
    action="store_true",
    help="Overlay historic best bid price on plot.",
)
PARSER.add_argument(
    "--best_ask_price",
    action="store_true",
    help="Overlay historic best bid price on plot.",
)
PARSER.add_argument(
    "--price_bounds",
    action="store_true",
    help="Overlay all price_bounds on plot.",
)
PARSER.add_argument(
    "--trading_mode",
    action="store_true",
    help="Overlay trading mode on plot.",
)
PARSER.add_argument(
    "--mark_price_sources",
    action="store_true",
    help="Overlay historic mark price sources on plot.",
)


if __name__ == "__main__":
    args = PARSER.parse_args()

    # Create a service for the specified network
    if args.network == "local":
        network = Network.NETWORK_LOCAL
    elif args.network == "mainnet":
        network = Network.NETWORK_MAINNET
    elif args.network == "stagnet":
        network = Network.NETWORK_STAGNET
    elif args.network == "testnet":
        network = Network.NETWORK_TESTNET
    else:
        raise ValueError(
            f"Invalid network, {args.network}, selected. Please select, local, mainnet, stagnet, or testnet."
        )
    service = Service(
        network, pathlib.Path(args.config) if args.config else None
    )

    if args.start_datetime is None:
        start_timestamp = int(
            service.api.data.get_vega_time() - 1 * 60 * 60 * 1e9
        )
    else:
        start_timestamp = datetime_to_timestamp(args.start_datetime, nano=True)
    if args.end_datetime is None:
        end_timestamp = int(service.api.data.get_vega_time())
    else:
        end_timestamp = datetime_to_timestamp(args.end_datetime, nano=True)

    # Get the market, asset, and market data for the specified market and times
    market = service.utils.market.find_market(args.market)
    asset = service.utils.market.find_settlement_asset(args.market)
    market_data_history = service.api.data.get_market_data_history_by_id(
        market_id=market.id,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        max_pages=args.pages,
    )

    fig: Figure
    axl: Axes
    axr: Axes

    fig, axl = plt.subplots(1, 1)
    axr = axl.twinx()

    if args.mark_price:
        overlay_mark_price(
            axl,
            market_data_history=market_data_history,
            price_decimals=market.decimal_places,
        )
    if args.last_traded_price:
        overlay_last_traded_price(
            axl,
            market_data_history=market_data_history,
            price_decimals=market.decimal_places,
        )
    if args.indicative_price:
        overlay_indicative_price(
            axl,
            market_data_history=market_data_history,
            price_decimals=market.decimal_places,
        )
    if args.mid_price:
        overlay_mid_price(
            axl,
            market_data_history=market_data_history,
            price_decimals=market.decimal_places,
        )
    if args.best_bid_price:
        overlay_best_bid_price(
            axl,
            market_data_history=market_data_history,
            price_decimals=market.decimal_places,
        )
    if args.best_ask_price:
        overlay_best_ask_price(
            axl,
            market_data_history=market_data_history,
            price_decimals=market.decimal_places,
        )
    if args.price_bounds:
        overlay_price_bounds(
            axl,
            market_data_history=market_data_history,
            price_decimals=market.decimal_places,
        )
    if args.trading_mode:
        overlay_trading_mode(
            axr,
            market_data_history=market_data_history,
        )
    if args.mark_price_sources:
        overlay_mark_price_sources(
            axl,
            market_data_history=market_data_history,
            asset_decimals=asset.details.decimals,
        )

    axl.set_title(
        f"Market Data: {market.tradable_instrument.instrument.name}",
        loc="left",
    )
    axl.set_xlabel("datetime")
    axl.set_ylabel(asset.details.symbol)
    axl.legend(loc="upper left")
    axr.legend(loc="upper right")

    plt.show()
