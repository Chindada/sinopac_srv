# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trade_bot_protobuf/src/sinopac.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$trade_bot_protobuf/src/sinopac.proto\x12\x10sinopac_protobuf\"\xa7\x02\n\x0b\x42idAskProto\x12\x10\n\x08\x65xchange\x18\x01 \x01(\t\x12\x39\n\x07\x62id_ask\x18\x02 \x01(\x0b\x32(.sinopac_protobuf.BidAskProto.BidAskData\x1a\xca\x01\n\nBidAskData\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x11\n\tdate_time\x18\x02 \x01(\t\x12\x11\n\tbid_price\x18\x03 \x03(\x01\x12\x12\n\nbid_volume\x18\x04 \x03(\x03\x12\x14\n\x0c\x64iff_bid_vol\x18\x05 \x03(\x03\x12\x11\n\task_price\x18\x06 \x03(\x01\x12\x12\n\nask_volume\x18\x07 \x03(\x03\x12\x14\n\x0c\x64iff_ask_vol\x18\x08 \x03(\x03\x12\x0f\n\x07suspend\x18\t \x01(\x03\x12\x10\n\x08simtrade\x18\n \x01(\x03\"E\n\x12\x45ntireTickArrProto\x12/\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32!.sinopac_protobuf.EntireTickProto\"\x9d\x01\n\x0f\x45ntireTickProto\x12\n\n\x02ts\x18\x01 \x01(\x03\x12\r\n\x05\x63lose\x18\x02 \x01(\x01\x12\x0e\n\x06volume\x18\x03 \x01(\x03\x12\x11\n\tbid_price\x18\x04 \x01(\x01\x12\x12\n\nbid_volume\x18\x05 \x01(\x03\x12\x11\n\task_price\x18\x06 \x01(\x01\x12\x12\n\nask_volume\x18\x07 \x01(\x03\x12\x11\n\ttick_type\x18\x08 \x01(\x03\"9\n\x0cKbarArrProto\x12)\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1b.sinopac_protobuf.KbarProto\"_\n\tKbarProto\x12\n\n\x02ts\x18\x01 \x01(\x03\x12\r\n\x05\x43lose\x18\x02 \x01(\x01\x12\x0c\n\x04Open\x18\x03 \x01(\x01\x12\x0c\n\x04High\x18\x04 \x01(\x01\x12\x0b\n\x03Low\x18\x05 \x01(\x01\x12\x0e\n\x06Volume\x18\x06 \x01(\x03\"A\n\x10SnapShotArrProto\x12-\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1f.sinopac_protobuf.SnapShotProto\"\xa9\x03\n\rSnapShotProto\x12\n\n\x02ts\x18\x01 \x01(\x03\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x10\n\x08\x65xchange\x18\x03 \x01(\t\x12\x0c\n\x04open\x18\x04 \x01(\x01\x12\x0c\n\x04high\x18\x05 \x01(\x01\x12\x0b\n\x03low\x18\x06 \x01(\x01\x12\r\n\x05\x63lose\x18\x07 \x01(\x01\x12\x11\n\ttick_type\x18\x08 \x01(\t\x12\x14\n\x0c\x63hange_price\x18\t \x01(\x01\x12\x13\n\x0b\x63hange_rate\x18\n \x01(\x01\x12\x13\n\x0b\x63hange_type\x18\x0b \x01(\t\x12\x15\n\raverage_price\x18\x0c \x01(\x01\x12\x0e\n\x06volume\x18\r \x01(\x03\x12\x14\n\x0ctotal_volume\x18\x0e \x01(\x03\x12\x0e\n\x06\x61mount\x18\x0f \x01(\x03\x12\x14\n\x0ctotal_amount\x18\x10 \x01(\x03\x12\x18\n\x10yesterday_volume\x18\x11 \x01(\x01\x12\x11\n\tbuy_price\x18\x12 \x01(\x01\x12\x12\n\nbuy_volume\x18\x13 \x01(\x01\x12\x12\n\nsell_price\x18\x14 \x01(\x01\x12\x13\n\x0bsell_volume\x18\x15 \x01(\x03\x12\x14\n\x0cvolume_ratio\x18\x16 \x01(\x01\"\xfe\x03\n\x0fStreamTickProto\x12\x10\n\x08\x65xchange\x18\x01 \x01(\t\x12\x38\n\x04tick\x18\x02 \x01(\x0b\x32*.sinopac_protobuf.StreamTickProto.TickData\x1a\x9e\x03\n\x08TickData\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x11\n\tdate_time\x18\x02 \x01(\t\x12\x0c\n\x04open\x18\x03 \x01(\x01\x12\x11\n\tavg_price\x18\x04 \x01(\x01\x12\r\n\x05\x63lose\x18\x05 \x01(\x01\x12\x0c\n\x04high\x18\x06 \x01(\x01\x12\x0b\n\x03low\x18\x07 \x01(\x01\x12\x0e\n\x06\x61mount\x18\x08 \x01(\x01\x12\x14\n\x0ctotal_amount\x18\t \x01(\x01\x12\x0e\n\x06volume\x18\n \x01(\x03\x12\x14\n\x0ctotal_volume\x18\x0b \x01(\x03\x12\x11\n\ttick_type\x18\x0c \x01(\x03\x12\x10\n\x08\x63hg_type\x18\r \x01(\x03\x12\x11\n\tprice_chg\x18\x0e \x01(\x01\x12\x0f\n\x07pct_chg\x18\x0f \x01(\x01\x12\x1a\n\x12\x62id_side_total_vol\x18\x10 \x01(\x03\x12\x1a\n\x12\x61sk_side_total_vol\x18\x11 \x01(\x03\x12\x1a\n\x12\x62id_side_total_cnt\x18\x12 \x01(\x03\x12\x1a\n\x12\x61sk_side_total_cnt\x18\x13 \x01(\x03\x12\x0f\n\x07suspend\x18\x14 \x01(\x03\x12\x10\n\x08simtrade\x18\x15 \x01(\x03\"P\n\nEventProto\x12\x11\n\tresp_code\x18\x01 \x01(\x03\x12\x12\n\nevent_code\x18\x02 \x01(\x03\x12\x0c\n\x04info\x18\x03 \x01(\t\x12\r\n\x05\x65vent\x18\x04 \x01(\t\"G\n\x13TradeRecordArrProto\x12\x30\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\".sinopac_protobuf.TradeRecordProto\"\x81\x01\n\x10TradeRecordProto\x12\x10\n\x08quantity\x18\x01 \x01(\x03\x12\r\n\x05price\x18\x02 \x01(\x01\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\x12\x0c\n\x04\x63ode\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\x12\x12\n\norder_time\x18\x06 \x01(\t\x12\x0e\n\x06status\x18\x07 \x01(\t\"E\n\x12VolumeRankArrProto\x12/\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32!.sinopac_protobuf.VolumeRankProto\"\x87\x04\n\x0fVolumeRankProto\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\n\n\x02ts\x18\x04 \x01(\x03\x12\x0c\n\x04open\x18\x05 \x01(\x01\x12\x0c\n\x04high\x18\x06 \x01(\x01\x12\x0b\n\x03low\x18\x07 \x01(\x01\x12\r\n\x05\x63lose\x18\x08 \x01(\x01\x12\x13\n\x0bprice_range\x18\t \x01(\x01\x12\x11\n\ttick_type\x18\n \x01(\x03\x12\x14\n\x0c\x63hange_price\x18\x0b \x01(\x01\x12\x13\n\x0b\x63hange_type\x18\x0c \x01(\x03\x12\x15\n\raverage_price\x18\r \x01(\x01\x12\x0e\n\x06volume\x18\x0e \x01(\x03\x12\x14\n\x0ctotal_volume\x18\x0f \x01(\x03\x12\x0e\n\x06\x61mount\x18\x10 \x01(\x03\x12\x14\n\x0ctotal_amount\x18\x11 \x01(\x03\x12\x18\n\x10yesterday_volume\x18\x12 \x01(\x03\x12\x14\n\x0cvolume_ratio\x18\x13 \x01(\x01\x12\x11\n\tbuy_price\x18\x14 \x01(\x01\x12\x12\n\nbuy_volume\x18\x15 \x01(\x03\x12\x12\n\nsell_price\x18\x16 \x01(\x01\x12\x13\n\x0bsell_volume\x18\x17 \x01(\x03\x12\x12\n\nbid_orders\x18\x18 \x01(\x03\x12\x13\n\x0b\x62id_volumes\x18\x19 \x01(\x03\x12\x12\n\nask_orders\x18\x1a \x01(\x03\x12\x13\n\x0b\x61sk_volumes\x18\x1b \x01(\x03\x42\x10Z\x0epkg/sinopacapib\x06proto3')



