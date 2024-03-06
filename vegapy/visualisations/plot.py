from typing import List

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

import vegapy.protobuf.protos as protos
from vegapy.visualisations.overlay import *


def price_monitoring_analysis(
    market: protos.vega.markets.Market,
    market_data_history: List[protos.vega.vega.MarketData],
) -> Figure:

    fig = plt.figure(tight_layout=True, figsize=(15, 8))
    gs = fig.add_gridspec(1, 1)

    ax0l = fig.add_subplot(gs[:, :])
    ax0r: Axes = ax0l.twinx()
    overlay_last_traded_price(ax0l, market_data_history, market.decimal_places)
    overlay_indicative_price(ax0l, market_data_history, market.decimal_places)
    overlay_price_bounds(
        ax0l,
        market_data_history,
        market.decimal_places,
        tightest_bounds=False,
    )
    overlay_trading_mode(ax0r, market_data_history)
    overlay_auction_starts(ax0r, market_data_history)
    overlay_auction_ends(ax0r, market_data_history)

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


def liquidation_analysis(
    asset: protos.vega.assets.Asset,
    market: protos.vega.markets.Market,
    trades: List[protos.vega.vega.Trade],
    market_data_history: List[protos.vega.vega.MarketData],
    aggregated_balance_history: List[
        protos.data_node.api.v2.trading_data.AggregatedBalance
    ],
) -> Figure:

    fig = plt.figure(tight_layout=True, figsize=(15, 8))
    gs = fig.add_gridspec(3, 2, height_ratios=[1, 2, 2])

    ax0l = fig.add_subplot(gs[:, 0])
    ax0r: Axes = ax0l.twinx()
    if market_data_history is not None:
        overlay_mark_price(ax0l, market_data_history, market.decimal_places)
        overlay_trading_mode(ax0r, market_data_history)
        overlay_auction_starts(ax0r, market_data_history)
        overlay_auction_ends(ax0r, market_data_history)
    ax0l.set_ylabel("price")
    ax0r.set_yticks([])

    ax1l = fig.add_subplot(gs[0, 1])
    ax1l.sharex(ax0l)
    ax1l.axhline(0, alpha=0.5, color="k", linewidth=1)
    ax1l.ticklabel_format(axis="y", style="sci", scilimits=(3, 3))
    overlay_network_liquidations(ax1l, trades, market.position_decimal_places)
    ax1l.legend(loc="upper left", framealpha=1)
    ax1l.set_ylabel("volume")

    ax2l = fig.add_subplot(gs[1, 1])
    ax2l.sharex(ax0l)
    ax2l.axhline(0, alpha=0.5, color="k", linewidth=1)
    ax2l.ticklabel_format(axis="y", style="sci", scilimits=(3, 3))
    overlay_network_position(ax2l, trades, market.position_decimal_places)
    ax2l.set_ylabel("position")

    ax3l = fig.add_subplot(gs[2, 1])
    ax3l.sharex(ax0l)
    ax3l.ticklabel_format(axis="y", style="scientific", scilimits=(6, 6))
    overlay_balance(ax3l, aggregated_balance_history, asset.details.decimals)
    ax3l.set_ylabel("insurance pool")

    leg = ax0l.legend(loc="upper left", framealpha=1)
    leg.remove()
    ax0r.legend(loc="upper right", framealpha=1)
    ax0r.add_artist(leg)

    ax0l.set_title(
        f"Liquidation analysis: {market.tradable_instrument.instrument.code}",
        loc="left",
    )

    return fig
