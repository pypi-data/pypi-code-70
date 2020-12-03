# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/google/fhir/proto/r4/core/profiles/shareable_library.proto
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
  name='proto/google/fhir/proto/r4/core/profiles/shareable_library.proto',
  package='google.fhir.r4.core',
  syntax='proto3',
  serialized_options=b'\n\027com.google.fhir.r4.coreP\001\230\306\260\265\007\004',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n@proto/google/fhir/proto/r4/core/profiles/shareable_library.proto\x12\x13google.fhir.r4.core\x1a\x19google/protobuf/any.proto\x1a)proto/google/fhir/proto/annotations.proto\x1a+proto/google/fhir/proto/r4/core/codes.proto\x1a/proto/google/fhir/proto/r4/core/datatypes.proto\"\xdd\x14\n\x10ShareableLibrary\x12#\n\x02id\x18\x01 \x01(\x0b\x32\x17.google.fhir.r4.core.Id\x12\'\n\x04meta\x18\x02 \x01(\x0b\x32\x19.google.fhir.r4.core.Meta\x12\x30\n\x0eimplicit_rules\x18\x03 \x01(\x0b\x32\x18.google.fhir.r4.core.Uri\x12+\n\x08language\x18\x04 \x01(\x0b\x32\x19.google.fhir.r4.core.Code\x12,\n\x04text\x18\x05 \x01(\x0b\x32\x1e.google.fhir.r4.core.Narrative\x12\'\n\tcontained\x18\x06 \x03(\x0b\x32\x14.google.protobuf.Any\x12\x31\n\textension\x18\x08 \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension\x12:\n\x12modifier_extension\x18\t \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension\x12-\n\x03url\x18\n \x01(\x0b\x32\x18.google.fhir.r4.core.UriB\x06\xf0\xd0\x87\xeb\x04\x01\x12\x33\n\nidentifier\x18\x0b \x03(\x0b\x32\x1f.google.fhir.r4.core.Identifier\x12\x34\n\x07version\x18\x0c \x01(\x0b\x32\x1b.google.fhir.r4.core.StringB\x06\xf0\xd0\x87\xeb\x04\x01\x12\x31\n\x04name\x18\r \x01(\x0b\x32\x1b.google.fhir.r4.core.StringB\x06\xf0\xd0\x87\xeb\x04\x01\x12*\n\x05title\x18\x0e \x01(\x0b\x32\x1b.google.fhir.r4.core.String\x12-\n\x08subtitle\x18\x0f \x01(\x0b\x32\x1b.google.fhir.r4.core.String\x12H\n\x06status\x18\x10 \x01(\x0b\x32\x30.google.fhir.r4.core.ShareableLibrary.StatusCodeB\x06\xf0\xd0\x87\xeb\x04\x01\x12:\n\x0c\x65xperimental\x18\x11 \x01(\x0b\x32\x1c.google.fhir.r4.core.BooleanB\x06\xf0\xd0\x87\xeb\x04\x01\x12:\n\x04type\x18\x12 \x01(\x0b\x32$.google.fhir.r4.core.CodeableConceptB\x06\xf0\xd0\x87\xeb\x04\x01\x12?\n\x07subject\x18\x13 \x01(\x0b\x32..google.fhir.r4.core.ShareableLibrary.SubjectX\x12+\n\x04\x64\x61te\x18\x14 \x01(\x0b\x32\x1d.google.fhir.r4.core.DateTime\x12\x36\n\tpublisher\x18\x15 \x01(\x0b\x32\x1b.google.fhir.r4.core.StringB\x06\xf0\xd0\x87\xeb\x04\x01\x12\x33\n\x07\x63ontact\x18\x16 \x03(\x0b\x32\".google.fhir.r4.core.ContactDetail\x12:\n\x0b\x64\x65scription\x18\x17 \x01(\x0b\x32\x1d.google.fhir.r4.core.MarkdownB\x06\xf0\xd0\x87\xeb\x04\x01\x12\x36\n\x0buse_context\x18\x18 \x03(\x0b\x32!.google.fhir.r4.core.UsageContext\x12:\n\x0cjurisdiction\x18\x19 \x03(\x0b\x32$.google.fhir.r4.core.CodeableConcept\x12.\n\x07purpose\x18\x1a \x01(\x0b\x32\x1d.google.fhir.r4.core.Markdown\x12*\n\x05usage\x18\x1b \x01(\x0b\x32\x1b.google.fhir.r4.core.String\x12\x30\n\tcopyright\x18\x1c \x01(\x0b\x32\x1d.google.fhir.r4.core.Markdown\x12\x30\n\rapproval_date\x18\x1d \x01(\x0b\x32\x19.google.fhir.r4.core.Date\x12\x33\n\x10last_review_date\x18\x1e \x01(\x0b\x32\x19.google.fhir.r4.core.Date\x12\x35\n\x10\x65\x66\x66\x65\x63tive_period\x18\x1f \x01(\x0b\x32\x1b.google.fhir.r4.core.Period\x12\x33\n\x05topic\x18  \x03(\x0b\x32$.google.fhir.r4.core.CodeableConcept\x12\x32\n\x06\x61uthor\x18! \x03(\x0b\x32\".google.fhir.r4.core.ContactDetail\x12\x32\n\x06\x65\x64itor\x18\" \x03(\x0b\x32\".google.fhir.r4.core.ContactDetail\x12\x34\n\x08reviewer\x18# \x03(\x0b\x32\".google.fhir.r4.core.ContactDetail\x12\x34\n\x08\x65ndorser\x18$ \x03(\x0b\x32\".google.fhir.r4.core.ContactDetail\x12>\n\x10related_artifact\x18% \x03(\x0b\x32$.google.fhir.r4.core.RelatedArtifact\x12;\n\tparameter\x18& \x03(\x0b\x32(.google.fhir.r4.core.ParameterDefinition\x12>\n\x10\x64\x61ta_requirement\x18\' \x03(\x0b\x32$.google.fhir.r4.core.DataRequirement\x12\x30\n\x07\x63ontent\x18( \x03(\x0b\x32\x1f.google.fhir.r4.core.Attachment\x1a\x98\x02\n\nStatusCode\x12?\n\x05value\x18\x01 \x01(\x0e\x32\x30.google.fhir.r4.core.PublicationStatusCode.Value\x12\'\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.fhir.r4.core.String\x12\x31\n\textension\x18\x03 \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension:m\xc0\x9f\xe3\xb6\x05\x01\x8a\xf9\x83\xb2\x05/http://hl7.org/fhir/ValueSet/publication-status\x9a\xb5\x8e\x93\x06,http://hl7.org/fhir/StructureDefinition/code\x1a\xa0\x01\n\x08SubjectX\x12@\n\x10\x63odeable_concept\x18\x01 \x01(\x0b\x32$.google.fhir.r4.core.CodeableConceptH\x00\x12@\n\treference\x18\x02 \x01(\x0b\x32\x1e.google.fhir.r4.core.ReferenceB\x0b\xf2\xff\xfc\xc2\x06\x05GroupH\x00:\x06\xa0\x83\x83\xe8\x06\x01\x42\x08\n\x06\x63hoice:y\xc0\x9f\xe3\xb6\x05\x03\x9a\xb5\x8e\x93\x06/http://hl7.org/fhir/StructureDefinition/Library\xb2\xfe\xe4\x97\x06\x38http://hl7.org/fhir/StructureDefinition/shareablelibraryJ\x04\x08\x07\x10\x08\x42!\n\x17\x63om.google.fhir.r4.coreP\x01\x98\xc6\xb0\xb5\x07\x04\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,proto_dot_google_dot_fhir_dot_proto_dot_annotations__pb2.DESCRIPTOR,proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_codes__pb2.DESCRIPTOR,proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2.DESCRIPTOR,])




