# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pymsd/proto/apiv1.proto
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
from pymsd.proto import schema_pb2 as pymsd_dot_proto_dot_schema__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17pymsd/proto/apiv1.proto\x12\x05\x61piv1\x1a\x1bpymsd/proto/dataframe.proto\x1a\x18pymsd/proto/schema.proto\"\xc9\x01\n\tGetParams\x12\x0b\n\x03obj\x18\x01 \x01(\t\x12\r\n\x05\x64kind\x18\x02 \x01(\t\x12\x0e\n\x06\x66ields\x18\x03 \x03(\t\x12\x12\n\nstart_date\x18\x04 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x05 \x01(\t\x12\x0e\n\x06offest\x18\x06 \x01(\x05\x12\r\n\x05limit\x18\x07 \x01(\x05\x12\x11\n\tascending\x18\x08 \x01(\x08\x12\x0b\n\x03ids\x18\t \x03(\t\x12\x0e\n\x06idname\x18\n \x01(\t\x12\x1b\n\x13\x61\x64\x64tional_where_ast\x18\x0b \x01(\t\"\xab\x01\n\x13GetDataFrameRequest\x12 \n\x06params\x18\x01 \x01(\x0b\x32\x10.apiv1.GetParams\x12\x0b\n\x03sql\x18\x02 \x01(\t\x12\x36\n\x06\x61\x64\x64ons\x18\x64 \x03(\x0b\x32&.apiv1.GetDataFrameRequest.AddonsEntry\x1a-\n\x0b\x41\x64\x64onsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc2\x01\n\x14GetDataFrameResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0e\n\x06messge\x18\x02 \x01(\t\x12$\n\x06values\x18\x03 \x01(\x0b\x32\x14.dataframe.DataFrame\x12\x37\n\x06\x61\x64\x64ons\x18\x64 \x03(\x0b\x32\'.apiv1.GetDataFrameResponse.AddonsEntry\x1a-\n\x0b\x41\x64\x64onsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"=\n\x0fUpdateRowBinary\x12\x0c\n\x04rows\x18\x01 \x01(\x05\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"\xd2\x02\n\tCsvOption\x12\x0f\n\x07\x63sv_sep\x18\x01 \x01(\x05\x12\x13\n\x0bskip_head_n\x18\x02 \x01(\x05\x12\x13\n\x0bskip_tail_n\x18\x03 \x01(\x05\x12\x14\n\x0cskip_prefies\x18\x04 \x03(\t\x12\x1e\n\x16\x63sv_additation_row_sep\x18\x05 \x01(\x0c\x12\x1c\n\x14\x63sv_fixed_col_offset\x18\x06 \x03(\x05\x12\x17\n\x0f\x63sv_col_mapping\x18\x07 \x03(\x05\x12N\n\x19\x63sv_col_mapping_by_prefix\x18\x08 \x03(\x0b\x32+.apiv1.CsvOption.CsvColMappingByPrefixEntry\x12\x0f\n\x07obj_col\x18\t \x01(\x05\x1a<\n\x1a\x43svColMappingByPrefixEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1c\n\x0cScriptOption\x12\x0c\n\x04name\x18\x01 \x01(\t\"}\n\x0fUpdateRowOption\x12&\n\x06\x66ormat\x18\x01 \x01(\x0e\x32\x16.apiv1.UpdateRowFormat\x12\x1d\n\x03\x63sv\x18\x02 \x01(\x0b\x32\x10.apiv1.CsvOption\x12#\n\x06script\x18\x03 \x01(\x0b\x32\x13.apiv1.ScriptOption\"\xaf\x01\n\x16UpdateDataFrameRequest\x12\x0b\n\x03obj\x18\x01 \x01(\t\x12\r\n\x05\x64kind\x18\x02 \x01(\t\x12\x0c\n\x04rows\x18\x03 \x01(\x0c\x12\x1f\n\x04mode\x18\x04 \x01(\x0e\x32\x11.apiv1.UpdateMode\x12*\n\nrowsOption\x18\x05 \x01(\x0b\x32\x16.apiv1.UpdateRowOption\x12\x13\n\x06source\x18\x06 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_source\"M\n\x17UpdateDataFrameResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0e\n\x06messge\x18\x02 \x01(\t\x12\x14\n\x0cupdated_rows\x18\x03 \x01(\x05\"N\n\x11UpdateMetaRequest\x12\r\n\x05idkey\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\x12\x0c\n\x04json\x18\x03 \x01(\t\x12\r\n\x05jsonb\x18\x04 \x01(\x0c\"2\n\x12UpdateMetaResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0e\n\x06messge\x18\x02 \x01(\t\"N\n\x06\x46ilter\x12\x0f\n\x07keyword\x18\x01 \x01(\t\x12\x1f\n\x04mode\x18\x02 \x01(\x0e\x32\x11.apiv1.FilterMode\x12\x12\n\nignoreCase\x18\x03 \x01(\x08\"4\n\x0fGetTableRequest\x12!\n\nnameFilter\x18\x01 \x01(\x0b\x32\r.apiv1.Filter\"\xa7\x01\n\x10GetTableResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0e\n\x06messge\x18\x02 \x01(\t\x12\x35\n\x07schemas\x18\x03 \x03(\x0b\x32$.apiv1.GetTableResponse.SchemasEntry\x1a>\n\x0cSchemasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.schema.Schema:\x02\x38\x01\"^\n\x11ListObjectRequest\x12\r\n\x05\x64kind\x18\x01 \x01(\t\x12 \n\tobjFilter\x18\x02 \x01(\x0b\x32\r.apiv1.Filter\x12\x10\n\x03sql\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x06\n\x04_sql\"\xb5\x02\n\x12ListObjectResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0e\n\x06messge\x18\x02 \x01(\t\x12\x37\n\x07objects\x18\x03 \x03(\x0b\x32&.apiv1.ListObjectResponse.ObjectsEntry\x12\x37\n\x07records\x18\x04 \x03(\x0b\x32&.apiv1.ListObjectResponse.RecordsEntry\x1aI\n\x0cObjectsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.dataframe.DataFrameIndex:\x02\x38\x01\x1a\x44\n\x0cRecordsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.dataframe.DataFrame:\x02\x38\x01\"\x86\x01\n\x0c\x42inlogRecord\x12\n\n\x02ts\x18\x01 \x01(\x03\x12(\n\x04Meta\x18\x05 \x01(\x0b\x32\x18.apiv1.UpdateMetaRequestH\x00\x12\x32\n\tDataFrame\x18\x06 \x01(\x0b\x32\x1d.apiv1.UpdateDataFrameRequestH\x00\x42\x0c\n\nanyRequest\"k\n\x0e\x46orwardRequest\x12#\n\toperation\x18\x01 \x01(\x0e\x32\x10.apiv1.ForwardOp\x12\x0e\n\x06target\x18\x02 \x01(\t\x12\x16\n\tstartDate\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0c\n\n_startDate\"\x1f\n\rForwardDetail\x12\x0e\n\x06lastTs\x18\x01 \x01(\x03\"\xae\x01\n\x0f\x46orwardResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0e\n\x06messge\x18\x02 \x01(\t\x12\x36\n\x08\x66orwards\x18\n \x03(\x0b\x32$.apiv1.ForwardResponse.ForwardsEntry\x1a\x45\n\rForwardsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.apiv1.ForwardDetail:\x02\x38\x01*r\n\nUpdateMode\x12\n\n\x06Schema\x10\x00\x12\n\n\x06Import\x10\x01\x12\t\n\x05Paste\x10\x02\x12\x0e\n\nBulkSchema\x10\x03\x12\x0e\n\nBulkImport\x10\x04\x12\t\n\x05\x43hain\x10\x05\x12\n\n\x06Modify\x10\x06\x12\n\n\x06Script\x10\x07*G\n\x0fUpdateRowFormat\x12\x07\n\x03\x43sv\x10\x00\x12\n\n\x06\x42inary\x10\x01\x12\x0f\n\x0bJsonRecords\x10\x02\x12\x0e\n\nJsonValues\x10\x03*5\n\nFilterMode\x12\x08\n\x04\x46ull\x10\x00\x12\x08\n\x04Part\x10\x01\x12\x08\n\x04Glob\x10\x02\x12\t\n\x05Regex\x10\x03*@\n\tForwardOp\x12\x10\n\x0cStartForward\x10\x00\x12\x0f\n\x0bStopForward\x10\x01\x12\x10\n\x0cListForwards\x10\x02\x32\xa6\x03\n\x10\x44\x61taFrameService\x12@\n\x03Get\x12\x1a.apiv1.GetDataFrameRequest\x1a\x1b.apiv1.GetDataFrameResponse\"\x00\x12\x43\n\nListObject\x12\x18.apiv1.ListObjectRequest\x1a\x19.apiv1.ListObjectResponse\"\x00\x12K\n\x06Update\x12\x1d.apiv1.UpdateDataFrameRequest\x1a\x1e.apiv1.UpdateDataFrameResponse\"\x00(\x01\x12=\n\x08GetTable\x12\x16.apiv1.GetTableRequest\x1a\x17.apiv1.GetTableResponse\"\x00\x12\x43\n\nUpdateMeta\x12\x18.apiv1.UpdateMetaRequest\x1a\x19.apiv1.UpdateMetaResponse\"\x00\x12:\n\x07\x46orward\x12\x15.apiv1.ForwardRequest\x1a\x16.apiv1.ForwardResponse\"\x00\x62\x06proto3')

_UPDATEMODE = DESCRIPTOR.enum_types_by_name['UpdateMode']
UpdateMode = enum_type_wrapper.EnumTypeWrapper(_UPDATEMODE)
_UPDATEROWFORMAT = DESCRIPTOR.enum_types_by_name['UpdateRowFormat']
UpdateRowFormat = enum_type_wrapper.EnumTypeWrapper(_UPDATEROWFORMAT)
_FILTERMODE = DESCRIPTOR.enum_types_by_name['FilterMode']
FilterMode = enum_type_wrapper.EnumTypeWrapper(_FILTERMODE)
_FORWARDOP = DESCRIPTOR.enum_types_by_name['ForwardOp']
ForwardOp = enum_type_wrapper.EnumTypeWrapper(_FORWARDOP)
Schema = 0
Import = 1
Paste = 2
BulkSchema = 3
BulkImport = 4
Chain = 5
Modify = 6
Script = 7
Csv = 0
Binary = 1
JsonRecords = 2
JsonValues = 3
Full = 0
Part = 1
Glob = 2
Regex = 3
StartForward = 0
StopForward = 1
ListForwards = 2


_GETPARAMS = DESCRIPTOR.message_types_by_name['GetParams']
_GETDATAFRAMEREQUEST = DESCRIPTOR.message_types_by_name['GetDataFrameRequest']
_GETDATAFRAMEREQUEST_ADDONSENTRY = _GETDATAFRAMEREQUEST.nested_types_by_name['AddonsEntry']
_GETDATAFRAMERESPONSE = DESCRIPTOR.message_types_by_name['GetDataFrameResponse']
_GETDATAFRAMERESPONSE_ADDONSENTRY = _GETDATAFRAMERESPONSE.nested_types_by_name['AddonsEntry']
_UPDATEROWBINARY = DESCRIPTOR.message_types_by_name['UpdateRowBinary']
_CSVOPTION = DESCRIPTOR.message_types_by_name['CsvOption']
_CSVOPTION_CSVCOLMAPPINGBYPREFIXENTRY = _CSVOPTION.nested_types_by_name['CsvColMappingByPrefixEntry']
_SCRIPTOPTION = DESCRIPTOR.message_types_by_name['ScriptOption']
_UPDATEROWOPTION = DESCRIPTOR.message_types_by_name['UpdateRowOption']
_UPDATEDATAFRAMEREQUEST = DESCRIPTOR.message_types_by_name['UpdateDataFrameRequest']
_UPDATEDATAFRAMERESPONSE = DESCRIPTOR.message_types_by_name['UpdateDataFrameResponse']
_UPDATEMETAREQUEST = DESCRIPTOR.message_types_by_name['UpdateMetaRequest']
_UPDATEMETARESPONSE = DESCRIPTOR.message_types_by_name['UpdateMetaResponse']
_FILTER = DESCRIPTOR.message_types_by_name['Filter']
_GETTABLEREQUEST = DESCRIPTOR.message_types_by_name['GetTableRequest']
_GETTABLERESPONSE = DESCRIPTOR.message_types_by_name['GetTableResponse']
_GETTABLERESPONSE_SCHEMASENTRY = _GETTABLERESPONSE.nested_types_by_name['SchemasEntry']
_LISTOBJECTREQUEST = DESCRIPTOR.message_types_by_name['ListObjectRequest']
_LISTOBJECTRESPONSE = DESCRIPTOR.message_types_by_name['ListObjectResponse']
_LISTOBJECTRESPONSE_OBJECTSENTRY = _LISTOBJECTRESPONSE.nested_types_by_name['ObjectsEntry']
_LISTOBJECTRESPONSE_RECORDSENTRY = _LISTOBJECTRESPONSE.nested_types_by_name['RecordsEntry']
_BINLOGRECORD = DESCRIPTOR.message_types_by_name['BinlogRecord']
_FORWARDREQUEST = DESCRIPTOR.message_types_by_name['ForwardRequest']
_FORWARDDETAIL = DESCRIPTOR.message_types_by_name['ForwardDetail']
_FORWARDRESPONSE = DESCRIPTOR.message_types_by_name['ForwardResponse']
_FORWARDRESPONSE_FORWARDSENTRY = _FORWARDRESPONSE.nested_types_by_name['ForwardsEntry']
GetParams = _reflection.GeneratedProtocolMessageType('GetParams', (_message.Message,), {
  'DESCRIPTOR' : _GETPARAMS,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.GetParams)
  })