_BIDASKPROTO = DESCRIPTOR.message_types_by_name['BidAskProto']
_BIDASKPROTO_BIDASKDATA = _BIDASKPROTO.nested_types_by_name['BidAskData']
_ENTIRETICKARRPROTO = DESCRIPTOR.message_types_by_name['EntireTickArrProto']
_ENTIRETICKPROTO = DESCRIPTOR.message_types_by_name['EntireTickProto']
_KBARARRPROTO = DESCRIPTOR.message_types_by_name['KbarArrProto']
_KBARPROTO = DESCRIPTOR.message_types_by_name['KbarProto']
_SNAPSHOTARRPROTO = DESCRIPTOR.message_types_by_name['SnapShotArrProto']
_SNAPSHOTPROTO = DESCRIPTOR.message_types_by_name['SnapShotProto']
_STREAMTICKPROTO = DESCRIPTOR.message_types_by_name['StreamTickProto']
_STREAMTICKPROTO_TICKDATA = _STREAMTICKPROTO.nested_types_by_name['TickData']
_EVENTPROTO = DESCRIPTOR.message_types_by_name['EventProto']
_TRADERECORDARRPROTO = DESCRIPTOR.message_types_by_name['TradeRecordArrProto']
_TRADERECORDPROTO = DESCRIPTOR.message_types_by_name['TradeRecordProto']
_VOLUMERANKARRPROTO = DESCRIPTOR.message_types_by_name['VolumeRankArrProto']
_VOLUMERANKPROTO = DESCRIPTOR.message_types_by_name['VolumeRankProto']
BidAskProto = _reflection.GeneratedProtocolMessageType('BidAskProto', (_message.Message,), {

  'BidAskData' : _reflection.GeneratedProtocolMessageType('BidAskData', (_message.Message,), {
    'DESCRIPTOR' : _BIDASKPROTO_BIDASKDATA,
    '__module__' : 'trade_bot_protobuf.src.sinopac_pb2'
    # @@protoc_insertion_point(class_scope:sinopac_protobuf.BidAskProto.BidAskData)
    })
  ,
  'DESCRIPTOR' : _BIDASKPROTO,
  '__module__' : 'trade_bot_protobuf.src.sinopac_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_protobuf.BidAskProto)
  })