_SHAREABLELIBRARY_STATUSCODE = _descriptor.Descriptor(
  name='StatusCode',
  full_name='google.fhir.r4.core.ShareableLibrary.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='google.fhir.r4.core.ShareableLibrary.StatusCode.value', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.r4.core.ShareableLibrary.StatusCode.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extension', full_name='google.fhir.r4.core.ShareableLibrary.StatusCode.extension', index=2,
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
  serialized_options=b'\300\237\343\266\005\001\212\371\203\262\005/http://hl7.org/fhir/ValueSet/publication-status\232\265\216\223\006,http://hl7.org/fhir/StructureDefinition/code',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2335,
  serialized_end=2615,
)

_SHAREABLELIBRARY_SUBJECTX = _descriptor.Descriptor(
  name='SubjectX',
  full_name='google.fhir.r4.core.ShareableLibrary.SubjectX',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='codeable_concept', full_name='google.fhir.r4.core.ShareableLibrary.SubjectX.codeable_concept', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reference', full_name='google.fhir.r4.core.ShareableLibrary.SubjectX.reference', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\377\374\302\006\005Group', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\240\203\203\350\006\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='choice', full_name='google.fhir.r4.core.ShareableLibrary.SubjectX.choice',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=2618,
  serialized_end=2778,
)