_sym_db.RegisterMessage(GetParams)

GetDataFrameRequest = _reflection.GeneratedProtocolMessageType('GetDataFrameRequest', (_message.Message,), {

  'AddonsEntry' : _reflection.GeneratedProtocolMessageType('AddonsEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETDATAFRAMEREQUEST_ADDONSENTRY,
    '__module__' : 'pymsd.proto.apiv1_pb2'
    # @@protoc_insertion_point(class_scope:apiv1.GetDataFrameRequest.AddonsEntry)
    })
  ,
  'DESCRIPTOR' : _GETDATAFRAMEREQUEST,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.GetDataFrameRequest)
  })
_sym_db.RegisterMessage(GetDataFrameRequest)
_sym_db.RegisterMessage(GetDataFrameRequest.AddonsEntry)

GetDataFrameResponse = _reflection.GeneratedProtocolMessageType('GetDataFrameResponse', (_message.Message,), {

  'AddonsEntry' : _reflection.GeneratedProtocolMessageType('AddonsEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETDATAFRAMERESPONSE_ADDONSENTRY,
    '__module__' : 'pymsd.proto.apiv1_pb2'
    # @@protoc_insertion_point(class_scope:apiv1.GetDataFrameResponse.AddonsEntry)
    })
  ,
  'DESCRIPTOR' : _GETDATAFRAMERESPONSE,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.GetDataFrameResponse)
  })
