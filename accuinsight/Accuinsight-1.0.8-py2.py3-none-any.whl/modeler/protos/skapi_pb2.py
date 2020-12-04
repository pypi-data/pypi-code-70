# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: skapi.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='skapi.proto',
  package='modeler',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0bskapi.proto\x12\x07modeler\x1a google/protobuf/descriptor.proto\"\xd0\x01\n\x13SkModelerRpcOptions\x12(\n\tendpoints\x18\x01 \x03(\x0b\x32\x15.modeler.HttpEndpoint\x12\'\n\nvisibility\x18\x02 \x01(\x0e\x32\x13.modeler.Visibility\x12\'\n\x0b\x65rror_codes\x18\x03 \x03(\x0e\x32\x12.modeler.ErrorCode\x12&\n\nrate_limit\x18\x04 \x01(\x0b\x32\x12.modeler.RateLimit\x12\x15\n\rrpc_doc_title\x18\x05 \x01(\t\"V\n\x0cHttpEndpoint\x12\x14\n\x06method\x18\x01 \x01(\t:\x04POST\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\"\n\x05since\x18\x03 \x01(\x0b\x32\x13.modeler.ApiVersion\"*\n\nApiVersion\x12\r\n\x05major\x18\x01 \x01(\x05\x12\r\n\x05minor\x18\x02 \x01(\x05\"@\n\tRateLimit\x12\x11\n\tmax_burst\x18\x01 \x01(\x03\x12 \n\x18max_sustained_per_second\x18\x02 \x01(\x03\"\x94\x01\n\x15\x44ocumentationMetadata\x12\x11\n\tdocstring\x18\x01 \x01(\t\x12\x10\n\x08lead_doc\x18\x02 \x01(\t\x12\'\n\nvisibility\x18\x03 \x01(\x0e\x32\x13.modeler.Visibility\x12\x1b\n\x13original_proto_path\x18\x04 \x03(\t\x12\x10\n\x08position\x18\x05 \x01(\x05*?\n\nVisibility\x12\n\n\x06PUBLIC\x10\x01\x12\x0c\n\x08INTERNAL\x10\x02\x12\x17\n\x13PUBLIC_UNDOCUMENTED\x10\x03*\xf6\x04\n\tErrorCode\x12\x12\n\x0eINTERNAL_ERROR\x10\x01\x12\x1b\n\x17TEMPORARILY_UNAVAILABLE\x10\x02\x12\x0c\n\x08IO_ERROR\x10\x03\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10\x04\x12\x1c\n\x17INVALID_PARAMETER_VALUE\x10\xe8\x07\x12\x17\n\x12\x45NDPOINT_NOT_FOUND\x10\xe9\x07\x12\x16\n\x11MALFORMED_REQUEST\x10\xea\x07\x12\x12\n\rINVALID_STATE\x10\xeb\x07\x12\x16\n\x11PERMISSION_DENIED\x10\xec\x07\x12\x15\n\x10\x46\x45\x41TURE_DISABLED\x10\xed\x07\x12\x1a\n\x15\x43USTOMER_UNAUTHORIZED\x10\xee\x07\x12\x1b\n\x16REQUEST_LIMIT_EXCEEDED\x10\xef\x07\x12\x1d\n\x18INVALID_STATE_TRANSITION\x10\xd1\x0f\x12\x1b\n\x16\x43OULD_NOT_ACQUIRE_LOCK\x10\xd2\x0f\x12\x1c\n\x17RESOURCE_ALREADY_EXISTS\x10\xb9\x17\x12\x1c\n\x17RESOURCE_DOES_NOT_EXIST\x10\xba\x17\x12\x13\n\x0eQUOTA_EXCEEDED\x10\xa1\x1f\x12\x1c\n\x17MAX_BLOCK_SIZE_EXCEEDED\x10\xa2\x1f\x12\x1b\n\x16MAX_READ_SIZE_EXCEEDED\x10\xa3\x1f\x12\x13\n\x0e\x44RY_RUN_FAILED\x10\x89\'\x12\x1c\n\x17RESOURCE_LIMIT_EXCEEDED\x10\x8a\'\x12\x18\n\x13\x44IRECTORY_NOT_EMPTY\x10\xf1.\x12\x18\n\x13\x44IRECTORY_PROTECTED\x10\xf2.\x12\x1f\n\x1aMAX_NOTEBOOK_SIZE_EXCEEDED\x10\xf3.:H\n\nvisibility\x12\x1d.google.protobuf.FieldOptions\x18\xee\x90\x03 \x01(\x0e\x32\x13.modeler.Visibility::\n\x11validate_required\x12\x1d.google.protobuf.FieldOptions\x18\xef\x90\x03 \x01(\x08:4\n\x0bjson_inline\x12\x1d.google.protobuf.FieldOptions\x18\xf0\x90\x03 \x01(\x08:1\n\x08json_map\x12\x1d.google.protobuf.FieldOptions\x18\xf1\x90\x03 \x01(\x08:R\n\tfield_doc\x12\x1d.google.protobuf.FieldOptions\x18\xf2\x90\x03 \x03(\x0b\x32\x1e.modeler.DocumentationMetadata:K\n\x03rpc\x12\x1e.google.protobuf.MethodOptions\x18\xee\x90\x03 \x01(\x0b\x32\x1c.modeler.SkModelerRpcOptions:T\n\nmethod_doc\x12\x1e.google.protobuf.MethodOptions\x18\xf2\x90\x03 \x03(\x0b\x32\x1e.modeler.DocumentationMetadata:V\n\x0bmessage_doc\x12\x1f.google.protobuf.MessageOptions\x18\xf2\x90\x03 \x03(\x0b\x32\x1e.modeler.DocumentationMetadata:V\n\x0bservice_doc\x12\x1f.google.protobuf.ServiceOptions\x18\xf2\x90\x03 \x03(\x0b\x32\x1e.modeler.DocumentationMetadata:P\n\x08\x65num_doc\x12\x1c.google.protobuf.EnumOptions\x18\xf2\x90\x03 \x03(\x0b\x32\x1e.modeler.DocumentationMetadata:W\n\x15\x65num_value_visibility\x12!.google.protobuf.EnumValueOptions\x18\xee\x90\x03 \x01(\x0e\x32\x13.modeler.Visibility:[\n\x0e\x65num_value_doc\x12!.google.protobuf.EnumValueOptions\x18\xf2\x90\x03 \x03(\x0b\x32\x1e.modeler.DocumentationMetadata')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])

