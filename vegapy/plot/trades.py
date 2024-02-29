import numpy as np
import vegapy.protobuf.protos as protos

from typing import List
from matplotlib.axes import Axes
from vegapy.utils import (
    timestamp_to_datetime,
    padded_int_to_float,
)


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
    ax.step(x, y, label="size")


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
    ax.step(x, y, label="price")


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
    ax.step(x, y, label="volume")


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
    ax.step(x, y, label="maker_fee")


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
    ax.step(x, y, label="liquidity_fee")


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
    ax.step(x, y, label="infrastructure_fee")