_sym_db.RegisterMessage(BidAskProto)
_sym_db.RegisterMessage(BidAskProto.BidAskData)

EntireTickArrProto = _reflection.GeneratedProtocolMessageType('EntireTickArrProto', (_message.Message,), {
  'DESCRIPTOR' : _ENTIRETICKARRPROTO,
  '__module__' : 'trade_bot_protobuf.src.sinopac_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_protobuf.EntireTickArrProto)
  })
_sym_db.RegisterMessage(EntireTickArrProto)

EntireTickProto = _reflection.GeneratedProtocolMessageType('EntireTickProto', (_message.Message,), {
  'DESCRIPTOR' : _ENTIRETICKPROTO,
  '__module__' : 'trade_bot_protobuf.src.sinopac_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_protobuf.EntireTickProto)
  })
_sym_db.RegisterMessage(EntireTickProto)

KbarArrProto = _reflection.GeneratedProtocolMessageType('KbarArrProto', (_message.Message,), {
  'DESCRIPTOR' : _KBARARRPROTO,
  '__module__' : 'trade_bot_protobuf.src.sinopac_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_protobuf.KbarArrProto)
  })
_sym_db.RegisterMessage(KbarArrProto)

KbarProto = _reflection.GeneratedProtocolMessageType('KbarProto', (_message.Message,), {
  'DESCRIPTOR' : _KBARPROTO,
  '__module__' : 'trade_bot_protobuf.src.sinopac_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_protobuf.KbarProto)
  })
_sym_db.RegisterMessage(KbarProto)

SnapShotArrProto = _reflection.GeneratedProtocolMessageType('SnapShotArrProto', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTARRPROTO,
  '__module__' : 'trade_bot_protobuf.src.sinopac_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_protobuf.SnapShotArrProto)
  })
_sym_db.RegisterMessage(SnapShotArrProto)

SnapShotProto = _reflection.GeneratedProtocolMessageType('SnapShotProto', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTPROTO,
  '__module__' : 'trade_bot_protobuf.src.sinopac_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_protobuf.SnapShotProto)
  })
_sym_db.RegisterMessage(SnapShotProto)

