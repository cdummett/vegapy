# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vega/oracle.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .data.v1 import data_pb2 as vega_dot_data_dot_v1_dot_data__pb2
from . import data_source_pb2 as vega_dot_data__source__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x11vega/oracle.proto\x12\x04vega\x1a\x17vega/data/v1/data.proto\x1a\x16vega/data_source.proto"e\n\nOracleSpec\x12W\n\x19\x65xternal_data_source_spec\x18\x01 \x01(\x0b\x32\x1c.vega.ExternalDataSourceSpecR\x16\x65xternalDataSourceSpec"M\n\nOracleData\x12?\n\rexternal_data\x18\x01 \x01(\x0b\x32\x1a.vega.data.v1.ExternalDataR\x0c\x65xternalDataB\'Z%code.vegaprotocol.io/vega/protos/vegab\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "vega.oracle_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"Z%code.vegaprotocol.io/vega/protos/vega"
    )
    _globals["_ORACLESPEC"]._serialized_start = 76
    _globals["_ORACLESPEC"]._serialized_end = 177
    _globals["_ORACLEDATA"]._serialized_start = 179
    _globals["_ORACLEDATA"]._serialized_end = 256
# @@protoc_insertion_point(module_scope)
