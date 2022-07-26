# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pymsd/proto/dataframe.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bpymsd/proto/dataframe.proto\x12\tdataframe\"Y\n\x06Series\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x05\x64type\x18\x02 \x01(\x0e\x32\x14.dataframe.FieldKind\x12\r\n\x05\x64\x61tas\x18\x0f \x01(\x0c\x12\r\n\x05texts\x18\x10 \x03(\t\"k\n\tDataFrame\x12\x0e\n\x06pk_col\x18\x01 \x01(\x05\x12\x19\n\x0c\x64istinct_col\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\"\n\x07\x63olumns\x18\x0f \x03(\x0b\x32\x11.dataframe.SeriesB\x0f\n\r_distinct_col\"@\n\x13\x44\x61taFrameIndexBlock\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0c\n\x04stop\x18\x02 \x01(\x03\x12\x0c\n\x04rows\x18\x03 \x01(\r\"\xa9\x01\n\x0e\x44\x61taFrameIndex\x12\x12\n\ntotal_rows\x18\x01 \x01(\r\x12\x1a\n\x12max_rows_per_block\x18\x02 \x01(\r\x12\x1a\n\x12max_rows_in_memory\x18\x05 \x01(\r\x12\r\n\x05start\x18\x03 \x01(\x03\x12\x0c\n\x04stop\x18\x04 \x01(\x03\x12.\n\x06\x62locks\x18\n \x03(\x0b\x32\x1e.dataframe.DataFrameIndexBlock*|\n\tFieldKind\x12\t\n\x05\x45mpty\x10\x00\x12\x0b\n\x05Int64\x10\x80\x80\x18\x12\x0e\n\x08\x44\x61teTime\x10\x81\x80\x18\x12\x0f\n\tDecimal64\x10\x82\x80\x18\x12\x0c\n\x06UInt64\x10\x83\x80\x18\x12\x0b\n\x05UInt8\x10\x81\x80 \x12\r\n\x07\x46loat64\x10\x80\x80\x38\x12\x0c\n\x06String\x10\x80\x80@b\x06proto3')

_FIELDKIND = DESCRIPTOR.enum_types_by_name['FieldKind']
FieldKind = enum_type_wrapper.EnumTypeWrapper(_FIELDKIND)
Empty = 0
Int64 = 393216
DateTime = 393217
Decimal64 = 393218
UInt64 = 393219
UInt8 = 524289
Float64 = 917504
String = 1048576


_SERIES = DESCRIPTOR.message_types_by_name['Series']
_DATAFRAME = DESCRIPTOR.message_types_by_name['DataFrame']
_DATAFRAMEINDEXBLOCK = DESCRIPTOR.message_types_by_name['DataFrameIndexBlock']
_DATAFRAMEINDEX = DESCRIPTOR.message_types_by_name['DataFrameIndex']
Series = _reflection.GeneratedProtocolMessageType('Series', (_message.Message,), {
  'DESCRIPTOR' : _SERIES,
  '__module__' : 'pymsd.proto.dataframe_pb2'
  # @@protoc_insertion_point(class_scope:dataframe.Series)
  })
_sym_db.RegisterMessage(Series)

DataFrame = _reflection.GeneratedProtocolMessageType('DataFrame', (_message.Message,), {
  'DESCRIPTOR' : _DATAFRAME,
  '__module__' : 'pymsd.proto.dataframe_pb2'
  # @@protoc_insertion_point(class_scope:dataframe.DataFrame)
  })
_sym_db.RegisterMessage(DataFrame)

DataFrameIndexBlock = _reflection.GeneratedProtocolMessageType('DataFrameIndexBlock', (_message.Message,), {
  'DESCRIPTOR' : _DATAFRAMEINDEXBLOCK,
  '__module__' : 'pymsd.proto.dataframe_pb2'
  # @@protoc_insertion_point(class_scope:dataframe.DataFrameIndexBlock)
  })
_sym_db.RegisterMessage(DataFrameIndexBlock)

DataFrameIndex = _reflection.GeneratedProtocolMessageType('DataFrameIndex', (_message.Message,), {
  'DESCRIPTOR' : _DATAFRAMEINDEX,
  '__module__' : 'pymsd.proto.dataframe_pb2'
  # @@protoc_insertion_point(class_scope:dataframe.DataFrameIndex)
  })
_sym_db.RegisterMessage(DataFrameIndex)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FIELDKIND._serialized_start=480
  _FIELDKIND._serialized_end=604
  _SERIES._serialized_start=42
  _SERIES._serialized_end=131
  _DATAFRAME._serialized_start=133
  _DATAFRAME._serialized_end=240
  _DATAFRAMEINDEXBLOCK._serialized_start=242
  _DATAFRAMEINDEXBLOCK._serialized_end=306
  _DATAFRAMEINDEX._serialized_start=309
  _DATAFRAMEINDEX._serialized_end=478
# @@protoc_insertion_point(module_scope)
