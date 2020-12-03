# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/google/fhir/proto/r4/core/resources/enrollment_request.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from proto.google.fhir.proto import annotations_pb2 as proto_dot_google_dot_fhir_dot_proto_dot_annotations__pb2
from proto.google.fhir.proto.r4.core import codes_pb2 as proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_codes__pb2
from proto.google.fhir.proto.r4.core import datatypes_pb2 as proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/google/fhir/proto/r4/core/resources/enrollment_request.proto',
  package='google.fhir.r4.core',
  syntax='proto3',
  serialized_options=b'\n\027com.google.fhir.r4.coreP\001\230\306\260\265\007\004',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nBproto/google/fhir/proto/r4/core/resources/enrollment_request.proto\x12\x13google.fhir.r4.core\x1a\x19google/protobuf/any.proto\x1a)proto/google/fhir/proto/annotations.proto\x1a+proto/google/fhir/proto/r4/core/codes.proto\x1a/proto/google/fhir/proto/r4/core/datatypes.proto\"\xca\t\n\x11\x45nrollmentRequest\x12#\n\x02id\x18\x01 \x01(\x0b\x32\x17.google.fhir.r4.core.Id\x12\'\n\x04meta\x18\x02 \x01(\x0b\x32\x19.google.fhir.r4.core.Meta\x12\x30\n\x0eimplicit_rules\x18\x03 \x01(\x0b\x32\x18.google.fhir.r4.core.Uri\x12+\n\x08language\x18\x04 \x01(\x0b\x32\x19.google.fhir.r4.core.Code\x12,\n\x04text\x18\x05 \x01(\x0b\x32\x1e.google.fhir.r4.core.Narrative\x12\'\n\tcontained\x18\x06 \x03(\x0b\x32\x14.google.protobuf.Any\x12\x31\n\textension\x18\x08 \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension\x12:\n\x12modifier_extension\x18\t \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension\x12\x33\n\nidentifier\x18\n \x03(\x0b\x32\x1f.google.fhir.r4.core.Identifier\x12\x41\n\x06status\x18\x0b \x01(\x0b\x32\x31.google.fhir.r4.core.EnrollmentRequest.StatusCode\x12.\n\x07\x63reated\x18\x0c \x01(\x0b\x32\x1d.google.fhir.r4.core.DateTime\x12\x43\n\x07insurer\x18\r \x01(\x0b\x32\x1e.google.fhir.r4.core.ReferenceB\x12\xf2\xff\xfc\xc2\x06\x0cOrganization\x12l\n\x08provider\x18\x0e \x01(\x0b\x32\x1e.google.fhir.r4.core.ReferenceB:\xf2\xff\xfc\xc2\x06\x0cPractitioner\xf2\xff\xfc\xc2\x06\x10PractitionerRole\xf2\xff\xfc\xc2\x06\x0cOrganization\x12@\n\tcandidate\x18\x0f \x01(\x0b\x32\x1e.google.fhir.r4.core.ReferenceB\r\xf2\xff\xfc\xc2\x06\x07Patient\x12@\n\x08\x63overage\x18\x10 \x01(\x0b\x32\x1e.google.fhir.r4.core.ReferenceB\x0e\xf2\xff\xfc\xc2\x06\x08\x43overage\x1a\x95\x02\n\nStatusCode\x12\x45\n\x05value\x18\x01 \x01(\x0e\x32\x36.google.fhir.r4.core.FinancialResourceStatusCode.Value\x12\'\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.fhir.r4.core.String\x12\x31\n\textension\x18\x03 \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension:d\xc0\x9f\xe3\xb6\x05\x01\x8a\xf9\x83\xb2\x05&http://hl7.org/fhir/ValueSet/fm-status\x9a\xb5\x8e\x93\x06,http://hl7.org/fhir/StructureDefinition/code:E\xc0\x9f\xe3\xb6\x05\x03\xb2\xfe\xe4\x97\x06\x39http://hl7.org/fhir/StructureDefinition/EnrollmentRequestJ\x04\x08\x07\x10\x08\x42!\n\x17\x63om.google.fhir.r4.coreP\x01\x98\xc6\xb0\xb5\x07\x04\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,proto_dot_google_dot_fhir_dot_proto_dot_annotations__pb2.DESCRIPTOR,proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_codes__pb2.DESCRIPTOR,proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2.DESCRIPTOR,])




_ENROLLMENTREQUEST_STATUSCODE = _descriptor.Descriptor(
  name='StatusCode',
  full_name='google.fhir.r4.core.EnrollmentRequest.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='google.fhir.r4.core.EnrollmentRequest.StatusCode.value', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.r4.core.EnrollmentRequest.StatusCode.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extension', full_name='google.fhir.r4.core.EnrollmentRequest.StatusCode.extension', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\300\237\343\266\005\001\212\371\203\262\005&http://hl7.org/fhir/ValueSet/fm-status\232\265\216\223\006,http://hl7.org/fhir/StructureDefinition/code',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1128,
  serialized_end=1405,
)