_SHAREABLELIBRARY = _descriptor.Descriptor(
  name='ShareableLibrary',
  full_name='google.fhir.r4.core.ShareableLibrary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.r4.core.ShareableLibrary.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='google.fhir.r4.core.ShareableLibrary.meta', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='implicit_rules', full_name='google.fhir.r4.core.ShareableLibrary.implicit_rules', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='google.fhir.r4.core.ShareableLibrary.language', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='google.fhir.r4.core.ShareableLibrary.text', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contained', full_name='google.fhir.r4.core.ShareableLibrary.contained', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extension', full_name='google.fhir.r4.core.ShareableLibrary.extension', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='modifier_extension', full_name='google.fhir.r4.core.ShareableLibrary.modifier_extension', index=7,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='google.fhir.r4.core.ShareableLibrary.url', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360\320\207\353\004\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='google.fhir.r4.core.ShareableLibrary.identifier', index=9,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='google.fhir.r4.core.ShareableLibrary.version', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360\320\207\353\004\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.fhir.r4.core.ShareableLibrary.name', index=11,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360\320\207\353\004\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='google.fhir.r4.core.ShareableLibrary.title', index=12,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subtitle', full_name='google.fhir.r4.core.ShareableLibrary.subtitle', index=13,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.fhir.r4.core.ShareableLibrary.status', index=14,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360\320\207\353\004\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='experimental', full_name='google.fhir.r4.core.ShareableLibrary.experimental', index=15,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360\320\207\353\004\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.fhir.r4.core.ShareableLibrary.type', index=16,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360\320\207\353\004\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subject', full_name='google.fhir.r4.core.ShareableLibrary.subject', index=17,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date', full_name='google.fhir.r4.core.ShareableLibrary.date', index=18,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='publisher', full_name='google.fhir.r4.core.ShareableLibrary.publisher', index=19,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360\320\207\353\004\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contact', full_name='google.fhir.r4.core.ShareableLibrary.contact', index=20,
      number=22, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.fhir.r4.core.ShareableLibrary.description', index=21,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360\320\207\353\004\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_context', full_name='google.fhir.r4.core.ShareableLibrary.use_context', index=22,
      number=24, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jurisdiction', full_name='google.fhir.r4.core.ShareableLibrary.jurisdiction', index=23,
      number=25, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='purpose', full_name='google.fhir.r4.core.ShareableLibrary.purpose', index=24,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='usage', full_name='google.fhir.r4.core.ShareableLibrary.usage', index=25,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='copyright', full_name='google.fhir.r4.core.ShareableLibrary.copyright', index=26,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='approval_date', full_name='google.fhir.r4.core.ShareableLibrary.approval_date', index=27,
      number=29, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_review_date', full_name='google.fhir.r4.core.ShareableLibrary.last_review_date', index=28,
      number=30, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='effective_period', full_name='google.fhir.r4.core.ShareableLibrary.effective_period', index=29,
      number=31, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topic', full_name='google.fhir.r4.core.ShareableLibrary.topic', index=30,
      number=32, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='author', full_name='google.fhir.r4.core.ShareableLibrary.author', index=31,
      number=33, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='editor', full_name='google.fhir.r4.core.ShareableLibrary.editor', index=32,
      number=34, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reviewer', full_name='google.fhir.r4.core.ShareableLibrary.reviewer', index=33,
      number=35, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endorser', full_name='google.fhir.r4.core.ShareableLibrary.endorser', index=34,
      number=36, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='related_artifact', full_name='google.fhir.r4.core.ShareableLibrary.related_artifact', index=35,
      number=37, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameter', full_name='google.fhir.r4.core.ShareableLibrary.parameter', index=36,
      number=38, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_requirement', full_name='google.fhir.r4.core.ShareableLibrary.data_requirement', index=37,
      number=39, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='google.fhir.r4.core.ShareableLibrary.content', index=38,
      number=40, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SHAREABLELIBRARY_STATUSCODE, _SHAREABLELIBRARY_SUBJECTX, ],
  enum_types=[
  ],
  serialized_options=b'\300\237\343\266\005\003\232\265\216\223\006/http://hl7.org/fhir/StructureDefinition/Library\262\376\344\227\0068http://hl7.org/fhir/StructureDefinition/shareablelibrary',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=254,
  serialized_end=2907,
)