_sym_db.RegisterMessage(GetDataFrameResponse)
_sym_db.RegisterMessage(GetDataFrameResponse.AddonsEntry)

UpdateRowBinary = _reflection.GeneratedProtocolMessageType('UpdateRowBinary', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEROWBINARY,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.UpdateRowBinary)
  })
_sym_db.RegisterMessage(UpdateRowBinary)

CsvOption = _reflection.GeneratedProtocolMessageType('CsvOption', (_message.Message,), {

  'CsvColMappingByPrefixEntry' : _reflection.GeneratedProtocolMessageType('CsvColMappingByPrefixEntry', (_message.Message,), {
    'DESCRIPTOR' : _CSVOPTION_CSVCOLMAPPINGBYPREFIXENTRY,
    '__module__' : 'pymsd.proto.apiv1_pb2'
    # @@protoc_insertion_point(class_scope:apiv1.CsvOption.CsvColMappingByPrefixEntry)
    })
  ,
  'DESCRIPTOR' : _CSVOPTION,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.CsvOption)
  })
_sym_db.RegisterMessage(CsvOption)
_sym_db.RegisterMessage(CsvOption.CsvColMappingByPrefixEntry)

ScriptOption = _reflection.GeneratedProtocolMessageType('ScriptOption', (_message.Message,), {
  'DESCRIPTOR' : _SCRIPTOPTION,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.ScriptOption)
  })
