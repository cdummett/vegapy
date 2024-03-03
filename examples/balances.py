import argparse
import pathlib
import datetime

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from vegapy.service.service import Service
from vegapy.service.networks.constants import Network
from vegapy.visualisations.overlay import (
    overlay_balance,
)
from vegapy.utils import datetime_to_timestamp
import vegapy.protobuf.protos as protos


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
    "-fa",
    "--asset",
    help="Specify asset id to filter balances by.",
)
PARSER.add_argument(
    "-fm",
    "--market",
    help="Specify market id to filter balances by.",
)
PARSER.add_argument(
    "-fp",
    "--party",
    help="Specify party id to filter balances by.",
)
PARSER.add_argument(
    "-ft",
    "--type",
    help="Specify account type to filter balances by (e.g. ACCOUNT_TYPE_GENERAL).",
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
            service.api.data.get_vega_time() - 2 * 24 * 60 * 60 * 1e9
        )
    else:
        start_timestamp = datetime_to_timestamp(args.start_datetime, nano=True)
    if args.end_datetime is None:
        end_timestamp = int(service.api.data.get_vega_time())
    else:
        end_timestamp = datetime_to_timestamp(args.end_datetime, nano=True)

    # Get the data
    asset = service.utils.asset.find_asset(args.asset)
    market = (
        service.utils.market.find_market(args.market)
        if args.market is not None
        else None
    )
    account_type = getattr(protos.vega.vega.AccountType, args.type)

    aggregated_balances = service.api.data.list_balance_changes(
        asset_id=asset.id,
        party_ids=[args.party],
        market_ids=[market.id] if market is not None else None,
        account_types=[account_type],
        date_range_start_timestamp=start_timestamp,
        date_range_end_timestamp=end_timestamp,
        max_pages=args.pages,
    )

    fig: Figure
    axl: Axes
    axr: Axes

    fig, axl = plt.subplots(1, 1)
    axr = axl.twinx()

    overlay_balance(
        axl,
        aggregated_balances=aggregated_balances,
        asset_decimals=asset.details.decimals,
    )

    axl.set_title(
        f"Balance: {args.party[:7]} | {market.tradable_instrument.instrument.code if market is not None else asset.id} | {args.type}",
        loc="left",
    )
    axl.set_xlabel("datetime")
    axl.set_ylabel(asset.details.symbol)
    axl.legend(loc="upper left")
    axr.legend(loc="upper right")

    plt.show()