_SHAREABLELIBRARY_STATUSCODE.fields_by_name['value'].enum_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_codes__pb2._PUBLICATIONSTATUSCODE_VALUE
_SHAREABLELIBRARY_STATUSCODE.fields_by_name['id'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._STRING
_SHAREABLELIBRARY_STATUSCODE.fields_by_name['extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_SHAREABLELIBRARY_STATUSCODE.containing_type = _SHAREABLELIBRARY
_SHAREABLELIBRARY_SUBJECTX.fields_by_name['codeable_concept'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CODEABLECONCEPT
_SHAREABLELIBRARY_SUBJECTX.fields_by_name['reference'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._REFERENCE
_SHAREABLELIBRARY_SUBJECTX.containing_type = _SHAREABLELIBRARY
_SHAREABLELIBRARY_SUBJECTX.oneofs_by_name['choice'].fields.append(
  _SHAREABLELIBRARY_SUBJECTX.fields_by_name['codeable_concept'])
_SHAREABLELIBRARY_SUBJECTX.fields_by_name['codeable_concept'].containing_oneof = _SHAREABLELIBRARY_SUBJECTX.oneofs_by_name['choice']
_SHAREABLELIBRARY_SUBJECTX.oneofs_by_name['choice'].fields.append(
  _SHAREABLELIBRARY_SUBJECTX.fields_by_name['reference'])
_SHAREABLELIBRARY_SUBJECTX.fields_by_name['reference'].containing_oneof = _SHAREABLELIBRARY_SUBJECTX.oneofs_by_name['choice']
_SHAREABLELIBRARY.fields_by_name['id'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._ID
_SHAREABLELIBRARY.fields_by_name['meta'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._META
_SHAREABLELIBRARY.fields_by_name['implicit_rules'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._URI
_SHAREABLELIBRARY.fields_by_name['language'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CODE
_SHAREABLELIBRARY.fields_by_name['text'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._NARRATIVE
_SHAREABLELIBRARY.fields_by_name['contained'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_SHAREABLELIBRARY.fields_by_name['extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_SHAREABLELIBRARY.fields_by_name['modifier_extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_SHAREABLELIBRARY.fields_by_name['url'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._URI
_SHAREABLELIBRARY.fields_by_name['identifier'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._IDENTIFIER
_SHAREABLELIBRARY.fields_by_name['version'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._STRING
_SHAREABLELIBRARY.fields_by_name['name'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._STRING
_SHAREABLELIBRARY.fields_by_name['title'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._STRING
_SHAREABLELIBRARY.fields_by_name['subtitle'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._STRING
_SHAREABLELIBRARY.fields_by_name['status'].message_type = _SHAREABLELIBRARY_STATUSCODE
_SHAREABLELIBRARY.fields_by_name['experimental'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._BOOLEAN
_SHAREABLELIBRARY.fields_by_name['type'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CODEABLECONCEPT
_SHAREABLELIBRARY.fields_by_name['subject'].message_type = _SHAREABLELIBRARY_SUBJECTX
_SHAREABLELIBRARY.fields_by_name['date'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._DATETIME
_SHAREABLELIBRARY.fields_by_name['publisher'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._STRING
_SHAREABLELIBRARY.fields_by_name['contact'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CONTACTDETAIL
_SHAREABLELIBRARY.fields_by_name['description'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._MARKDOWN
_SHAREABLELIBRARY.fields_by_name['use_context'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._USAGECONTEXT
_SHAREABLELIBRARY.fields_by_name['jurisdiction'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CODEABLECONCEPT
_SHAREABLELIBRARY.fields_by_name['purpose'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._MARKDOWN
_SHAREABLELIBRARY.fields_by_name['usage'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._STRING
_SHAREABLELIBRARY.fields_by_name['copyright'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._MARKDOWN
_SHAREABLELIBRARY.fields_by_name['approval_date'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._DATE
_SHAREABLELIBRARY.fields_by_name['last_review_date'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._DATE
_SHAREABLELIBRARY.fields_by_name['effective_period'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._PERIOD
_SHAREABLELIBRARY.fields_by_name['topic'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CODEABLECONCEPT
_SHAREABLELIBRARY.fields_by_name['author'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CONTACTDETAIL
_SHAREABLELIBRARY.fields_by_name['editor'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CONTACTDETAIL
_SHAREABLELIBRARY.fields_by_name['reviewer'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CONTACTDETAIL
_SHAREABLELIBRARY.fields_by_name['endorser'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CONTACTDETAIL
_SHAREABLELIBRARY.fields_by_name['related_artifact'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._RELATEDARTIFACT
_SHAREABLELIBRARY.fields_by_name['parameter'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._PARAMETERDEFINITION
_SHAREABLELIBRARY.fields_by_name['data_requirement'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._DATAREQUIREMENT
_SHAREABLELIBRARY.fields_by_name['content'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._ATTACHMENT
DESCRIPTOR.message_types_by_name['ShareableLibrary'] = _SHAREABLELIBRARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ShareableLibrary = _reflection.GeneratedProtocolMessageType('ShareableLibrary', (_message.Message,), {

  'StatusCode' : _reflection.GeneratedProtocolMessageType('StatusCode', (_message.Message,), {
    'DESCRIPTOR' : _SHAREABLELIBRARY_STATUSCODE,
    '__module__' : 'proto.google.fhir.proto.r4.core.profiles.shareable_library_pb2'
    # @@protoc_insertion_point(class_scope:google.fhir.r4.core.ShareableLibrary.StatusCode)
    })
  ,

  'SubjectX' : _reflection.GeneratedProtocolMessageType('SubjectX', (_message.Message,), {
    'DESCRIPTOR' : _SHAREABLELIBRARY_SUBJECTX,
    '__module__' : 'proto.google.fhir.proto.r4.core.profiles.shareable_library_pb2'
    # @@protoc_insertion_point(class_scope:google.fhir.r4.core.ShareableLibrary.SubjectX)
    })
  ,
  'DESCRIPTOR' : _SHAREABLELIBRARY,
  '__module__' : 'proto.google.fhir.proto.r4.core.profiles.shareable_library_pb2'
  # @@protoc_insertion_point(class_scope:google.fhir.r4.core.ShareableLibrary)
  })
_sym_db.RegisterMessage(ShareableLibrary)
_sym_db.RegisterMessage(ShareableLibrary.StatusCode)
_sym_db.RegisterMessage(ShareableLibrary.SubjectX)


DESCRIPTOR._options = None
_SHAREABLELIBRARY_STATUSCODE._options = None
_SHAREABLELIBRARY_SUBJECTX.fields_by_name['reference']._options = None
_SHAREABLELIBRARY_SUBJECTX._options = None
_SHAREABLELIBRARY.fields_by_name['url']._options = None
_SHAREABLELIBRARY.fields_by_name['version']._options = None
_SHAREABLELIBRARY.fields_by_name['name']._options = None
_SHAREABLELIBRARY.fields_by_name['status']._options = None
_SHAREABLELIBRARY.fields_by_name['experimental']._options = None
_SHAREABLELIBRARY.fields_by_name['type']._options = None
_SHAREABLELIBRARY.fields_by_name['publisher']._options = None
_SHAREABLELIBRARY.fields_by_name['description']._options = None
_SHAREABLELIBRARY._options = None
# @@protoc_insertion_point(module_scope)