StreamTickProto = _reflection.GeneratedProtocolMessageType('StreamTickProto', (_message.Message,), {

  'TickData' : _reflection.GeneratedProtocolMessageType('TickData', (_message.Message,), {
    'DESCRIPTOR' : _STREAMTICKPROTO_TICKDATA,
    '__module__' : 'trade_bot_protobuf.src.sinopac_pb2'
    # @@protoc_insertion_point(class_scope:sinopac_protobuf.StreamTickProto.TickData)
    })
  ,
  'DESCRIPTOR' : _STREAMTICKPROTO,
  '__module__' : 'trade_bot_protobuf.src.sinopac_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_protobuf.StreamTickProto)
  })
_sym_db.RegisterMessage(StreamTickProto)
_sym_db.RegisterMessage(StreamTickProto.TickData)

EventProto = _reflection.GeneratedProtocolMessageType('EventProto', (_message.Message,), {
  'DESCRIPTOR' : _EVENTPROTO,
  '__module__' : 'trade_bot_protobuf.src.sinopac_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_protobuf.EventProto)
  })
_sym_db.RegisterMessage(EventProto)

TradeRecordArrProto = _reflection.GeneratedProtocolMessageType('TradeRecordArrProto', (_message.Message,), {
  'DESCRIPTOR' : _TRADERECORDARRPROTO,
  '__module__' : 'trade_bot_protobuf.src.sinopac_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_protobuf.TradeRecordArrProto)
  })
_sym_db.RegisterMessage(TradeRecordArrProto)

TradeRecordProto = _reflection.GeneratedProtocolMessageType('TradeRecordProto', (_message.Message,), {
  'DESCRIPTOR' : _TRADERECORDPROTO,
  '__module__' : 'trade_bot_protobuf.src.sinopac_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_protobuf.TradeRecordProto)
  })
_sym_db.RegisterMessage(TradeRecordProto)

VolumeRankArrProto = _reflection.GeneratedProtocolMessageType('VolumeRankArrProto', (_message.Message,), {
  'DESCRIPTOR' : _VOLUMERANKARRPROTO,
  '__module__' : 'trade_bot_protobuf.src.sinopac_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_protobuf.VolumeRankArrProto)
  })
_sym_db.RegisterMessage(VolumeRankArrProto)

VolumeRankProto = _reflection.GeneratedProtocolMessageType('VolumeRankProto', (_message.Message,), {
  'DESCRIPTOR' : _VOLUMERANKPROTO,
  '__module__' : 'trade_bot_protobuf.src.sinopac_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_protobuf.VolumeRankProto)
  })
_sym_db.RegisterMessage(VolumeRankProto)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\016pkg/sinopacapi'
  _BIDASKPROTO._serialized_start=59
  _BIDASKPROTO._serialized_end=354
  _BIDASKPROTO_BIDASKDATA._serialized_start=152
  _BIDASKPROTO_BIDASKDATA._serialized_end=354
  _ENTIRETICKARRPROTO._serialized_start=356
  _ENTIRETICKARRPROTO._serialized_end=425
  _ENTIRETICKPROTO._serialized_start=428
  _ENTIRETICKPROTO._serialized_end=585
  _KBARARRPROTO._serialized_start=587
  _KBARARRPROTO._serialized_end=644
  _KBARPROTO._serialized_start=646
  _KBARPROTO._serialized_end=741
  _SNAPSHOTARRPROTO._serialized_start=743
  _SNAPSHOTARRPROTO._serialized_end=808
  _SNAPSHOTPROTO._serialized_start=811
  _SNAPSHOTPROTO._serialized_end=1236
  _STREAMTICKPROTO._serialized_start=1239
  _STREAMTICKPROTO._serialized_end=1749
  _STREAMTICKPROTO_TICKDATA._serialized_start=1335
  _STREAMTICKPROTO_TICKDATA._serialized_end=1749
  _EVENTPROTO._serialized_start=1751
  _EVENTPROTO._serialized_end=1831
  _TRADERECORDARRPROTO._serialized_start=1833
  _TRADERECORDARRPROTO._serialized_end=1904
  _TRADERECORDPROTO._serialized_start=1907
  _TRADERECORDPROTO._serialized_end=2036
  _VOLUMERANKARRPROTO._serialized_start=2038
  _VOLUMERANKARRPROTO._serialized_end=2107
  _VOLUMERANKPROTO._serialized_start=2110
  _VOLUMERANKPROTO._serialized_end=2629
# @@protoc_insertion_point(module_scope)