_ENROLLMENTREQUEST = _descriptor.Descriptor(
  name='EnrollmentRequest',
  full_name='google.fhir.r4.core.EnrollmentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.r4.core.EnrollmentRequest.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='google.fhir.r4.core.EnrollmentRequest.meta', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='implicit_rules', full_name='google.fhir.r4.core.EnrollmentRequest.implicit_rules', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='google.fhir.r4.core.EnrollmentRequest.language', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='google.fhir.r4.core.EnrollmentRequest.text', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contained', full_name='google.fhir.r4.core.EnrollmentRequest.contained', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extension', full_name='google.fhir.r4.core.EnrollmentRequest.extension', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='modifier_extension', full_name='google.fhir.r4.core.EnrollmentRequest.modifier_extension', index=7,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='google.fhir.r4.core.EnrollmentRequest.identifier', index=8,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.fhir.r4.core.EnrollmentRequest.status', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created', full_name='google.fhir.r4.core.EnrollmentRequest.created', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='insurer', full_name='google.fhir.r4.core.EnrollmentRequest.insurer', index=11,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\377\374\302\006\014Organization', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provider', full_name='google.fhir.r4.core.EnrollmentRequest.provider', index=12,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\377\374\302\006\014Practitioner\362\377\374\302\006\020PractitionerRole\362\377\374\302\006\014Organization', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='candidate', full_name='google.fhir.r4.core.EnrollmentRequest.candidate', index=13,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\377\374\302\006\007Patient', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coverage', full_name='google.fhir.r4.core.EnrollmentRequest.coverage', index=14,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\377\374\302\006\010Coverage', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ENROLLMENTREQUEST_STATUSCODE, ],
  enum_types=[
  ],
  serialized_options=b'\300\237\343\266\005\003\262\376\344\227\0069http://hl7.org/fhir/StructureDefinition/EnrollmentRequest',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=256,
  serialized_end=1482,
)

_ENROLLMENTREQUEST_STATUSCODE.fields_by_name['value'].enum_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_codes__pb2._FINANCIALRESOURCESTATUSCODE_VALUE
_ENROLLMENTREQUEST_STATUSCODE.fields_by_name['id'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._STRING
_ENROLLMENTREQUEST_STATUSCODE.fields_by_name['extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_ENROLLMENTREQUEST_STATUSCODE.containing_type = _ENROLLMENTREQUEST
_ENROLLMENTREQUEST.fields_by_name['id'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._ID
_ENROLLMENTREQUEST.fields_by_name['meta'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._META
_ENROLLMENTREQUEST.fields_by_name['implicit_rules'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._URI
_ENROLLMENTREQUEST.fields_by_name['language'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CODE
_ENROLLMENTREQUEST.fields_by_name['text'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._NARRATIVE
_ENROLLMENTREQUEST.fields_by_name['contained'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_ENROLLMENTREQUEST.fields_by_name['extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_ENROLLMENTREQUEST.fields_by_name['modifier_extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_ENROLLMENTREQUEST.fields_by_name['identifier'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._IDENTIFIER
_ENROLLMENTREQUEST.fields_by_name['status'].message_type = _ENROLLMENTREQUEST_STATUSCODE
_ENROLLMENTREQUEST.fields_by_name['created'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._DATETIME
_ENROLLMENTREQUEST.fields_by_name['insurer'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._REFERENCE
_ENROLLMENTREQUEST.fields_by_name['provider'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._REFERENCE
_ENROLLMENTREQUEST.fields_by_name['candidate'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._REFERENCE
_ENROLLMENTREQUEST.fields_by_name['coverage'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._REFERENCE
DESCRIPTOR.message_types_by_name['EnrollmentRequest'] = _ENROLLMENTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EnrollmentRequest = _reflection.GeneratedProtocolMessageType('EnrollmentRequest', (_message.Message,), {

  'StatusCode' : _reflection.GeneratedProtocolMessageType('StatusCode', (_message.Message,), {
    'DESCRIPTOR' : _ENROLLMENTREQUEST_STATUSCODE,
    '__module__' : 'proto.google.fhir.proto.r4.core.resources.enrollment_request_pb2'
    # @@protoc_insertion_point(class_scope:google.fhir.r4.core.EnrollmentRequest.StatusCode)
    })
  ,
  'DESCRIPTOR' : _ENROLLMENTREQUEST,
  '__module__' : 'proto.google.fhir.proto.r4.core.resources.enrollment_request_pb2'
  # @@protoc_insertion_point(class_scope:google.fhir.r4.core.EnrollmentRequest)
  })
_sym_db.RegisterMessage(EnrollmentRequest)
_sym_db.RegisterMessage(EnrollmentRequest.StatusCode)


DESCRIPTOR._options = None
_ENROLLMENTREQUEST_STATUSCODE._options = None
_ENROLLMENTREQUEST.fields_by_name['insurer']._options = None
_ENROLLMENTREQUEST.fields_by_name['provider']._options = None
_ENROLLMENTREQUEST.fields_by_name['candidate']._options = None
_ENROLLMENTREQUEST.fields_by_name['coverage']._options = None
_ENROLLMENTREQUEST._options = None
# @@protoc_insertion_point(module_scope)
