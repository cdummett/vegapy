# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vega/assets.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x11vega/assets.proto\x12\x04vega"\xed\x01\n\x05\x41sset\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12,\n\x07\x64\x65tails\x18\x02 \x01(\x0b\x32\x12.vega.AssetDetailsR\x07\x64\x65tails\x12*\n\x06status\x18\x03 \x01(\x0e\x32\x12.vega.Asset.StatusR\x06status"z\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x13\n\x0fSTATUS_PROPOSED\x10\x01\x12\x13\n\x0fSTATUS_REJECTED\x10\x02\x12\x1a\n\x16STATUS_PENDING_LISTING\x10\x03\x12\x12\n\x0eSTATUS_ENABLED\x10\x04"\xe0\x01\n\x0c\x41ssetDetails\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x16\n\x06symbol\x18\x02 \x01(\tR\x06symbol\x12\x1a\n\x08\x64\x65\x63imals\x18\x04 \x01(\x04R\x08\x64\x65\x63imals\x12\x18\n\x07quantum\x18\x05 \x01(\tR\x07quantum\x12\x39\n\rbuiltin_asset\x18\x65 \x01(\x0b\x32\x12.vega.BuiltinAssetH\x00R\x0c\x62uiltinAsset\x12#\n\x05\x65rc20\x18\x66 \x01(\x0b\x32\x0b.vega.ERC20H\x00R\x05\x65rc20B\x08\n\x06sourceJ\x04\x08\x03\x10\x04"C\n\x0c\x42uiltinAsset\x12\x33\n\x16max_faucet_amount_mint\x18\x01 \x01(\tR\x13maxFaucetAmountMint"\x88\x01\n\x05\x45RC20\x12)\n\x10\x63ontract_address\x18\x01 \x01(\tR\x0f\x63ontractAddress\x12%\n\x0elifetime_limit\x18\x02 \x01(\tR\rlifetimeLimit\x12-\n\x12withdraw_threshold\x18\x03 \x01(\tR\x11withdrawThreshold"{\n\x12\x41ssetDetailsUpdate\x12\x18\n\x07quantum\x18\x05 \x01(\tR\x07quantum\x12)\n\x05\x65rc20\x18\x65 \x01(\x0b\x32\x11.vega.ERC20UpdateH\x00R\x05\x65rc20B\x08\n\x06sourceJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05"c\n\x0b\x45RC20Update\x12%\n\x0elifetime_limit\x18\x01 \x01(\tR\rlifetimeLimit\x12-\n\x12withdraw_threshold\x18\x02 \x01(\tR\x11withdrawThresholdB\'Z%code.vegaprotocol.io/vega/protos/vegab\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "vega.assets_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"Z%code.vegaprotocol.io/vega/protos/vega"
    _globals["_ASSET"]._serialized_start = 28
    _globals["_ASSET"]._serialized_end = 265
    _globals["_ASSET_STATUS"]._serialized_start = 143
    _globals["_ASSET_STATUS"]._serialized_end = 265
    _globals["_ASSETDETAILS"]._serialized_start = 268
    _globals["_ASSETDETAILS"]._serialized_end = 492
    _globals["_BUILTINASSET"]._serialized_start = 494
    _globals["_BUILTINASSET"]._serialized_end = 561
    _globals["_ERC20"]._serialized_start = 564
    _globals["_ERC20"]._serialized_end = 700
    _globals["_ASSETDETAILSUPDATE"]._serialized_start = 702
    _globals["_ASSETDETAILSUPDATE"]._serialized_end = 825
    _globals["_ERC20UPDATE"]._serialized_start = 827
    _globals["_ERC20UPDATE"]._serialized_end = 926
# @@protoc_insertion_point(module_scope)