_sym_db.RegisterMessage(ScriptOption)

UpdateRowOption = _reflection.GeneratedProtocolMessageType('UpdateRowOption', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEROWOPTION,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.UpdateRowOption)
  })
_sym_db.RegisterMessage(UpdateRowOption)

UpdateDataFrameRequest = _reflection.GeneratedProtocolMessageType('UpdateDataFrameRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDATAFRAMEREQUEST,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.UpdateDataFrameRequest)
  })
_sym_db.RegisterMessage(UpdateDataFrameRequest)

UpdateDataFrameResponse = _reflection.GeneratedProtocolMessageType('UpdateDataFrameResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDATAFRAMERESPONSE,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.UpdateDataFrameResponse)
  })
_sym_db.RegisterMessage(UpdateDataFrameResponse)

UpdateMetaRequest = _reflection.GeneratedProtocolMessageType('UpdateMetaRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMETAREQUEST,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.UpdateMetaRequest)
  })
_sym_db.RegisterMessage(UpdateMetaRequest)

UpdateMetaResponse = _reflection.GeneratedProtocolMessageType('UpdateMetaResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMETARESPONSE,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.UpdateMetaResponse)
  })
_sym_db.RegisterMessage(UpdateMetaResponse)

Filter = _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), {
  'DESCRIPTOR' : _FILTER,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.Filter)
  })
