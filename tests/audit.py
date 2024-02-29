import logging
import vegapy.proto as proto
from vegapy.service.service_trading_data import TradingDataService


def camel_to_snake(name):
    return "".join(
        ["_" + c.lower() if c.isupper() else c for c in name]
    ).lstrip("_")


def test_check_implemented_method_coverage():
    implemented_methods = []
    for method in TradingDataService.__dict__:
        if not method.startswith("_"):
            implemented_methods.append(method)
    missing_methods = 0
    for (
        method
    ) in proto.data_node.api.v2.trading_data_grpc.TradingDataService.__dict__:
        if not method.startswith("_"):
            try:
                assert camel_to_snake(method) in implemented_methods
            except AssertionError as e:
                logging.error(f"Method {method} not implemented.")
                missing_methods += 1
    assert missing_methods == 0


import os


def test_check_tested_method_coverage():
    implemented_methods = []
    for method in TradingDataService.__dict__:
        if not method.startswith("_"):
            implemented_methods.append(method)

    os.walk(os.getcwd())

    os.cwd()
    import pathlib

    pathlib.Path(__file__)
    # tested_methods =


if __name__ == "__main__":
    import os
    import pathlib

    dir = pathlib.Path("tests")

    for file in dir.absolute().glob("test_*.py"):
        print(file.suffix, type(file))
