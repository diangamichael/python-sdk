# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ussd.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ussd.proto',
  package='com.elarian.hera.proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nussd.proto\x12\x16\x63om.elarian.hera.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x0c\x63ommon.proto\"\xec\x02\n\x15UssdSessionStateEntry\x12?\n\x0f\x63ustomer_number\x18\x01 \x01(\x0b\x32&.com.elarian.hera.proto.CustomerNumber\x12\x41\n\x0e\x63hannel_number\x18\x02 \x01(\x0b\x32).com.elarian.hera.proto.UssdChannelNumber\x12\x12\n\nsession_id\x18\x03 \x01(\t\x12,\n\x06\x61pp_id\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x04hops\x18\x05 \x03(\x0b\x32\x1f.com.elarian.hera.proto.UssdHop\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xd2\x01\n\tUssdState\x12?\n\x08sessions\x18\x01 \x03(\x0b\x32-.com.elarian.hera.proto.UssdSessionStateEntry\x12@\n\x10\x63ustomer_numbers\x18\x02 \x03(\x0b\x32&.com.elarian.hera.proto.CustomerNumber\x12\x42\n\x0f\x63hannel_numbers\x18\x03 \x03(\x0b\x32).com.elarian.hera.proto.UssdChannelNumber\"\x81\x02\n\tUssdEvent\x12\x46\n\rstate_adopted\x18\x01 \x01(\x0b\x32-.com.elarian.hera.proto.UssdStateAdoptedEventH\x00\x12V\n\x15\x65ntity_decommissioned\x18\x02 \x01(\x0b\x32\x35.com.elarian.hera.proto.UssdEntityDecommissionedEventH\x00\x12K\n\x12ussd_hop_completed\x18\x03 \x01(\x0b\x32-.com.elarian.hera.proto.UssdHopCompletedEventH\x00\x42\x07\n\x05\x65vent\"\xfc\x01\n\x15UssdStateAdoptedEvent\x12\x0e\n\x06org_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63ustomer_id\x18\x02 \x01(\t\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x0b\x61pp_headers\x18\x04 \x01(\x0b\x32\".com.elarian.hera.proto.AppHeaders\x12\x19\n\x11other_customer_id\x18\x05 \x01(\t\x12;\n\x10other_ussd_state\x18\x06 \x01(\x0b\x32!.com.elarian.hera.proto.UssdState\"\xc5\x01\n\x1dUssdEntityDecommissionedEvent\x12\x0e\n\x06org_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63ustomer_id\x18\x02 \x01(\t\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x0b\x61pp_headers\x18\x04 \x01(\x0b\x32\".com.elarian.hera.proto.AppHeaders\x12\x17\n\x0fnew_customer_id\x18\x05 \x01(\t\"\xdf\x02\n\x15UssdHopCompletedEvent\x12\x0e\n\x06org_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63ustomer_id\x18\x02 \x01(\t\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x06\x61pp_id\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x12\n\nsession_id\x18\x05 \x01(\t\x12?\n\x0f\x63ustomer_number\x18\x06 \x01(\x0b\x32&.com.elarian.hera.proto.CustomerNumber\x12\x41\n\x0e\x63hannel_number\x18\x07 \x01(\x0b\x32).com.elarian.hera.proto.UssdChannelNumber\x12,\n\x03hop\x18\x08 \x01(\x0b\x32\x1f.com.elarian.hera.proto.UssdHopb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,common__pb2.DESCRIPTOR,])




_USSDSESSIONSTATEENTRY = _descriptor.Descriptor(
  name='UssdSessionStateEntry',
  full_name='com.elarian.hera.proto.UssdSessionStateEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_number', full_name='com.elarian.hera.proto.UssdSessionStateEntry.customer_number', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_number', full_name='com.elarian.hera.proto.UssdSessionStateEntry.channel_number', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='com.elarian.hera.proto.UssdSessionStateEntry.session_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='com.elarian.hera.proto.UssdSessionStateEntry.app_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hops', full_name='com.elarian.hera.proto.UssdSessionStateEntry.hops', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='com.elarian.hera.proto.UssdSessionStateEntry.created_at', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='com.elarian.hera.proto.UssdSessionStateEntry.updated_at', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=118,
  serialized_end=482,
)


_USSDSTATE = _descriptor.Descriptor(
  name='UssdState',
  full_name='com.elarian.hera.proto.UssdState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sessions', full_name='com.elarian.hera.proto.UssdState.sessions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='customer_numbers', full_name='com.elarian.hera.proto.UssdState.customer_numbers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_numbers', full_name='com.elarian.hera.proto.UssdState.channel_numbers', index=2,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=485,
  serialized_end=695,
)