_sym_db.RegisterMessage(Filter)

GetTableRequest = _reflection.GeneratedProtocolMessageType('GetTableRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTABLEREQUEST,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.GetTableRequest)
  })
_sym_db.RegisterMessage(GetTableRequest)

GetTableResponse = _reflection.GeneratedProtocolMessageType('GetTableResponse', (_message.Message,), {

  'SchemasEntry' : _reflection.GeneratedProtocolMessageType('SchemasEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETTABLERESPONSE_SCHEMASENTRY,
    '__module__' : 'pymsd.proto.apiv1_pb2'
    # @@protoc_insertion_point(class_scope:apiv1.GetTableResponse.SchemasEntry)
    })
  ,
  'DESCRIPTOR' : _GETTABLERESPONSE,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.GetTableResponse)
  })
_sym_db.RegisterMessage(GetTableResponse)
_sym_db.RegisterMessage(GetTableResponse.SchemasEntry)

ListObjectRequest = _reflection.GeneratedProtocolMessageType('ListObjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTOBJECTREQUEST,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.ListObjectRequest)
  })
_sym_db.RegisterMessage(ListObjectRequest)

ListObjectResponse = _reflection.GeneratedProtocolMessageType('ListObjectResponse', (_message.Message,), {

  'ObjectsEntry' : _reflection.GeneratedProtocolMessageType('ObjectsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTOBJECTRESPONSE_OBJECTSENTRY,
    '__module__' : 'pymsd.proto.apiv1_pb2'
    # @@protoc_insertion_point(class_scope:apiv1.ListObjectResponse.ObjectsEntry)
    })
  ,

  'RecordsEntry' : _reflection.GeneratedProtocolMessageType('RecordsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTOBJECTRESPONSE_RECORDSENTRY,
    '__module__' : 'pymsd.proto.apiv1_pb2'
    # @@protoc_insertion_point(class_scope:apiv1.ListObjectResponse.RecordsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTOBJECTRESPONSE,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.ListObjectResponse)
  })
