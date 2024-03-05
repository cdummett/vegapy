import datetime
import numpy as np
import vegapy.protobuf.protos as protos

from typing import List
from matplotlib.axes import Axes
from collections import defaultdict
from vegapy.utils import (
    timestamp_to_datetime,
    padded_int_to_float,
)


def overlay_mid_price(
    ax: Axes,
    market_data_history: List[protos.vega.vega.MarketData],
    price_decimals: int,
):
    x = []
    y = []
    for market_data in market_data_history:
        x.append(timestamp_to_datetime(market_data.timestamp, nano=True))
        price = padded_int_to_float(market_data.mid_price, price_decimals)
        y.append(price if price != 0 else np.nan)
    ax.step(x, y, label="mid_price", where="post")


def overlay_mark_price(
    ax: Axes,
    market_data_history: List[protos.vega.vega.MarketData],
    price_decimals: int,
):
    x = []
    y = []
    for market_data in market_data_history:
        x.append(timestamp_to_datetime(market_data.timestamp, nano=True))
        price = padded_int_to_float(market_data.mark_price, price_decimals)
        y.append(price if price != 0 else np.nan)
    ax.step(x, y, label="mark_price", where="post")


def overlay_last_traded_price(
    ax: Axes,
    market_data_history: List[protos.vega.vega.MarketData],
    price_decimals: int,
):
    x = []
    y = []
    for market_data in market_data_history:
        x.append(timestamp_to_datetime(market_data.timestamp, nano=True))
        price = padded_int_to_float(
            market_data.last_traded_price, price_decimals
        )
        y.append(price if price != 0 else np.nan)
    ax.step(x, y, label="last_traded_price", where="post")


def overlay_indicative_price(
    ax: Axes,
    market_data_history: List[protos.vega.vega.MarketData],
    price_decimals: int,
):
    x = []
    y = []
    for market_data in market_data_history:
        x.append(timestamp_to_datetime(market_data.timestamp, nano=True))
        price = padded_int_to_float(
            market_data.indicative_price, price_decimals
        )
        y.append(price if price != 0 else np.nan)
    ax.step(x, y, label="indicative_price", where="post")


def overlay_best_bid_price(
    ax: Axes,
    market_data_history: List[protos.vega.vega.MarketData],
    price_decimals: int,
):
    x = []
    y = []
    for market_data in market_data_history:
        x.append(timestamp_to_datetime(market_data.timestamp, nano=True))
        price = padded_int_to_float(market_data.best_bid_price, price_decimals)
        y.append(price if price != 0 else np.nan)
    ax.step(x, y, label="best_bid_price", where="post")


def overlay_best_ask_price(
    ax: Axes,
    market_data_history: List[protos.vega.vega.MarketData],
    price_decimals: int,
):
    x = []
    y = []
    for market_data in market_data_history:
        x.append(timestamp_to_datetime(market_data.timestamp, nano=True))
        price = padded_int_to_float(
            market_data.best_offer_price, price_decimals
        )
        y.append(price if price != 0 else np.nan)
    ax.step(x, y, label="best_ask_price", where="post")


def overlay_price_bounds(
    ax: Axes,
    market_data_history: List[protos.vega.vega.MarketData],
    price_decimals: int,
    all_bounds: bool = True,
):
    x = []
    y_min = []
    y_max = []
    valid_prices = defaultdict(lambda: {"x": [], "y_min": [], "y_max": []})
    for market_data in market_data_history:
        curr_datetime = timestamp_to_datetime(
            ts=market_data.timestamp, nano=True
        )

        for horizon in valid_prices:
            if horizon not in [
                bound.trigger.horizon
                for bound in market_data.price_monitoring_bounds
            ]:
                valid_prices[horizon]["x"].append(curr_datetime)
                valid_prices[horizon]["y_min"].append(np.NaN)
                valid_prices[horizon]["y_max"].append(np.NaN)

        max_min_valid_price = -np.inf
        min_max_valid_price = np.inf
        for bound in market_data.price_monitoring_bounds:
            valid_prices[bound.trigger.horizon]["x"].append(curr_datetime)
            min_valid_price = padded_int_to_float(
                bound.min_valid_price, price_decimals
            )
            max_valid_price = padded_int_to_float(
                bound.max_valid_price, price_decimals
            )
            valid_prices[bound.trigger.horizon]["y_min"].append(
                min_valid_price
            )
            valid_prices[bound.trigger.horizon]["y_max"].append(
                max_valid_price
            )
            if min_valid_price > max_min_valid_price:
                max_min_valid_price = min_valid_price
            if max_valid_price < min_max_valid_price:
                min_max_valid_price = max_valid_price

        x.append(curr_datetime)
        y_min.append(max_min_valid_price)
        y_max.append(min_max_valid_price)

    if all_bounds:
        for horizon, data in valid_prices.items():
            l = ax.step(
                data["x"],
                data["y_min"],
                label=f"valid price: {horizon}",
                where="post",
            )
            ax.step(
                data["x"], data["y_max"], color=l[0].get_color(), where="post"
            )
    l = ax.step(x, y_min, label=f"tightest bound", linewidth=1.5, where="post")
    ax.step(x, y_max, color=l[0].get_color(), linewidth=1.5, where="post")