_VISIBILITY = _descriptor.EnumDescriptor(
  name='Visibility',
  full_name='modeler.Visibility',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PUBLIC', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUBLIC_UNDOCUMENTED', index=2, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=618,
  serialized_end=681,
)
_sym_db.RegisterEnumDescriptor(_VISIBILITY)

Visibility = enum_type_wrapper.EnumTypeWrapper(_VISIBILITY)
_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='modeler.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMPORARILY_UNAVAILABLE', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IO_ERROR', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_REQUEST', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PARAMETER_VALUE', index=4, number=1000,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENDPOINT_NOT_FOUND', index=5, number=1001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MALFORMED_REQUEST', index=6, number=1002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_STATE', index=7, number=1003,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERMISSION_DENIED', index=8, number=1004,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEATURE_DISABLED', index=9, number=1005,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_UNAUTHORIZED', index=10, number=1006,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_LIMIT_EXCEEDED', index=11, number=1007,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_STATE_TRANSITION', index=12, number=2001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COULD_NOT_ACQUIRE_LOCK', index=13, number=2002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESOURCE_ALREADY_EXISTS', index=14, number=3001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESOURCE_DOES_NOT_EXIST', index=15, number=3002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUOTA_EXCEEDED', index=16, number=4001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX_BLOCK_SIZE_EXCEEDED', index=17, number=4002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX_READ_SIZE_EXCEEDED', index=18, number=4003,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRY_RUN_FAILED', index=19, number=5001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESOURCE_LIMIT_EXCEEDED', index=20, number=5002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIRECTORY_NOT_EMPTY', index=21, number=6001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIRECTORY_PROTECTED', index=22, number=6002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX_NOTEBOOK_SIZE_EXCEEDED', index=23, number=6003,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=684,
  serialized_end=1314,
)
_sym_db.RegisterEnumDescriptor(_ERRORCODE)

ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
PUBLIC = 1
INTERNAL = 2
PUBLIC_UNDOCUMENTED = 3
INTERNAL_ERROR = 1
TEMPORARILY_UNAVAILABLE = 2
IO_ERROR = 3
BAD_REQUEST = 4
INVALID_PARAMETER_VALUE = 1000
ENDPOINT_NOT_FOUND = 1001
MALFORMED_REQUEST = 1002
INVALID_STATE = 1003
PERMISSION_DENIED = 1004
FEATURE_DISABLED = 1005
CUSTOMER_UNAUTHORIZED = 1006
REQUEST_LIMIT_EXCEEDED = 1007
INVALID_STATE_TRANSITION = 2001
COULD_NOT_ACQUIRE_LOCK = 2002
RESOURCE_ALREADY_EXISTS = 3001
RESOURCE_DOES_NOT_EXIST = 3002
QUOTA_EXCEEDED = 4001
MAX_BLOCK_SIZE_EXCEEDED = 4002
MAX_READ_SIZE_EXCEEDED = 4003
DRY_RUN_FAILED = 5001
RESOURCE_LIMIT_EXCEEDED = 5002
DIRECTORY_NOT_EMPTY = 6001
DIRECTORY_PROTECTED = 6002
MAX_NOTEBOOK_SIZE_EXCEEDED = 6003