_sym_db.RegisterMessage(ListObjectResponse)
_sym_db.RegisterMessage(ListObjectResponse.ObjectsEntry)
_sym_db.RegisterMessage(ListObjectResponse.RecordsEntry)

BinlogRecord = _reflection.GeneratedProtocolMessageType('BinlogRecord', (_message.Message,), {
  'DESCRIPTOR' : _BINLOGRECORD,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.BinlogRecord)
  })
_sym_db.RegisterMessage(BinlogRecord)

ForwardRequest = _reflection.GeneratedProtocolMessageType('ForwardRequest', (_message.Message,), {
  'DESCRIPTOR' : _FORWARDREQUEST,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.ForwardRequest)
  })
_sym_db.RegisterMessage(ForwardRequest)

ForwardDetail = _reflection.GeneratedProtocolMessageType('ForwardDetail', (_message.Message,), {
  'DESCRIPTOR' : _FORWARDDETAIL,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.ForwardDetail)
  })
_sym_db.RegisterMessage(ForwardDetail)

ForwardResponse = _reflection.GeneratedProtocolMessageType('ForwardResponse', (_message.Message,), {

  'ForwardsEntry' : _reflection.GeneratedProtocolMessageType('ForwardsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FORWARDRESPONSE_FORWARDSENTRY,
    '__module__' : 'pymsd.proto.apiv1_pb2'
    # @@protoc_insertion_point(class_scope:apiv1.ForwardResponse.ForwardsEntry)
    })
  ,
  'DESCRIPTOR' : _FORWARDRESPONSE,
  '__module__' : 'pymsd.proto.apiv1_pb2'
  # @@protoc_insertion_point(class_scope:apiv1.ForwardResponse)
  })
_sym_db.RegisterMessage(ForwardResponse)
_sym_db.RegisterMessage(ForwardResponse.ForwardsEntry)

