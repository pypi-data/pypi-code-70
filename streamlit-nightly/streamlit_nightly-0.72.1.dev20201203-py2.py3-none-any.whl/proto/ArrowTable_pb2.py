# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/ArrowTable.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='streamlit/proto/ArrowTable.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n streamlit/proto/ArrowTable.proto\"S\n\nArrowTable\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\r\n\x05index\x18\x02 \x01(\x0c\x12\x0f\n\x07\x63olumns\x18\x03 \x01(\x0c\x12\x17\n\x06styler\x18\x05 \x01(\x0b\x32\x07.Styler\"O\n\x06Styler\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0f\n\x07\x63\x61ption\x18\x02 \x01(\t\x12\x0e\n\x06styles\x18\x03 \x01(\t\x12\x16\n\x0e\x64isplay_values\x18\x04 \x01(\x0c\x62\x06proto3')
)




_ARROWTABLE = _descriptor.Descriptor(
  name='ArrowTable',
  full_name='ArrowTable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='ArrowTable.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='ArrowTable.index', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='ArrowTable.columns', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='styler', full_name='ArrowTable.styler', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=119,
)


_STYLER = _descriptor.Descriptor(
  name='Styler',
  full_name='Styler',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='Styler.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='caption', full_name='Styler.caption', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='styles', full_name='Styler.styles', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_values', full_name='Styler.display_values', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=200,
)

_ARROWTABLE.fields_by_name['styler'].message_type = _STYLER
DESCRIPTOR.message_types_by_name['ArrowTable'] = _ARROWTABLE
DESCRIPTOR.message_types_by_name['Styler'] = _STYLER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ArrowTable = _reflection.GeneratedProtocolMessageType('ArrowTable', (_message.Message,), dict(
  DESCRIPTOR = _ARROWTABLE,
  __module__ = 'streamlit.proto.ArrowTable_pb2'
  # @@protoc_insertion_point(class_scope:ArrowTable)
  ))
_sym_db.RegisterMessage(ArrowTable)

Styler = _reflection.GeneratedProtocolMessageType('Styler', (_message.Message,), dict(
  DESCRIPTOR = _STYLER,
  __module__ = 'streamlit.proto.ArrowTable_pb2'
  # @@protoc_insertion_point(class_scope:Styler)
  ))
_sym_db.RegisterMessage(Styler)


# @@protoc_insertion_point(module_scope)
