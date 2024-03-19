# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vega/api/v1/core.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import (
    field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2,
)
from protoc_gen_openapiv2.options import (
    annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2,
)
from ...commands.v1 import (
    transaction_pb2 as vega_dot_commands_dot_v1_dot_transaction__pb2,
)
from ...events.v1 import events_pb2 as vega_dot_events_dot_v1_dot_events__pb2
from ... import vega_pb2 as vega_dot_vega__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x16vega/api/v1/core.proto\x12\x0bvega.api.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a"vega/commands/v1/transaction.proto\x1a\x1bvega/events/v1/events.proto\x1a\x0fvega/vega.proto"{\n\x1aPropagateChainEventRequest\x12\x1a\n\x05\x65vent\x18\x01 \x01(\x0c\x42\x04\xe2\x41\x01\x02R\x05\x65vent\x12\x1d\n\x07pub_key\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x06pubKey\x12"\n\tsignature\x18\x03 \x01(\x0c\x42\x04\xe2\x41\x01\x02R\tsignature"7\n\x1bPropagateChainEventResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"\xe3\x01\n\x18SubmitTransactionRequest\x12\x33\n\x02tx\x18\x01 \x01(\x0b\x32\x1d.vega.commands.v1.TransactionB\x04\xe2\x41\x01\x02R\x02tx\x12\x44\n\x04type\x18\x02 \x01(\x0e\x32*.vega.api.v1.SubmitTransactionRequest.TypeB\x04\xe2\x41\x01\x02R\x04type"L\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nTYPE_ASYNC\x10\x01\x12\r\n\tTYPE_SYNC\x10\x02\x12\x0f\n\x0bTYPE_COMMIT\x10\x03"\xa0\x01\n\x19SubmitTransactionResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x17\n\x07tx_hash\x18\x02 \x01(\tR\x06txHash\x12\x12\n\x04\x63ode\x18\x03 \x01(\rR\x04\x63ode\x12\x12\n\x04\x64\x61ta\x18\x04 \x01(\tR\x04\x64\x61ta\x12\x10\n\x03log\x18\x05 \x01(\tR\x03log\x12\x16\n\x06height\x18\x06 \x01(\x03R\x06height"N\n\x17\x43heckTransactionRequest\x12\x33\n\x02tx\x18\x01 \x01(\x0b\x32\x1d.vega.commands.v1.TransactionB\x04\xe2\x41\x01\x02R\x02tx"\xbc\x01\n\x18\x43heckTransactionResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x12\n\x04\x63ode\x18\x02 \x01(\rR\x04\x63ode\x12\x1d\n\ngas_wanted\x18\x03 \x01(\x03R\tgasWanted\x12\x19\n\x08gas_used\x18\x04 \x01(\x03R\x07gasUsed\x12\x12\n\x04\x64\x61ta\x18\x05 \x01(\tR\x04\x64\x61ta\x12\x10\n\x03log\x18\x06 \x01(\tR\x03log\x12\x12\n\x04info\x18\x07 \x01(\tR\x04info"\xca\x01\n\x1bSubmitRawTransactionRequest\x12\x14\n\x02tx\x18\x01 \x01(\x0c\x42\x04\xe2\x41\x01\x02R\x02tx\x12G\n\x04type\x18\x02 \x01(\x0e\x32-.vega.api.v1.SubmitRawTransactionRequest.TypeB\x04\xe2\x41\x01\x02R\x04type"L\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nTYPE_ASYNC\x10\x01\x12\r\n\tTYPE_SYNC\x10\x02\x12\x0f\n\x0bTYPE_COMMIT\x10\x03"\xa3\x01\n\x1cSubmitRawTransactionResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x17\n\x07tx_hash\x18\x02 \x01(\tR\x06txHash\x12\x12\n\x04\x63ode\x18\x03 \x01(\rR\x04\x63ode\x12\x12\n\x04\x64\x61ta\x18\x04 \x01(\tR\x04\x64\x61ta\x12\x10\n\x03log\x18\x05 \x01(\tR\x03log\x12\x16\n\x06height\x18\x06 \x01(\x03R\x06height"2\n\x1a\x43heckRawTransactionRequest\x12\x14\n\x02tx\x18\x01 \x01(\x0c\x42\x04\xe2\x41\x01\x02R\x02tx"\xbf\x01\n\x1b\x43heckRawTransactionResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12\x12\n\x04\x63ode\x18\x02 \x01(\rR\x04\x63ode\x12\x1d\n\ngas_wanted\x18\x03 \x01(\x03R\tgasWanted\x12\x19\n\x08gas_used\x18\x04 \x01(\x03R\x07gasUsed\x12\x12\n\x04\x64\x61ta\x18\x05 \x01(\tR\x04\x64\x61ta\x12\x10\n\x03log\x18\x06 \x01(\tR\x03log\x12\x12\n\x04info\x18\x07 \x01(\tR\x04info"\x14\n\x12GetVegaTimeRequest"3\n\x13GetVegaTimeResponse\x12\x1c\n\ttimestamp\x18\x01 \x01(\x03R\ttimestamp"\xa1\x01\n\x16ObserveEventBusRequest\x12\x30\n\x04type\x18\x01 \x03(\x0e\x32\x1c.vega.events.v1.BusEventTypeR\x04type\x12\x1b\n\tmarket_id\x18\x02 \x01(\tR\x08marketId\x12\x19\n\x08party_id\x18\x03 \x01(\tR\x07partyId\x12\x1d\n\nbatch_size\x18\x04 \x01(\x03R\tbatchSize"K\n\x17ObserveEventBusResponse\x12\x30\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x18.vega.events.v1.BusEventR\x06\x65vents"\x13\n\x11StatisticsRequest"M\n\x12StatisticsResponse\x12\x37\n\nstatistics\x18\x01 \x01(\x0b\x32\x17.vega.api.v1.StatisticsR\nstatistics"\xc8\x0c\n\nStatistics\x12!\n\x0c\x62lock_height\x18\x01 \x01(\x04R\x0b\x62lockHeight\x12%\n\x0e\x62\x61\x63klog_length\x18\x02 \x01(\x04R\rbacklogLength\x12\x1f\n\x0btotal_peers\x18\x03 \x01(\x04R\ntotalPeers\x12!\n\x0cgenesis_time\x18\x04 \x01(\tR\x0bgenesisTime\x12!\n\x0c\x63urrent_time\x18\x05 \x01(\tR\x0b\x63urrentTime\x12\x1b\n\tvega_time\x18\x06 \x01(\tR\x08vegaTime\x12)\n\x06status\x18\x07 \x01(\x0e\x32\x11.vega.ChainStatusR\x06status\x12 \n\x0ctx_per_block\x18\x08 \x01(\x04R\ntxPerBlock\x12(\n\x10\x61verage_tx_bytes\x18\t \x01(\x04R\x0e\x61verageTxBytes\x12\x37\n\x18\x61verage_orders_per_block\x18\n \x01(\x04R\x15\x61verageOrdersPerBlock\x12*\n\x11trades_per_second\x18\x0b \x01(\x04R\x0ftradesPerSecond\x12*\n\x11orders_per_second\x18\x0c \x01(\x04R\x0fordersPerSecond\x12#\n\rtotal_markets\x18\r \x01(\x04R\x0ctotalMarkets\x12*\n\x11total_amend_order\x18\x10 \x01(\x04R\x0ftotalAmendOrder\x12,\n\x12total_cancel_order\x18\x11 \x01(\x04R\x10totalCancelOrder\x12,\n\x12total_create_order\x18\x12 \x01(\x04R\x10totalCreateOrder\x12!\n\x0ctotal_orders\x18\x13 \x01(\x04R\x0btotalOrders\x12!\n\x0ctotal_trades\x18\x14 \x01(\x04R\x0btotalTrades\x12/\n\x13order_subscriptions\x18\x15 \x01(\rR\x12orderSubscriptions\x12/\n\x13trade_subscriptions\x18\x16 \x01(\rR\x12tradeSubscriptions\x12\x31\n\x14\x63\x61ndle_subscriptions\x18\x17 \x01(\rR\x13\x63\x61ndleSubscriptions\x12<\n\x1amarket_depth_subscriptions\x18\x18 \x01(\rR\x18marketDepthSubscriptions\x12\x37\n\x17positions_subscriptions\x18\x19 \x01(\rR\x16positionsSubscriptions\x12\x33\n\x15\x61\x63\x63ount_subscriptions\x18\x1a \x01(\rR\x14\x61\x63\x63ountSubscriptions\x12:\n\x19market_data_subscriptions\x18\x1b \x01(\rR\x17marketDataSubscriptions\x12(\n\x10\x61pp_version_hash\x18\x1c \x01(\tR\x0e\x61ppVersionHash\x12\x1f\n\x0b\x61pp_version\x18\x1d \x01(\tR\nappVersion\x12#\n\rchain_version\x18\x1e \x01(\tR\x0c\x63hainVersion\x12%\n\x0e\x62lock_duration\x18\x1f \x01(\x04R\rblockDuration\x12\x16\n\x06uptime\x18  \x01(\tR\x06uptime\x12\x19\n\x08\x63hain_id\x18! \x01(\tR\x07\x63hainId\x12K\n"market_depth_updates_subscriptions\x18" \x01(\rR\x1fmarketDepthUpdatesSubscriptions\x12\x1d\n\nblock_hash\x18# \x01(\tR\tblockHash\x12\x1b\n\tepoch_seq\x18$ \x01(\x04R\x08\x65pochSeq\x12(\n\x10\x65poch_start_time\x18% \x01(\tR\x0e\x65pochStartTime\x12*\n\x11\x65poch_expiry_time\x18& \x01(\tR\x0f\x65pochExpiryTime\x12\x1f\n\x0b\x65vent_count\x18\' \x01(\x04R\neventCount\x12*\n\x11\x65vents_per_second\x18( \x01(\x04R\x0f\x65ventsPerSecond"\x18\n\x16LastBlockHeightRequest"\x91\x03\n\x17LastBlockHeightResponse\x12\x16\n\x06height\x18\x01 \x01(\x04R\x06height\x12\x12\n\x04hash\x18\x02 \x01(\tR\x04hash\x12\x33\n\x16spam_pow_hash_function\x18\x03 \x01(\tR\x13spamPowHashFunction\x12.\n\x13spam_pow_difficulty\x18\x04 \x01(\rR\x11spamPowDifficulty\x12\x41\n\x1espam_pow_number_of_past_blocks\x18\x05 \x01(\rR\x19spamPowNumberOfPastBlocks\x12\x42\n\x1fspam_pow_number_of_tx_per_block\x18\x06 \x01(\rR\x19spamPowNumberOfTxPerBlock\x12\x43\n\x1espam_pow_increasing_difficulty\x18\x07 \x01(\x08R\x1bspamPowIncreasingDifficulty\x12\x19\n\x08\x63hain_id\x18\x08 \x01(\tR\x07\x63hainId";\n\x18GetSpamStatisticsRequest\x12\x1f\n\x08party_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x07partyId"\xc4\x01\n\rSpamStatistic\x12&\n\x0f\x63ount_for_epoch\x18\x01 \x01(\x04R\rcountForEpoch\x12"\n\rmax_for_epoch\x18\x02 \x01(\x04R\x0bmaxForEpoch\x12&\n\x0c\x62\x61nned_until\x18\x04 \x01(\tH\x00R\x0b\x62\x61nnedUntil\x88\x01\x01\x12.\n\x13min_tokens_required\x18\x05 \x01(\tR\x11minTokensRequiredB\x0f\n\r_banned_until"\xb1\x01\n\x12VoteSpamStatistics\x12>\n\nstatistics\x18\x01 \x03(\x0b\x32\x1e.vega.api.v1.VoteSpamStatisticR\nstatistics\x12"\n\rmax_for_epoch\x18\x02 \x01(\x04R\x0bmaxForEpoch\x12&\n\x0c\x62\x61nned_until\x18\x03 \x01(\tH\x00R\x0b\x62\x61nnedUntil\x88\x01\x01\x42\x0f\n\r_banned_until"\x87\x01\n\x11VoteSpamStatistic\x12\x1a\n\x08proposal\x18\x01 \x01(\tR\x08proposal\x12&\n\x0f\x63ount_for_epoch\x18\x02 \x01(\x04R\rcountForEpoch\x12.\n\x13min_tokens_required\x18\x03 \x01(\tR\x11minTokensRequired"\xe8\x02\n\rPoWBlockState\x12!\n\x0c\x62lock_height\x18\x01 \x01(\x04R\x0b\x62lockHeight\x12\x1d\n\nblock_hash\x18\x02 \x01(\tR\tblockHash\x12+\n\x11transactions_seen\x18\x03 \x01(\x04R\x10transactionsSeen\x12\x34\n\x13\x65xpected_difficulty\x18\x04 \x01(\x04H\x00R\x12\x65xpectedDifficulty\x88\x01\x01\x12#\n\rhash_function\x18\x05 \x01(\tR\x0chashFunction\x12\x1e\n\ndifficulty\x18\x06 \x01(\x04R\ndifficulty\x12 \n\x0ctx_per_block\x18\x07 \x01(\x04R\ntxPerBlock\x12\x33\n\x15increasing_difficulty\x18\x08 \x01(\x08R\x14increasingDifficultyB\x16\n\x14_expected_difficulty"\xb9\x01\n\x0cPoWStatistic\x12=\n\x0c\x62lock_states\x18\x01 \x03(\x0b\x32\x1a.vega.api.v1.PoWBlockStateR\x0b\x62lockStates\x12&\n\x0c\x62\x61nned_until\x18\x02 \x01(\tH\x00R\x0b\x62\x61nnedUntil\x88\x01\x01\x12\x31\n\x15number_of_past_blocks\x18\x03 \x01(\x04R\x12numberOfPastBlocksB\x0f\n\r_banned_until"\xb9\x05\n\x0eSpamStatistics\x12\x38\n\tproposals\x18\x01 \x01(\x0b\x32\x1a.vega.api.v1.SpamStatisticR\tproposals\x12<\n\x0b\x64\x65legations\x18\x02 \x01(\x0b\x32\x1a.vega.api.v1.SpamStatisticR\x0b\x64\x65legations\x12\x38\n\ttransfers\x18\x03 \x01(\x0b\x32\x1a.vega.api.v1.SpamStatisticR\ttransfers\x12I\n\x12node_announcements\x18\x04 \x01(\x0b\x32\x1a.vega.api.v1.SpamStatisticR\x11nodeAnnouncements\x12\x35\n\x05votes\x18\x05 \x01(\x0b\x32\x1f.vega.api.v1.VoteSpamStatisticsR\x05votes\x12+\n\x03pow\x18\x06 \x01(\x0b\x32\x19.vega.api.v1.PoWStatisticR\x03pow\x12\x45\n\x10issue_signatures\x18\x07 \x01(\x0b\x32\x1a.vega.api.v1.SpamStatisticR\x0fissueSignatures\x12\x1b\n\tepoch_seq\x18\x08 \x01(\x04R\x08\x65pochSeq\x12J\n\x13\x63reate_referral_set\x18\t \x01(\x0b\x32\x1a.vega.api.v1.SpamStatisticR\x11\x63reateReferralSet\x12J\n\x13update_referral_set\x18\n \x01(\x0b\x32\x1a.vega.api.v1.SpamStatisticR\x11updateReferralSet\x12J\n\x13\x61pply_referral_code\x18\x0b \x01(\x0b\x32\x1a.vega.api.v1.SpamStatisticR\x11\x61pplyReferralCode"s\n\x19GetSpamStatisticsResponse\x12\x19\n\x08\x63hain_id\x18\x01 \x01(\tR\x07\x63hainId\x12;\n\nstatistics\x18\x02 \x01(\x0b\x32\x1b.vega.api.v1.SpamStatisticsR\nstatistics2\xd8\x07\n\x0b\x43oreService\x12\x62\n\x11SubmitTransaction\x12%.vega.api.v1.SubmitTransactionRequest\x1a&.vega.api.v1.SubmitTransactionResponse\x12h\n\x13PropagateChainEvent\x12\'.vega.api.v1.PropagateChainEventRequest\x1a(.vega.api.v1.PropagateChainEventResponse\x12M\n\nStatistics\x12\x1e.vega.api.v1.StatisticsRequest\x1a\x1f.vega.api.v1.StatisticsResponse\x12\\\n\x0fLastBlockHeight\x12#.vega.api.v1.LastBlockHeightRequest\x1a$.vega.api.v1.LastBlockHeightResponse\x12P\n\x0bGetVegaTime\x12\x1f.vega.api.v1.GetVegaTimeRequest\x1a .vega.api.v1.GetVegaTimeResponse\x12`\n\x0fObserveEventBus\x12#.vega.api.v1.ObserveEventBusRequest\x1a$.vega.api.v1.ObserveEventBusResponse(\x01\x30\x01\x12k\n\x14SubmitRawTransaction\x12(.vega.api.v1.SubmitRawTransactionRequest\x1a).vega.api.v1.SubmitRawTransactionResponse\x12_\n\x10\x43heckTransaction\x12$.vega.api.v1.CheckTransactionRequest\x1a%.vega.api.v1.CheckTransactionResponse\x12h\n\x13\x43heckRawTransaction\x12\'.vega.api.v1.CheckRawTransactionRequest\x1a(.vega.api.v1.CheckRawTransactionResponse\x12\x62\n\x11GetSpamStatistics\x12%.vega.api.v1.GetSpamStatisticsRequest\x1a&.vega.api.v1.GetSpamStatisticsResponseBiZ,code.vegaprotocol.io/vega/protos/vega/api/v1\x92\x41\x38\x12\x1d\n\x0eVega core APIs2\x0bv0.76.0-dev\x1a\x13lb.testnet.vega.xyz*\x02\x01\x02\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "vega.api.v1.core_pb2", _globals
)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"Z,code.vegaprotocol.io/vega/protos/vega/api/v1\222A8\022\035\n\016Vega core APIs2\013v0.76.0-dev\032\023lb.testnet.vega.xyz*\002\001\002"
    )
    _globals["_PROPAGATECHAINEVENTREQUEST"].fields_by_name[
        "event"
    ]._loaded_options = None
    _globals["_PROPAGATECHAINEVENTREQUEST"].fields_by_name[
        "event"
    ]._serialized_options = b"\342A\001\002"
    _globals["_PROPAGATECHAINEVENTREQUEST"].fields_by_name[
        "pub_key"
    ]._loaded_options = None
    _globals["_PROPAGATECHAINEVENTREQUEST"].fields_by_name[
        "pub_key"
    ]._serialized_options = b"\342A\001\002"
    _globals["_PROPAGATECHAINEVENTREQUEST"].fields_by_name[
        "signature"
    ]._loaded_options = None
    _globals["_PROPAGATECHAINEVENTREQUEST"].fields_by_name[
        "signature"
    ]._serialized_options = b"\342A\001\002"
    _globals["_SUBMITTRANSACTIONREQUEST"].fields_by_name[
        "tx"
    ]._loaded_options = None
    _globals["_SUBMITTRANSACTIONREQUEST"].fields_by_name[
        "tx"
    ]._serialized_options = b"\342A\001\002"
    _globals["_SUBMITTRANSACTIONREQUEST"].fields_by_name[
        "type"
    ]._loaded_options = None
    _globals["_SUBMITTRANSACTIONREQUEST"].fields_by_name[
        "type"
    ]._serialized_options = b"\342A\001\002"
    _globals["_CHECKTRANSACTIONREQUEST"].fields_by_name[
        "tx"
    ]._loaded_options = None
    _globals["_CHECKTRANSACTIONREQUEST"].fields_by_name[
        "tx"
    ]._serialized_options = b"\342A\001\002"
    _globals["_SUBMITRAWTRANSACTIONREQUEST"].fields_by_name[
        "tx"
    ]._loaded_options = None
    _globals["_SUBMITRAWTRANSACTIONREQUEST"].fields_by_name[
        "tx"
    ]._serialized_options = b"\342A\001\002"
    _globals["_SUBMITRAWTRANSACTIONREQUEST"].fields_by_name[
        "type"
    ]._loaded_options = None
    _globals["_SUBMITRAWTRANSACTIONREQUEST"].fields_by_name[
        "type"
    ]._serialized_options = b"\342A\001\002"
    _globals["_CHECKRAWTRANSACTIONREQUEST"].fields_by_name[
        "tx"
    ]._loaded_options = None
    _globals["_CHECKRAWTRANSACTIONREQUEST"].fields_by_name[
        "tx"
    ]._serialized_options = b"\342A\001\002"
    _globals["_GETSPAMSTATISTICSREQUEST"].fields_by_name[
        "party_id"
    ]._loaded_options = None
    _globals["_GETSPAMSTATISTICSREQUEST"].fields_by_name[
        "party_id"
    ]._serialized_options = b"\342A\001\002"
    _globals["_PROPAGATECHAINEVENTREQUEST"]._serialized_start = 202
    _globals["_PROPAGATECHAINEVENTREQUEST"]._serialized_end = 325
    _globals["_PROPAGATECHAINEVENTRESPONSE"]._serialized_start = 327
    _globals["_PROPAGATECHAINEVENTRESPONSE"]._serialized_end = 382
    _globals["_SUBMITTRANSACTIONREQUEST"]._serialized_start = 385
    _globals["_SUBMITTRANSACTIONREQUEST"]._serialized_end = 612
    _globals["_SUBMITTRANSACTIONREQUEST_TYPE"]._serialized_start = 536
    _globals["_SUBMITTRANSACTIONREQUEST_TYPE"]._serialized_end = 612
    _globals["_SUBMITTRANSACTIONRESPONSE"]._serialized_start = 615
    _globals["_SUBMITTRANSACTIONRESPONSE"]._serialized_end = 775
    _globals["_CHECKTRANSACTIONREQUEST"]._serialized_start = 777
    _globals["_CHECKTRANSACTIONREQUEST"]._serialized_end = 855
    _globals["_CHECKTRANSACTIONRESPONSE"]._serialized_start = 858
    _globals["_CHECKTRANSACTIONRESPONSE"]._serialized_end = 1046
    _globals["_SUBMITRAWTRANSACTIONREQUEST"]._serialized_start = 1049
    _globals["_SUBMITRAWTRANSACTIONREQUEST"]._serialized_end = 1251
    _globals["_SUBMITRAWTRANSACTIONREQUEST_TYPE"]._serialized_start = 536
    _globals["_SUBMITRAWTRANSACTIONREQUEST_TYPE"]._serialized_end = 612
    _globals["_SUBMITRAWTRANSACTIONRESPONSE"]._serialized_start = 1254
    _globals["_SUBMITRAWTRANSACTIONRESPONSE"]._serialized_end = 1417
    _globals["_CHECKRAWTRANSACTIONREQUEST"]._serialized_start = 1419
    _globals["_CHECKRAWTRANSACTIONREQUEST"]._serialized_end = 1469
    _globals["_CHECKRAWTRANSACTIONRESPONSE"]._serialized_start = 1472
    _globals["_CHECKRAWTRANSACTIONRESPONSE"]._serialized_end = 1663
    _globals["_GETVEGATIMEREQUEST"]._serialized_start = 1665
    _globals["_GETVEGATIMEREQUEST"]._serialized_end = 1685
    _globals["_GETVEGATIMERESPONSE"]._serialized_start = 1687
    _globals["_GETVEGATIMERESPONSE"]._serialized_end = 1738
    _globals["_OBSERVEEVENTBUSREQUEST"]._serialized_start = 1741
    _globals["_OBSERVEEVENTBUSREQUEST"]._serialized_end = 1902
    _globals["_OBSERVEEVENTBUSRESPONSE"]._serialized_start = 1904
    _globals["_OBSERVEEVENTBUSRESPONSE"]._serialized_end = 1979
    _globals["_STATISTICSREQUEST"]._serialized_start = 1981
    _globals["_STATISTICSREQUEST"]._serialized_end = 2000
    _globals["_STATISTICSRESPONSE"]._serialized_start = 2002
    _globals["_STATISTICSRESPONSE"]._serialized_end = 2079
    _globals["_STATISTICS"]._serialized_start = 2082
    _globals["_STATISTICS"]._serialized_end = 3690
    _globals["_LASTBLOCKHEIGHTREQUEST"]._serialized_start = 3692
    _globals["_LASTBLOCKHEIGHTREQUEST"]._serialized_end = 3716
    _globals["_LASTBLOCKHEIGHTRESPONSE"]._serialized_start = 3719
    _globals["_LASTBLOCKHEIGHTRESPONSE"]._serialized_end = 4120
    _globals["_GETSPAMSTATISTICSREQUEST"]._serialized_start = 4122
    _globals["_GETSPAMSTATISTICSREQUEST"]._serialized_end = 4181
    _globals["_SPAMSTATISTIC"]._serialized_start = 4184
    _globals["_SPAMSTATISTIC"]._serialized_end = 4380
    _globals["_VOTESPAMSTATISTICS"]._serialized_start = 4383
    _globals["_VOTESPAMSTATISTICS"]._serialized_end = 4560
    _globals["_VOTESPAMSTATISTIC"]._serialized_start = 4563
    _globals["_VOTESPAMSTATISTIC"]._serialized_end = 4698
    _globals["_POWBLOCKSTATE"]._serialized_start = 4701
    _globals["_POWBLOCKSTATE"]._serialized_end = 5061
    _globals["_POWSTATISTIC"]._serialized_start = 5064
    _globals["_POWSTATISTIC"]._serialized_end = 5249
    _globals["_SPAMSTATISTICS"]._serialized_start = 5252
    _globals["_SPAMSTATISTICS"]._serialized_end = 5949
    _globals["_GETSPAMSTATISTICSRESPONSE"]._serialized_start = 5951
    _globals["_GETSPAMSTATISTICSRESPONSE"]._serialized_end = 6066
    _globals["_CORESERVICE"]._serialized_start = 6069
    _globals["_CORESERVICE"]._serialized_end = 7053
# @@protoc_insertion_point(module_scope)
