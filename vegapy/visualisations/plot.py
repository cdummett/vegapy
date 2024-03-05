from typing import List

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

import vegapy.protobuf.protos as protos
from vegapy.visualisations.overlay import (
    overlay_mark_price,
    overlay_last_traded_price,
    overlay_price_bounds,
    overlay_trading_mode,
    overlay_balance,
    overlay_network_position,
    overlay_network_liquidations,
    overlay_indicative_price,
)


def price_monitoring_analysis(
    market: protos.vega.markets.Market,
    market_data_history: List[protos.vega.vega.MarketData],
) -> Figure:

    fig = plt.figure(tight_layout=True)
    gs = fig.add_gridspec(1, 1)

    ax0l = fig.add_subplot(gs[:, :])
    ax0r: Axes = ax0l.twinx()
    overlay_last_traded_price(ax0l, market_data_history, market.decimal_places)
    overlay_indicative_price(ax0l, market_data_history, market.decimal_places)

    overlay_price_bounds(
        ax0l, market_data_history, market.decimal_places, all_bounds=False
    )
    overlay_trading_mode(ax0r, market_data_history)

    ax0l.set_title(
        f"Price Monitoring: {market.tradable_instrument.instrument.code}",
        loc="left",
    )
    ax0l.set_ylabel("price")
    ax0r.set_yticks([])
    leg = ax0l.legend(loc="upper left", framealpha=1)
    leg.remove()
    ax0r.legend(loc="upper right", framealpha=1)
    ax0r.add_artist(leg)

    return fig