_USSDEVENT = _descriptor.Descriptor(
  name='UssdEvent',
  full_name='com.elarian.hera.proto.UssdEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state_adopted', full_name='com.elarian.hera.proto.UssdEvent.state_adopted', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity_decommissioned', full_name='com.elarian.hera.proto.UssdEvent.entity_decommissioned', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ussd_hop_completed', full_name='com.elarian.hera.proto.UssdEvent.ussd_hop_completed', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='event', full_name='com.elarian.hera.proto.UssdEvent.event',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=698,
  serialized_end=955,
)


_USSDSTATEADOPTEDEVENT = _descriptor.Descriptor(
  name='UssdStateAdoptedEvent',
  full_name='com.elarian.hera.proto.UssdStateAdoptedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='org_id', full_name='com.elarian.hera.proto.UssdStateAdoptedEvent.org_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='com.elarian.hera.proto.UssdStateAdoptedEvent.customer_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='com.elarian.hera.proto.UssdStateAdoptedEvent.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_headers', full_name='com.elarian.hera.proto.UssdStateAdoptedEvent.app_headers', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='other_customer_id', full_name='com.elarian.hera.proto.UssdStateAdoptedEvent.other_customer_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='other_ussd_state', full_name='com.elarian.hera.proto.UssdStateAdoptedEvent.other_ussd_state', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=958,
  serialized_end=1210,
)


_USSDENTITYDECOMMISSIONEDEVENT = _descriptor.Descriptor(
  name='UssdEntityDecommissionedEvent',
  full_name='com.elarian.hera.proto.UssdEntityDecommissionedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='org_id', full_name='com.elarian.hera.proto.UssdEntityDecommissionedEvent.org_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='com.elarian.hera.proto.UssdEntityDecommissionedEvent.customer_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='com.elarian.hera.proto.UssdEntityDecommissionedEvent.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_headers', full_name='com.elarian.hera.proto.UssdEntityDecommissionedEvent.app_headers', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_customer_id', full_name='com.elarian.hera.proto.UssdEntityDecommissionedEvent.new_customer_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1213,
  serialized_end=1410,
)


_USSDHOPCOMPLETEDEVENT = _descriptor.Descriptor(
  name='UssdHopCompletedEvent',
  full_name='com.elarian.hera.proto.UssdHopCompletedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='org_id', full_name='com.elarian.hera.proto.UssdHopCompletedEvent.org_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='com.elarian.hera.proto.UssdHopCompletedEvent.customer_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='com.elarian.hera.proto.UssdHopCompletedEvent.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='com.elarian.hera.proto.UssdHopCompletedEvent.app_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='com.elarian.hera.proto.UssdHopCompletedEvent.session_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='customer_number', full_name='com.elarian.hera.proto.UssdHopCompletedEvent.customer_number', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_number', full_name='com.elarian.hera.proto.UssdHopCompletedEvent.channel_number', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hop', full_name='com.elarian.hera.proto.UssdHopCompletedEvent.hop', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1413,
  serialized_end=1764,
)