def overlay_trading_mode(
    ax: Axes,
    market_data_history: List[protos.vega.vega.MarketData],
):
    trading_mode_history = defaultdict(lambda: {"x": [], "y": []})
    for market_data in market_data_history:
        for trading_mode in protos.vega.markets.Market.TradingMode.values():
            trading_mode_history[trading_mode]["x"].append(
                timestamp_to_datetime(ts=market_data.timestamp, nano=True)
            )
            if market_data.market_trading_mode == trading_mode:
                trading_mode_history[trading_mode]["y"].append(1)
            else:
                trading_mode_history[trading_mode]["y"].append(0)

    for trading_mode, data in trading_mode_history.items():
        if all(y == 0 for y in data["y"]):
            continue
        ax.fill_between(
            data["x"],
            data["y"],
            step="post",
            alpha=0.2,
            linewidth=0,
            label=protos.vega.markets.Market.TradingMode.Name(trading_mode),
        )


def overlay_mark_price_sources(
    ax: Axes,
    market_data_history: List[protos.vega.vega.MarketData],
    asset_decimals: int,
):
    price_sources = defaultdict(lambda: {"x": [], "y": []})

    for market_data in market_data_history:
        for price_source in market_data.mark_price_state.price_sources:
            price_sources[price_source.price_source]["x"].append(
                timestamp_to_datetime(price_source.last_updated, nano=True)
            )
            price = padded_int_to_float(price_source.price, asset_decimals)
            price_sources[price_source.price_source]["y"].append(
                price if price != 0 else np.nan
            )
    for key in price_sources:
        ax.step(
            price_sources[key]["x"],
            price_sources[key]["y"],
            "-o",
            markersize=1,
            label=key,
            alpha=1.0,
            linewidth=0.5,
            where="post",
        )


def overlay_internal_price_sources():
    # TODO: Implement function
    pass


def overlay_funding_payment():
    # TODO: Implement function
    pass


def overlay_funding_rate():
    # TODO: Implement function
    pass


def overlay_size(
    ax: Axes,
    trades: List[protos.vega.vega.Trade],
    size_decimals: int,
):
    x = []
    y = []
    for trade in trades:
        x.append(timestamp_to_datetime(trade.timestamp, nano=True))
        size = padded_int_to_float(trade.size, size_decimals)
        y.append(size if size != 0 else np.nan)
    ax.step(x, y, label="size", where="post")


def overlay_price(
    ax: Axes,
    trades: List[protos.vega.vega.Trade],
    price_decimals: int,
):
    x = []
    y = []
    for trade in trades:
        x.append(timestamp_to_datetime(trade.timestamp, nano=True))
        price = padded_int_to_float(trade.price, price_decimals)
        y.append(price if price != 0 else np.nan)
    ax.step(x, y, label="price", where="post")


def overlay_volume(
    ax: Axes,
    trades: List[protos.vega.vega.Trade],
    price_decimals: int,
    size_decimals: int,
):
    x = []
    y = []
    for trade in trades:
        x.append(timestamp_to_datetime(trade.timestamp, nano=True))
        price = padded_int_to_float(trade.price, price_decimals)
        size = padded_int_to_float(trade.size, size_decimals)
        y.append(price * size if price != 0 else np.nan)
    ax.step(x, y, label="volume", where="post")


def overlay_maker_fee(
    ax: Axes,
    trades: List[protos.vega.vega.Trade],
    asset_decimals: int,
    cumulative: bool = False,
):
    x = []
    y = []
    for trade in reversed(trades):
        x.append(timestamp_to_datetime(trade.timestamp, nano=True))
        buyer_maker_fee = padded_int_to_float(
            trade.buyer_fee.maker_fee, asset_decimals
        )
        seller_maker_fee = padded_int_to_float(
            trade.buyer_fee.maker_fee, asset_decimals
        )
        y.append(buyer_maker_fee + seller_maker_fee)
    if cumulative:
        y = np.cumsum(y)
    ax.step(x, y, label="maker_fee", where="post")