VISIBILITY_FIELD_NUMBER = 51310
visibility = _descriptor.FieldDescriptor(
  name='visibility', full_name='modeler.visibility', index=0,
  number=51310, type=14, cpp_type=8, label=1,
  has_default_value=False, default_value=1,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
VALIDATE_REQUIRED_FIELD_NUMBER = 51311
validate_required = _descriptor.FieldDescriptor(
  name='validate_required', full_name='modeler.validate_required', index=1,
  number=51311, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
JSON_INLINE_FIELD_NUMBER = 51312
json_inline = _descriptor.FieldDescriptor(
  name='json_inline', full_name='modeler.json_inline', index=2,
  number=51312, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
JSON_MAP_FIELD_NUMBER = 51313
json_map = _descriptor.FieldDescriptor(
  name='json_map', full_name='modeler.json_map', index=3,
  number=51313, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
FIELD_DOC_FIELD_NUMBER = 51314
field_doc = _descriptor.FieldDescriptor(
  name='field_doc', full_name='modeler.field_doc', index=4,
  number=51314, type=11, cpp_type=10, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
RPC_FIELD_NUMBER = 51310
rpc = _descriptor.FieldDescriptor(
  name='rpc', full_name='modeler.rpc', index=5,
  number=51310, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
METHOD_DOC_FIELD_NUMBER = 51314
method_doc = _descriptor.FieldDescriptor(
  name='method_doc', full_name='modeler.method_doc', index=6,
  number=51314, type=11, cpp_type=10, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
MESSAGE_DOC_FIELD_NUMBER = 51314
message_doc = _descriptor.FieldDescriptor(
  name='message_doc', full_name='modeler.message_doc', index=7,
  number=51314, type=11, cpp_type=10, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
SERVICE_DOC_FIELD_NUMBER = 51314
service_doc = _descriptor.FieldDescriptor(
  name='service_doc', full_name='modeler.service_doc', index=8,
  number=51314, type=11, cpp_type=10, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
ENUM_DOC_FIELD_NUMBER = 51314
enum_doc = _descriptor.FieldDescriptor(
  name='enum_doc', full_name='modeler.enum_doc', index=9,
  number=51314, type=11, cpp_type=10, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
ENUM_VALUE_VISIBILITY_FIELD_NUMBER = 51310
enum_value_visibility = _descriptor.FieldDescriptor(
  name='enum_value_visibility', full_name='modeler.enum_value_visibility', index=10,
  number=51310, type=14, cpp_type=8, label=1,
  has_default_value=False, default_value=1,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
ENUM_VALUE_DOC_FIELD_NUMBER = 51314
enum_value_doc = _descriptor.FieldDescriptor(
  name='enum_value_doc', full_name='modeler.enum_value_doc', index=11,
  number=51314, type=11, cpp_type=10, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)


_SKMODELERRPCOPTIONS = _descriptor.Descriptor(
  name='SkModelerRpcOptions',
  full_name='modeler.SkModelerRpcOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoints', full_name='modeler.SkModelerRpcOptions.endpoints', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visibility', full_name='modeler.SkModelerRpcOptions.visibility', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_codes', full_name='modeler.SkModelerRpcOptions.error_codes', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='modeler.SkModelerRpcOptions.rate_limit', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rpc_doc_title', full_name='modeler.SkModelerRpcOptions.rpc_doc_title', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=267,
)


_HTTPENDPOINT = _descriptor.Descriptor(
  name='HttpEndpoint',
  full_name='modeler.HttpEndpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='modeler.HttpEndpoint.method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("POST").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='modeler.HttpEndpoint.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='since', full_name='modeler.HttpEndpoint.since', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=269,
  serialized_end=355,
)


_APIVERSION = _descriptor.Descriptor(
  name='ApiVersion',
  full_name='modeler.ApiVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='major', full_name='modeler.ApiVersion.major', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minor', full_name='modeler.ApiVersion.minor', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=357,
  serialized_end=399,
)


_RATELIMIT = _descriptor.Descriptor(
  name='RateLimit',
  full_name='modeler.RateLimit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_burst', full_name='modeler.RateLimit.max_burst', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_sustained_per_second', full_name='modeler.RateLimit.max_sustained_per_second', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=401,
  serialized_end=465,
)


_DOCUMENTATIONMETADATA = _descriptor.Descriptor(
  name='DocumentationMetadata',
  full_name='modeler.DocumentationMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='docstring', full_name='modeler.DocumentationMetadata.docstring', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lead_doc', full_name='modeler.DocumentationMetadata.lead_doc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visibility', full_name='modeler.DocumentationMetadata.visibility', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='original_proto_path', full_name='modeler.DocumentationMetadata.original_proto_path', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='modeler.DocumentationMetadata.position', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=468,
  serialized_end=616,
)

_SKMODELERRPCOPTIONS.fields_by_name['endpoints'].message_type = _HTTPENDPOINT
_SKMODELERRPCOPTIONS.fields_by_name['visibility'].enum_type = _VISIBILITY
_SKMODELERRPCOPTIONS.fields_by_name['error_codes'].enum_type = _ERRORCODE
_SKMODELERRPCOPTIONS.fields_by_name['rate_limit'].message_type = _RATELIMIT
_HTTPENDPOINT.fields_by_name['since'].message_type = _APIVERSION
_DOCUMENTATIONMETADATA.fields_by_name['visibility'].enum_type = _VISIBILITY
DESCRIPTOR.message_types_by_name['SkModelerRpcOptions'] = _SKMODELERRPCOPTIONS
DESCRIPTOR.message_types_by_name['HttpEndpoint'] = _HTTPENDPOINT
DESCRIPTOR.message_types_by_name['ApiVersion'] = _APIVERSION
DESCRIPTOR.message_types_by_name['RateLimit'] = _RATELIMIT
DESCRIPTOR.message_types_by_name['DocumentationMetadata'] = _DOCUMENTATIONMETADATA
DESCRIPTOR.enum_types_by_name['Visibility'] = _VISIBILITY
DESCRIPTOR.enum_types_by_name['ErrorCode'] = _ERRORCODE
DESCRIPTOR.extensions_by_name['visibility'] = visibility
DESCRIPTOR.extensions_by_name['validate_required'] = validate_required
DESCRIPTOR.extensions_by_name['json_inline'] = json_inline
DESCRIPTOR.extensions_by_name['json_map'] = json_map
DESCRIPTOR.extensions_by_name['field_doc'] = field_doc
DESCRIPTOR.extensions_by_name['rpc'] = rpc
DESCRIPTOR.extensions_by_name['method_doc'] = method_doc
DESCRIPTOR.extensions_by_name['message_doc'] = message_doc
DESCRIPTOR.extensions_by_name['service_doc'] = service_doc
DESCRIPTOR.extensions_by_name['enum_doc'] = enum_doc
DESCRIPTOR.extensions_by_name['enum_value_visibility'] = enum_value_visibility
DESCRIPTOR.extensions_by_name['enum_value_doc'] = enum_value_doc
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SkModelerRpcOptions = _reflection.GeneratedProtocolMessageType('SkModelerRpcOptions', (_message.Message,), dict(
  DESCRIPTOR = _SKMODELERRPCOPTIONS,
  __module__ = 'skapi_pb2'
  # @@protoc_insertion_point(class_scope:modeler.SkModelerRpcOptions)
  ))
_sym_db.RegisterMessage(SkModelerRpcOptions)

HttpEndpoint = _reflection.GeneratedProtocolMessageType('HttpEndpoint', (_message.Message,), dict(
  DESCRIPTOR = _HTTPENDPOINT,
  __module__ = 'skapi_pb2'
  # @@protoc_insertion_point(class_scope:modeler.HttpEndpoint)
  ))
_sym_db.RegisterMessage(HttpEndpoint)

ApiVersion = _reflection.GeneratedProtocolMessageType('ApiVersion', (_message.Message,), dict(
  DESCRIPTOR = _APIVERSION,
  __module__ = 'skapi_pb2'
  # @@protoc_insertion_point(class_scope:modeler.ApiVersion)
  ))
_sym_db.RegisterMessage(ApiVersion)

RateLimit = _reflection.GeneratedProtocolMessageType('RateLimit', (_message.Message,), dict(
  DESCRIPTOR = _RATELIMIT,
  __module__ = 'skapi_pb2'
  # @@protoc_insertion_point(class_scope:modeler.RateLimit)
  ))
_sym_db.RegisterMessage(RateLimit)

DocumentationMetadata = _reflection.GeneratedProtocolMessageType('DocumentationMetadata', (_message.Message,), dict(
  DESCRIPTOR = _DOCUMENTATIONMETADATA,
  __module__ = 'skapi_pb2'
  # @@protoc_insertion_point(class_scope:modeler.DocumentationMetadata)
  ))
_sym_db.RegisterMessage(DocumentationMetadata)

visibility.enum_type = _VISIBILITY
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(visibility)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(validate_required)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(json_inline)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(json_map)
field_doc.message_type = _DOCUMENTATIONMETADATA
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field_doc)
rpc.message_type = _SKMODELERRPCOPTIONS
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(rpc)
method_doc.message_type = _DOCUMENTATIONMETADATA
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(method_doc)
message_doc.message_type = _DOCUMENTATIONMETADATA
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(message_doc)
service_doc.message_type = _DOCUMENTATIONMETADATA
google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(service_doc)
enum_doc.message_type = _DOCUMENTATIONMETADATA
google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(enum_doc)
enum_value_visibility.enum_type = _VISIBILITY
google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(enum_value_visibility)
enum_value_doc.message_type = _DOCUMENTATIONMETADATA
google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(enum_value_doc)

# @@protoc_insertion_point(module_scope)