_USSDSESSIONSTATEENTRY.fields_by_name['customer_number'].message_type = common__pb2._CUSTOMERNUMBER
_USSDSESSIONSTATEENTRY.fields_by_name['channel_number'].message_type = common__pb2._USSDCHANNELNUMBER
_USSDSESSIONSTATEENTRY.fields_by_name['app_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_USSDSESSIONSTATEENTRY.fields_by_name['hops'].message_type = common__pb2._USSDHOP
_USSDSESSIONSTATEENTRY.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_USSDSESSIONSTATEENTRY.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_USSDSTATE.fields_by_name['sessions'].message_type = _USSDSESSIONSTATEENTRY
_USSDSTATE.fields_by_name['customer_numbers'].message_type = common__pb2._CUSTOMERNUMBER
_USSDSTATE.fields_by_name['channel_numbers'].message_type = common__pb2._USSDCHANNELNUMBER
_USSDEVENT.fields_by_name['state_adopted'].message_type = _USSDSTATEADOPTEDEVENT
_USSDEVENT.fields_by_name['entity_decommissioned'].message_type = _USSDENTITYDECOMMISSIONEDEVENT
_USSDEVENT.fields_by_name['ussd_hop_completed'].message_type = _USSDHOPCOMPLETEDEVENT
_USSDEVENT.oneofs_by_name['event'].fields.append(
  _USSDEVENT.fields_by_name['state_adopted'])
_USSDEVENT.fields_by_name['state_adopted'].containing_oneof = _USSDEVENT.oneofs_by_name['event']
_USSDEVENT.oneofs_by_name['event'].fields.append(
  _USSDEVENT.fields_by_name['entity_decommissioned'])
_USSDEVENT.fields_by_name['entity_decommissioned'].containing_oneof = _USSDEVENT.oneofs_by_name['event']
_USSDEVENT.oneofs_by_name['event'].fields.append(
  _USSDEVENT.fields_by_name['ussd_hop_completed'])
_USSDEVENT.fields_by_name['ussd_hop_completed'].containing_oneof = _USSDEVENT.oneofs_by_name['event']
_USSDSTATEADOPTEDEVENT.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_USSDSTATEADOPTEDEVENT.fields_by_name['app_headers'].message_type = common__pb2._APPHEADERS
_USSDSTATEADOPTEDEVENT.fields_by_name['other_ussd_state'].message_type = _USSDSTATE
_USSDENTITYDECOMMISSIONEDEVENT.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_USSDENTITYDECOMMISSIONEDEVENT.fields_by_name['app_headers'].message_type = common__pb2._APPHEADERS
_USSDHOPCOMPLETEDEVENT.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_USSDHOPCOMPLETEDEVENT.fields_by_name['app_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_USSDHOPCOMPLETEDEVENT.fields_by_name['customer_number'].message_type = common__pb2._CUSTOMERNUMBER
_USSDHOPCOMPLETEDEVENT.fields_by_name['channel_number'].message_type = common__pb2._USSDCHANNELNUMBER
_USSDHOPCOMPLETEDEVENT.fields_by_name['hop'].message_type = common__pb2._USSDHOP
DESCRIPTOR.message_types_by_name['UssdSessionStateEntry'] = _USSDSESSIONSTATEENTRY
DESCRIPTOR.message_types_by_name['UssdState'] = _USSDSTATE
DESCRIPTOR.message_types_by_name['UssdEvent'] = _USSDEVENT
DESCRIPTOR.message_types_by_name['UssdStateAdoptedEvent'] = _USSDSTATEADOPTEDEVENT
DESCRIPTOR.message_types_by_name['UssdEntityDecommissionedEvent'] = _USSDENTITYDECOMMISSIONEDEVENT
DESCRIPTOR.message_types_by_name['UssdHopCompletedEvent'] = _USSDHOPCOMPLETEDEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UssdSessionStateEntry = _reflection.GeneratedProtocolMessageType('UssdSessionStateEntry', (_message.Message,), {
  'DESCRIPTOR' : _USSDSESSIONSTATEENTRY,
  '__module__' : 'ussd_pb2'
  # @@protoc_insertion_point(class_scope:com.elarian.hera.proto.UssdSessionStateEntry)
  })
_sym_db.RegisterMessage(UssdSessionStateEntry)

UssdState = _reflection.GeneratedProtocolMessageType('UssdState', (_message.Message,), {
  'DESCRIPTOR' : _USSDSTATE,
  '__module__' : 'ussd_pb2'
  # @@protoc_insertion_point(class_scope:com.elarian.hera.proto.UssdState)
  })
_sym_db.RegisterMessage(UssdState)

UssdEvent = _reflection.GeneratedProtocolMessageType('UssdEvent', (_message.Message,), {
  'DESCRIPTOR' : _USSDEVENT,
  '__module__' : 'ussd_pb2'
  # @@protoc_insertion_point(class_scope:com.elarian.hera.proto.UssdEvent)
  })
_sym_db.RegisterMessage(UssdEvent)

UssdStateAdoptedEvent = _reflection.GeneratedProtocolMessageType('UssdStateAdoptedEvent', (_message.Message,), {
  'DESCRIPTOR' : _USSDSTATEADOPTEDEVENT,
  '__module__' : 'ussd_pb2'
  # @@protoc_insertion_point(class_scope:com.elarian.hera.proto.UssdStateAdoptedEvent)
  })
_sym_db.RegisterMessage(UssdStateAdoptedEvent)

UssdEntityDecommissionedEvent = _reflection.GeneratedProtocolMessageType('UssdEntityDecommissionedEvent', (_message.Message,), {
  'DESCRIPTOR' : _USSDENTITYDECOMMISSIONEDEVENT,
  '__module__' : 'ussd_pb2'
  # @@protoc_insertion_point(class_scope:com.elarian.hera.proto.UssdEntityDecommissionedEvent)
  })
_sym_db.RegisterMessage(UssdEntityDecommissionedEvent)

UssdHopCompletedEvent = _reflection.GeneratedProtocolMessageType('UssdHopCompletedEvent', (_message.Message,), {
  'DESCRIPTOR' : _USSDHOPCOMPLETEDEVENT,
  '__module__' : 'ussd_pb2'
  # @@protoc_insertion_point(class_scope:com.elarian.hera.proto.UssdHopCompletedEvent)
  })
_sym_db.RegisterMessage(UssdHopCompletedEvent)


# @@protoc_insertion_point(module_scope)