def overlay_liquidity_fee(
    ax: Axes,
    trades: List[protos.vega.vega.Trade],
    asset_decimals: int,
    cumulative: bool = False,
):
    x = []
    y = []
    for trade in reversed(trades):
        x.append(timestamp_to_datetime(trade.timestamp, nano=True))
        buyer_liquidity_fee = padded_int_to_float(
            trade.buyer_fee.liquidity_fee, asset_decimals
        )
        seller_liquidity_fee = padded_int_to_float(
            trade.buyer_fee.liquidity_fee, asset_decimals
        )
        y.append(buyer_liquidity_fee + seller_liquidity_fee)
    if cumulative:
        y = np.cumsum(y)
    ax.step(x, y, label="liquidity_fee", where="post")


def overlay_infrastructure_fee(
    ax: Axes,
    trades: List[protos.vega.vega.Trade],
    asset_decimals: int,
    cumulative: bool = False,
):
    x = []
    y = []
    for trade in reversed(trades):
        x.append(timestamp_to_datetime(trade.timestamp, nano=True))
        buyer_infrastructure_fee = padded_int_to_float(
            trade.buyer_fee.infrastructure_fee, asset_decimals
        )
        seller_infrastructure_fee = padded_int_to_float(
            trade.buyer_fee.infrastructure_fee, asset_decimals
        )
        y.append(buyer_infrastructure_fee + seller_infrastructure_fee)
    if cumulative:
        y = np.cumsum(y)
    ax.step(x, y, label="infrastructure_fee", where="post")


def overlay_network_position(
    ax: Axes,
    trades: List[protos.vega.vega.Trade],
    size_decimals: int,
):
    x = []
    y = []
    last_timestamp = None
    for trade in reversed(trades):
        dt = timestamp_to_datetime(trade.timestamp, nano=True)
        size = padded_int_to_float(trade.size, size_decimals)
        if trade.buyer == "network":
            if trade.timestamp != last_timestamp:
                x.append(dt)
                y.append(y[-1] if y != [] else 0)
                last_timestamp = trade.timestamp
            y[-1] += +size
        if trade.seller == "network":
            if trade.timestamp != last_timestamp:
                x.append(dt)
                y.append(y[-1] if y != [] else 0)
                last_timestamp = trade.timestamp
            y[-1] += -size
    ax.step(x, y, label="position", where="post")


def overlay_network_liquidations(
    ax: Axes,
    trades: List[protos.vega.vega.Trade],
    size_decimals: int,
):

    x_long = []
    y_long = []
    x_short = []
    y_short = []

    last_timestamp_long = None
    last_timestamp_short = None
    for trade in trades:

        if (
            trade.type
            != protos.vega.vega.Trade.Type.TYPE_NETWORK_CLOSE_OUT_BAD
        ):
            continue
        x = timestamp_to_datetime(trade.timestamp, nano=True)
        y = padded_int_to_float(trade.size, size_decimals)
        if trade.buyer == "network":
            if trade.timestamp != last_timestamp_long:
                x_long.append(x)
                y_long.append(0)
                last_timestamp_long = trade.timestamp
            y_long[-1] += y
        if trade.seller == "network":
            if trade.timestamp != last_timestamp_short:
                x_short.append(x)
                y_short.append(0)
                last_timestamp_short = trade.timestamp
            y_short[-1] += -y
    ax.bar(
        x_long,
        y_long,
        color="r",
        width=datetime.timedelta(seconds=30),
        label="longs",
    )
    ax.bar(
        x_short,
        y_short,
        color="g",
        width=datetime.timedelta(seconds=30),
        label="shorts",
    )


def overlay_balance(
    ax,
    aggregated_balances: List[
        protos.data_node.api.v2.trading_data.AggregatedBalance
    ],
    asset_decimals: int,
):
    x = []
    y = []
    for aggregated_balance in aggregated_balances:
        x.append(
            timestamp_to_datetime(aggregated_balance.timestamp, nano=True)
        )
        balance = padded_int_to_float(
            aggregated_balance.balance, asset_decimals
        )
        y.append(balance)
    ax.step(x, y, label="balance", where="post")
