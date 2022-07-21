# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pymsd/proto/schema.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pymsd.proto import dataframe_pb2 as pymsd_dot_proto_dot_dataframe__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18pymsd/proto/schema.proto\x12\x06schema\x1a\x1bpymsd/proto/dataframe.proto\"\x86\x01\n\x08OpParams\x12\x16\n\tsrc_field\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nsrc_schema\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1a\n\rtrigger_field\x18\x04 \x01(\tH\x02\x88\x01\x01\x42\x0c\n\n_src_fieldB\r\n\x0b_src_schemaB\x10\n\x0e_trigger_field\"\xc9\x01\n\x05\x46ield\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x05\x64type\x18\x02 \x01(\x0e\x32\x14.dataframe.FieldKind\x12\r\n\x05refer\x18\x03 \x01(\r\x12\x1b\n\x02op\x18\x04 \x01(\x0e\x32\x0f.schema.FieldOp\x12\r\n\x05paste\x18\x05 \x01(\x08\x12\x11\n\x04\x65xpr\x18\x06 \x01(\tH\x00\x88\x01\x01\x12(\n\top_params\x18\x07 \x01(\x0b\x32\x10.schema.OpParamsH\x01\x88\x01\x01\x42\x07\n\x05_exprB\x0c\n\n_op_params\"\xa0\x02\n\x06Schema\x12\x0e\n\x06pk_col\x18\x01 \x01(\x05\x12\x1d\n\x06\x66ields\x18\x02 \x03(\x0b\x32\r.schema.Field\x12\x1a\n\x12max_rows_per_block\x18\x03 \x01(\r\x12\x1a\n\x12max_rows_in_memory\x18\x04 \x01(\r\x12\x0e\n\x06\x63hains\x18\x05 \x03(\t\x12\x19\n\x0c\x64istinct_col\x18\x06 \x01(\x05H\x00\x88\x01\x01\x12\x10\n\x03ttl\x18\x07 \x01(\rH\x01\x88\x01\x01\x12*\n\x06\x61\x64\x64ons\x18\x64 \x03(\x0b\x32\x1a.schema.Schema.AddonsEntry\x1a-\n\x0b\x41\x64\x64onsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0f\n\r_distinct_colB\x06\n\x04_ttl*\x87\x01\n\x07\x46ieldOp\x12\x08\n\x04Save\x10\x00\x12\r\n\tSaveFirst\x10\x01\x12\x0b\n\x07SaveMax\x10\x02\x12\x0b\n\x07SaveMin\x10\x03\x12\x07\n\x03Inc\x10\x04\x12\x0f\n\x0b\x44iffPrevios\x10\x05\x12\r\n\tDiffFirst\x10\x06\x12\t\n\x05\x43ount\x10\x07\x12\x07\n\x03\x41vg\x10\x08\x12\x0c\n\x08\x44istinct\x10\tb\x06proto3')

_FIELDOP = DESCRIPTOR.enum_types_by_name['FieldOp']
FieldOp = enum_type_wrapper.EnumTypeWrapper(_FIELDOP)
Save = 0
SaveFirst = 1
SaveMax = 2
SaveMin = 3
Inc = 4
DiffPrevios = 5
DiffFirst = 6
Count = 7
Avg = 8
Distinct = 9


_OPPARAMS = DESCRIPTOR.message_types_by_name['OpParams']
_FIELD = DESCRIPTOR.message_types_by_name['Field']
_SCHEMA = DESCRIPTOR.message_types_by_name['Schema']
_SCHEMA_ADDONSENTRY = _SCHEMA.nested_types_by_name['AddonsEntry']
OpParams = _reflection.GeneratedProtocolMessageType('OpParams', (_message.Message,), {
  'DESCRIPTOR' : _OPPARAMS,
  '__module__' : 'pymsd.proto.schema_pb2'
  # @@protoc_insertion_point(class_scope:schema.OpParams)
  })
_sym_db.RegisterMessage(OpParams)

Field = _reflection.GeneratedProtocolMessageType('Field', (_message.Message,), {
  'DESCRIPTOR' : _FIELD,
  '__module__' : 'pymsd.proto.schema_pb2'
  # @@protoc_insertion_point(class_scope:schema.Field)
  })
_sym_db.RegisterMessage(Field)

Schema = _reflection.GeneratedProtocolMessageType('Schema', (_message.Message,), {

  'AddonsEntry' : _reflection.GeneratedProtocolMessageType('AddonsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SCHEMA_ADDONSENTRY,
    '__module__' : 'pymsd.proto.schema_pb2'
    # @@protoc_insertion_point(class_scope:schema.Schema.AddonsEntry)
    })
  ,
  'DESCRIPTOR' : _SCHEMA,
  '__module__' : 'pymsd.proto.schema_pb2'
  # @@protoc_insertion_point(class_scope:schema.Schema)
  })
_sym_db.RegisterMessage(Schema)
_sym_db.RegisterMessage(Schema.AddonsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SCHEMA_ADDONSENTRY._options = None
  _SCHEMA_ADDONSENTRY._serialized_options = b'8\001'
  _FIELDOP._serialized_start=698
  _FIELDOP._serialized_end=833
  _OPPARAMS._serialized_start=66
  _OPPARAMS._serialized_end=200
  _FIELD._serialized_start=203
  _FIELD._serialized_end=404
  _SCHEMA._serialized_start=407
  _SCHEMA._serialized_end=695
  _SCHEMA_ADDONSENTRY._serialized_start=625
  _SCHEMA_ADDONSENTRY._serialized_end=670
# @@protoc_insertion_point(module_scope)