_DATAFRAMESERVICE = DESCRIPTOR.services_by_name['DataFrameService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETDATAFRAMEREQUEST_ADDONSENTRY._options = None
  _GETDATAFRAMEREQUEST_ADDONSENTRY._serialized_options = b'8\001'
  _GETDATAFRAMERESPONSE_ADDONSENTRY._options = None
  _GETDATAFRAMERESPONSE_ADDONSENTRY._serialized_options = b'8\001'
  _CSVOPTION_CSVCOLMAPPINGBYPREFIXENTRY._options = None
  _CSVOPTION_CSVCOLMAPPINGBYPREFIXENTRY._serialized_options = b'8\001'
  _GETTABLERESPONSE_SCHEMASENTRY._options = None
  _GETTABLERESPONSE_SCHEMASENTRY._serialized_options = b'8\001'
  _LISTOBJECTRESPONSE_OBJECTSENTRY._options = None
  _LISTOBJECTRESPONSE_OBJECTSENTRY._serialized_options = b'8\001'
  _LISTOBJECTRESPONSE_RECORDSENTRY._options = None
  _LISTOBJECTRESPONSE_RECORDSENTRY._serialized_options = b'8\001'
  _FORWARDRESPONSE_FORWARDSENTRY._options = None
  _FORWARDRESPONSE_FORWARDSENTRY._serialized_options = b'8\001'
  _UPDATEMODE._serialized_start=2782
  _UPDATEMODE._serialized_end=2896
  _UPDATEROWFORMAT._serialized_start=2898
  _UPDATEROWFORMAT._serialized_end=2969
  _FILTERMODE._serialized_start=2971
  _FILTERMODE._serialized_end=3024
  _FORWARDOP._serialized_start=3026
  _FORWARDOP._serialized_end=3090
  _GETPARAMS._serialized_start=90
  _GETPARAMS._serialized_end=291
  _GETDATAFRAMEREQUEST._serialized_start=294
  _GETDATAFRAMEREQUEST._serialized_end=465
  _GETDATAFRAMEREQUEST_ADDONSENTRY._serialized_start=420
  _GETDATAFRAMEREQUEST_ADDONSENTRY._serialized_end=465
  _GETDATAFRAMERESPONSE._serialized_start=468
  _GETDATAFRAMERESPONSE._serialized_end=662
  _GETDATAFRAMERESPONSE_ADDONSENTRY._serialized_start=420
  _GETDATAFRAMERESPONSE_ADDONSENTRY._serialized_end=465
  _UPDATEROWBINARY._serialized_start=664
  _UPDATEROWBINARY._serialized_end=725
  _CSVOPTION._serialized_start=728
  _CSVOPTION._serialized_end=1066
  _CSVOPTION_CSVCOLMAPPINGBYPREFIXENTRY._serialized_start=1006
  _CSVOPTION_CSVCOLMAPPINGBYPREFIXENTRY._serialized_end=1066
  _SCRIPTOPTION._serialized_start=1068
  _SCRIPTOPTION._serialized_end=1096
  _UPDATEROWOPTION._serialized_start=1098
  _UPDATEROWOPTION._serialized_end=1223
  _UPDATEDATAFRAMEREQUEST._serialized_start=1226
  _UPDATEDATAFRAMEREQUEST._serialized_end=1401
  _UPDATEDATAFRAMERESPONSE._serialized_start=1403
  _UPDATEDATAFRAMERESPONSE._serialized_end=1480
  _UPDATEMETAREQUEST._serialized_start=1482
  _UPDATEMETAREQUEST._serialized_end=1560
  _UPDATEMETARESPONSE._serialized_start=1562
  _UPDATEMETARESPONSE._serialized_end=1612
  _FILTER._serialized_start=1614
  _FILTER._serialized_end=1692
  _GETTABLEREQUEST._serialized_start=1694
  _GETTABLEREQUEST._serialized_end=1746
  _GETTABLERESPONSE._serialized_start=1749
  _GETTABLERESPONSE._serialized_end=1916
  _GETTABLERESPONSE_SCHEMASENTRY._serialized_start=1854
  _GETTABLERESPONSE_SCHEMASENTRY._serialized_end=1916
  _LISTOBJECTREQUEST._serialized_start=1918
  _LISTOBJECTREQUEST._serialized_end=2012
  _LISTOBJECTRESPONSE._serialized_start=2015
  _LISTOBJECTRESPONSE._serialized_end=2324
  _LISTOBJECTRESPONSE_OBJECTSENTRY._serialized_start=2181
  _LISTOBJECTRESPONSE_OBJECTSENTRY._serialized_end=2254
  _LISTOBJECTRESPONSE_RECORDSENTRY._serialized_start=2256
  _LISTOBJECTRESPONSE_RECORDSENTRY._serialized_end=2324
  _BINLOGRECORD._serialized_start=2327
  _BINLOGRECORD._serialized_end=2461
  _FORWARDREQUEST._serialized_start=2463
  _FORWARDREQUEST._serialized_end=2570
  _FORWARDDETAIL._serialized_start=2572
  _FORWARDDETAIL._serialized_end=2603
  _FORWARDRESPONSE._serialized_start=2606
  _FORWARDRESPONSE._serialized_end=2780
  _FORWARDRESPONSE_FORWARDSENTRY._serialized_start=2711
  _FORWARDRESPONSE_FORWARDSENTRY._serialized_end=2780
  _DATAFRAMESERVICE._serialized_start=3093
  _DATAFRAMESERVICE._serialized_end=3515
# @@protoc_insertion_point(module_scope)
