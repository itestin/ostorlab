# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent_instance_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='agent_instance_settings.proto',
  package='ostorlab.runtimes.proto',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1d\x61gent_instance_settings.proto\x12\x17ostorlab.runtimes.proto\"0\n\x03\x41rg\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04type\x18\x02 \x02(\t\x12\r\n\x05value\x18\x03 \x02(\x0c\"<\n\x0bPortMapping\x12\x13\n\x0bsource_port\x18\x01 \x02(\x11\x12\x18\n\x10\x64\x65stination_port\x18\x02 \x02(\x11\"\x8f\x03\n\x15\x41gentInstanceSettings\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\x0f\n\x07\x62us_url\x18\x02 \x02(\t\x12\x1a\n\x12\x62us_exchange_topic\x18\x03 \x02(\t\x12\x1a\n\x12\x62us_management_url\x18\x04 \x01(\t\x12\x11\n\tbus_vhost\x18\x05 \x01(\t\x12*\n\x04\x61rgs\x18\x06 \x03(\x0b\x32\x1c.ostorlab.runtimes.proto.Arg\x12\x13\n\x0b\x63onstraints\x18\x07 \x03(\t\x12\x0e\n\x06mounts\x18\x08 \x03(\t\x12\x16\n\x0erestart_policy\x18\t \x02(\t\x12\x11\n\tmem_limit\x18\n \x01(\x12\x12\x38\n\nopen_ports\x18\x0b \x03(\x0b\x32$.ostorlab.runtimes.proto.PortMapping\x12\x10\n\x08replicas\x18\x0c \x02(\x11\x12\x18\n\x10healthcheck_host\x18\r \x02(\t\x12\x18\n\x10healthcheck_port\x18\x0e \x02(\x11\x12\x11\n\tredis_url\x18\x0f \x01(\t')
)




_ARG = _descriptor.Descriptor(
  name='Arg',
  full_name='ostorlab.runtimes.proto.Arg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ostorlab.runtimes.proto.Arg.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='ostorlab.runtimes.proto.Arg.type', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ostorlab.runtimes.proto.Arg.value', index=2,
      number=3, type=12, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=106,
)


_PORTMAPPING = _descriptor.Descriptor(
  name='PortMapping',
  full_name='ostorlab.runtimes.proto.PortMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_port', full_name='ostorlab.runtimes.proto.PortMapping.source_port', index=0,
      number=1, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination_port', full_name='ostorlab.runtimes.proto.PortMapping.destination_port', index=1,
      number=2, type=17, cpp_type=1, label=2,
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
  serialized_start=108,
  serialized_end=168,
)


_AGENTINSTANCESETTINGS = _descriptor.Descriptor(
  name='AgentInstanceSettings',
  full_name='ostorlab.runtimes.proto.AgentInstanceSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ostorlab.runtimes.proto.AgentInstanceSettings.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bus_url', full_name='ostorlab.runtimes.proto.AgentInstanceSettings.bus_url', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bus_exchange_topic', full_name='ostorlab.runtimes.proto.AgentInstanceSettings.bus_exchange_topic', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bus_management_url', full_name='ostorlab.runtimes.proto.AgentInstanceSettings.bus_management_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bus_vhost', full_name='ostorlab.runtimes.proto.AgentInstanceSettings.bus_vhost', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='ostorlab.runtimes.proto.AgentInstanceSettings.args', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='constraints', full_name='ostorlab.runtimes.proto.AgentInstanceSettings.constraints', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mounts', full_name='ostorlab.runtimes.proto.AgentInstanceSettings.mounts', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='restart_policy', full_name='ostorlab.runtimes.proto.AgentInstanceSettings.restart_policy', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mem_limit', full_name='ostorlab.runtimes.proto.AgentInstanceSettings.mem_limit', index=9,
      number=10, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='open_ports', full_name='ostorlab.runtimes.proto.AgentInstanceSettings.open_ports', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replicas', full_name='ostorlab.runtimes.proto.AgentInstanceSettings.replicas', index=11,
      number=12, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='healthcheck_host', full_name='ostorlab.runtimes.proto.AgentInstanceSettings.healthcheck_host', index=12,
      number=13, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='healthcheck_port', full_name='ostorlab.runtimes.proto.AgentInstanceSettings.healthcheck_port', index=13,
      number=14, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='redis_url', full_name='ostorlab.runtimes.proto.AgentInstanceSettings.redis_url', index=14,
      number=15, type=9, cpp_type=9, label=1,
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
  serialized_start=171,
  serialized_end=570,
)

_AGENTINSTANCESETTINGS.fields_by_name['args'].message_type = _ARG
_AGENTINSTANCESETTINGS.fields_by_name['open_ports'].message_type = _PORTMAPPING
DESCRIPTOR.message_types_by_name['Arg'] = _ARG
DESCRIPTOR.message_types_by_name['PortMapping'] = _PORTMAPPING
DESCRIPTOR.message_types_by_name['AgentInstanceSettings'] = _AGENTINSTANCESETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Arg = _reflection.GeneratedProtocolMessageType('Arg', (_message.Message,), dict(
  DESCRIPTOR = _ARG,
  __module__ = 'agent_instance_settings_pb2'
  # @@protoc_insertion_point(class_scope:ostorlab.runtimes.proto.Arg)
  ))
_sym_db.RegisterMessage(Arg)

PortMapping = _reflection.GeneratedProtocolMessageType('PortMapping', (_message.Message,), dict(
  DESCRIPTOR = _PORTMAPPING,
  __module__ = 'agent_instance_settings_pb2'
  # @@protoc_insertion_point(class_scope:ostorlab.runtimes.proto.PortMapping)
  ))
_sym_db.RegisterMessage(PortMapping)

AgentInstanceSettings = _reflection.GeneratedProtocolMessageType('AgentInstanceSettings', (_message.Message,), dict(
  DESCRIPTOR = _AGENTINSTANCESETTINGS,
  __module__ = 'agent_instance_settings_pb2'
  # @@protoc_insertion_point(class_scope:ostorlab.runtimes.proto.AgentInstanceSettings)
  ))
_sym_db.RegisterMessage(AgentInstanceSettings)


# @@protoc_insertion_point(module_scope)
