# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: management.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='management.proto',
  package='wishful_controller.framework',
  serialized_pb=_b('\n\x10management.proto\x12\x1cwishful_controller.framework\"\xd8\x02\n\x07\x43mdDesc\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\x0e\n\x06\x66\x61mily\x18\x02 \x01(\t\x12\x11\n\tfunc_name\x18\x03 \x02(\t\x12\x11\n\texec_time\x18\x04 \x01(\t\x12\x0f\n\x07\x63\x61ll_id\x18\x05 \x01(\t\x12\x11\n\tcaller_id\x18\x06 \x01(\t\x12\x16\n\x0etransaction_id\x18\x07 \x01(\t\x12\x11\n\tinterface\x18\x08 \x01(\t\x12U\n\x12serialization_type\x18\t \x01(\x0e\x32\x33.wishful_controller.framework.CmdDesc.Serialization:\x04NONE\x12\x17\n\x0frepeat_interval\x18\n \x01(\t\x12\x15\n\rrepeat_number\x18\x0b \x01(\r\"3\n\rSerialization\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06PICKLE\x10\x01\x12\x0c\n\x08PROTOBUF\x10\x02\"\"\n\x06\x44\x65vice\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x02(\t\"\xbf\x03\n\x06Module\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x34\n\x06\x64\x65vice\x18\x03 \x01(\x0b\x32$.wishful_controller.framework.Device\x12\x42\n\nattributes\x18\x04 \x03(\x0b\x32..wishful_controller.framework.Module.Attribute\x12@\n\tfunctions\x18\x05 \x03(\x0b\x32-.wishful_controller.framework.Module.Function\x12:\n\x06\x65vents\x18\x06 \x03(\x0b\x32*.wishful_controller.framework.Module.Event\x12>\n\x08services\x18\x07 \x03(\x0b\x32,.wishful_controller.framework.Module.Service\x1a\x19\n\tAttribute\x12\x0c\n\x04name\x18\x01 \x02(\t\x1a\x18\n\x08\x46unction\x12\x0c\n\x04name\x18\x01 \x02(\t\x1a\x15\n\x05\x45vent\x12\x0c\n\x04name\x18\x01 \x02(\t\x1a\x17\n\x07Service\x12\x0c\n\x04name\x18\x01 \x02(\t\"\x80\x01\n\x0bNodeInfoMsg\x12\x12\n\nagent_uuid\x18\x01 \x02(\t\x12\n\n\x02ip\x18\x02 \x02(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04info\x18\x04 \x01(\t\x12\x35\n\x07modules\x18\x05 \x03(\x0b\x32$.wishful_controller.framework.Module\"%\n\x0fNodeInfoRequest\x12\x12\n\nagent_uuid\x18\x01 \x02(\t\"Y\n\nNewNodeAck\x12\x0e\n\x06status\x18\x01 \x02(\x08\x12\x17\n\x0f\x63ontroller_uuid\x18\x02 \x01(\t\x12\x12\n\nagent_uuid\x18\x03 \x01(\t\x12\x0e\n\x06topics\x18\x04 \x03(\t\"1\n\x0bNodeExitMsg\x12\x12\n\nagent_uuid\x18\x01 \x02(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\")\n\x08HelloMsg\x12\x0c\n\x04uuid\x18\x01 \x02(\t\x12\x0f\n\x07timeout\x18\x02 \x02(\r\"\xb1\x05\n\x08RuleDesc\x12;\n\x05\x65vent\x18\x01 \x02(\x0b\x32,.wishful_controller.framework.RuleDesc.Event\x12=\n\x06\x66ilter\x18\x02 \x03(\x0b\x32-.wishful_controller.framework.RuleDesc.Filter\x12;\n\x05match\x18\x03 \x01(\x0b\x32,.wishful_controller.framework.RuleDesc.Match\x12P\n\npermanence\x18\x04 \x01(\x0e\x32\x31.wishful_controller.framework.RuleDesc.Permanence:\tTRANSIENT\x12=\n\x06\x61\x63tion\x18\x05 \x01(\x0b\x32-.wishful_controller.framework.RuleDesc.Action\x12\x10\n\x08\x63\x61llback\x18\x06 \x01(\t\x1a\x62\n\x05\x45vent\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\x11\n\tfunc_name\x18\x02 \x02(\t\x12\x11\n\tinterface\x18\x03 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x04 \x02(\t\x12\x17\n\x0frepeat_interval\x18\x05 \x02(\t\x1aU\n\x06\x46ilter\x12\x13\n\x0b\x66ilter_type\x18\x01 \x02(\t\x12\x1a\n\x12\x66ilter_window_type\x18\x02 \x02(\t\x12\x1a\n\x12\x66ilter_window_size\x18\x03 \x02(\t\x1a)\n\x05Match\x12\x11\n\tcondition\x18\x07 \x02(\t\x12\r\n\x05value\x18\x08 \x02(\t\x1a\x37\n\x06\x41\x63tion\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\x11\n\tfunc_name\x18\x02 \x02(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x02(\t\"*\n\nPermanence\x12\r\n\tTRANSIENT\x10\x00\x12\r\n\tPERMANENT\x10\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CMDDESC_SERIALIZATION = _descriptor.EnumDescriptor(
  name='Serialization',
  full_name='wishful_controller.framework.CmdDesc.Serialization',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PICKLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTOBUF', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=344,
  serialized_end=395,
)
_sym_db.RegisterEnumDescriptor(_CMDDESC_SERIALIZATION)

_RULEDESC_PERMANENCE = _descriptor.EnumDescriptor(
  name='Permanence',
  full_name='wishful_controller.framework.RuleDesc.Permanence',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRANSIENT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERMANENT', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1886,
  serialized_end=1928,
)
_sym_db.RegisterEnumDescriptor(_RULEDESC_PERMANENCE)


_CMDDESC = _descriptor.Descriptor(
  name='CmdDesc',
  full_name='wishful_controller.framework.CmdDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='wishful_controller.framework.CmdDesc.type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='family', full_name='wishful_controller.framework.CmdDesc.family', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='func_name', full_name='wishful_controller.framework.CmdDesc.func_name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exec_time', full_name='wishful_controller.framework.CmdDesc.exec_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='call_id', full_name='wishful_controller.framework.CmdDesc.call_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caller_id', full_name='wishful_controller.framework.CmdDesc.caller_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='wishful_controller.framework.CmdDesc.transaction_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interface', full_name='wishful_controller.framework.CmdDesc.interface', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serialization_type', full_name='wishful_controller.framework.CmdDesc.serialization_type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repeat_interval', full_name='wishful_controller.framework.CmdDesc.repeat_interval', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repeat_number', full_name='wishful_controller.framework.CmdDesc.repeat_number', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CMDDESC_SERIALIZATION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=395,
)


_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='wishful_controller.framework.Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='wishful_controller.framework.Device.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_controller.framework.Device.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=397,
  serialized_end=431,
)


_MODULE_ATTRIBUTE = _descriptor.Descriptor(
  name='Attribute',
  full_name='wishful_controller.framework.Module.Attribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_controller.framework.Module.Attribute.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=782,
  serialized_end=807,
)

_MODULE_FUNCTION = _descriptor.Descriptor(
  name='Function',
  full_name='wishful_controller.framework.Module.Function',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_controller.framework.Module.Function.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=809,
  serialized_end=833,
)

_MODULE_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='wishful_controller.framework.Module.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_controller.framework.Module.Event.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=835,
  serialized_end=856,
)

_MODULE_SERVICE = _descriptor.Descriptor(
  name='Service',
  full_name='wishful_controller.framework.Module.Service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_controller.framework.Module.Service.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=858,
  serialized_end=881,
)

_MODULE = _descriptor.Descriptor(
  name='Module',
  full_name='wishful_controller.framework.Module',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='wishful_controller.framework.Module.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_controller.framework.Module.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device', full_name='wishful_controller.framework.Module.device', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='wishful_controller.framework.Module.attributes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='functions', full_name='wishful_controller.framework.Module.functions', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='events', full_name='wishful_controller.framework.Module.events', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='services', full_name='wishful_controller.framework.Module.services', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MODULE_ATTRIBUTE, _MODULE_FUNCTION, _MODULE_EVENT, _MODULE_SERVICE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=434,
  serialized_end=881,
)


_NODEINFOMSG = _descriptor.Descriptor(
  name='NodeInfoMsg',
  full_name='wishful_controller.framework.NodeInfoMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_uuid', full_name='wishful_controller.framework.NodeInfoMsg.agent_uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip', full_name='wishful_controller.framework.NodeInfoMsg.ip', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_controller.framework.NodeInfoMsg.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='wishful_controller.framework.NodeInfoMsg.info', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modules', full_name='wishful_controller.framework.NodeInfoMsg.modules', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=884,
  serialized_end=1012,
)


_NODEINFOREQUEST = _descriptor.Descriptor(
  name='NodeInfoRequest',
  full_name='wishful_controller.framework.NodeInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_uuid', full_name='wishful_controller.framework.NodeInfoRequest.agent_uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1014,
  serialized_end=1051,
)


_NEWNODEACK = _descriptor.Descriptor(
  name='NewNodeAck',
  full_name='wishful_controller.framework.NewNodeAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wishful_controller.framework.NewNodeAck.status', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='controller_uuid', full_name='wishful_controller.framework.NewNodeAck.controller_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='agent_uuid', full_name='wishful_controller.framework.NewNodeAck.agent_uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topics', full_name='wishful_controller.framework.NewNodeAck.topics', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1053,
  serialized_end=1142,
)


_NODEEXITMSG = _descriptor.Descriptor(
  name='NodeExitMsg',
  full_name='wishful_controller.framework.NodeExitMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_uuid', full_name='wishful_controller.framework.NodeExitMsg.agent_uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='wishful_controller.framework.NodeExitMsg.reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1144,
  serialized_end=1193,
)


_HELLOMSG = _descriptor.Descriptor(
  name='HelloMsg',
  full_name='wishful_controller.framework.HelloMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='wishful_controller.framework.HelloMsg.uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='wishful_controller.framework.HelloMsg.timeout', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1195,
  serialized_end=1236,
)


_RULEDESC_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='wishful_controller.framework.RuleDesc.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='wishful_controller.framework.RuleDesc.Event.type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='func_name', full_name='wishful_controller.framework.RuleDesc.Event.func_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interface', full_name='wishful_controller.framework.RuleDesc.Event.interface', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='args', full_name='wishful_controller.framework.RuleDesc.Event.args', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repeat_interval', full_name='wishful_controller.framework.RuleDesc.Event.repeat_interval', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1599,
  serialized_end=1697,
)

_RULEDESC_FILTER = _descriptor.Descriptor(
  name='Filter',
  full_name='wishful_controller.framework.RuleDesc.Filter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter_type', full_name='wishful_controller.framework.RuleDesc.Filter.filter_type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_window_type', full_name='wishful_controller.framework.RuleDesc.Filter.filter_window_type', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_window_size', full_name='wishful_controller.framework.RuleDesc.Filter.filter_window_size', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1699,
  serialized_end=1784,
)

_RULEDESC_MATCH = _descriptor.Descriptor(
  name='Match',
  full_name='wishful_controller.framework.RuleDesc.Match',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='condition', full_name='wishful_controller.framework.RuleDesc.Match.condition', index=0,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='wishful_controller.framework.RuleDesc.Match.value', index=1,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1786,
  serialized_end=1827,
)

_RULEDESC_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='wishful_controller.framework.RuleDesc.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='wishful_controller.framework.RuleDesc.Action.type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='func_name', full_name='wishful_controller.framework.RuleDesc.Action.func_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='args', full_name='wishful_controller.framework.RuleDesc.Action.args', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1829,
  serialized_end=1884,
)

_RULEDESC = _descriptor.Descriptor(
  name='RuleDesc',
  full_name='wishful_controller.framework.RuleDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='wishful_controller.framework.RuleDesc.event', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter', full_name='wishful_controller.framework.RuleDesc.filter', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match', full_name='wishful_controller.framework.RuleDesc.match', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='permanence', full_name='wishful_controller.framework.RuleDesc.permanence', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='wishful_controller.framework.RuleDesc.action', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='callback', full_name='wishful_controller.framework.RuleDesc.callback', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RULEDESC_EVENT, _RULEDESC_FILTER, _RULEDESC_MATCH, _RULEDESC_ACTION, ],
  enum_types=[
    _RULEDESC_PERMANENCE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1239,
  serialized_end=1928,
)

_CMDDESC.fields_by_name['serialization_type'].enum_type = _CMDDESC_SERIALIZATION
_CMDDESC_SERIALIZATION.containing_type = _CMDDESC
_MODULE_ATTRIBUTE.containing_type = _MODULE
_MODULE_FUNCTION.containing_type = _MODULE
_MODULE_EVENT.containing_type = _MODULE
_MODULE_SERVICE.containing_type = _MODULE
_MODULE.fields_by_name['device'].message_type = _DEVICE
_MODULE.fields_by_name['attributes'].message_type = _MODULE_ATTRIBUTE
_MODULE.fields_by_name['functions'].message_type = _MODULE_FUNCTION
_MODULE.fields_by_name['events'].message_type = _MODULE_EVENT
_MODULE.fields_by_name['services'].message_type = _MODULE_SERVICE
_NODEINFOMSG.fields_by_name['modules'].message_type = _MODULE
_RULEDESC_EVENT.containing_type = _RULEDESC
_RULEDESC_FILTER.containing_type = _RULEDESC
_RULEDESC_MATCH.containing_type = _RULEDESC
_RULEDESC_ACTION.containing_type = _RULEDESC
_RULEDESC.fields_by_name['event'].message_type = _RULEDESC_EVENT
_RULEDESC.fields_by_name['filter'].message_type = _RULEDESC_FILTER
_RULEDESC.fields_by_name['match'].message_type = _RULEDESC_MATCH
_RULEDESC.fields_by_name['permanence'].enum_type = _RULEDESC_PERMANENCE
_RULEDESC.fields_by_name['action'].message_type = _RULEDESC_ACTION
_RULEDESC_PERMANENCE.containing_type = _RULEDESC
DESCRIPTOR.message_types_by_name['CmdDesc'] = _CMDDESC
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
DESCRIPTOR.message_types_by_name['Module'] = _MODULE
DESCRIPTOR.message_types_by_name['NodeInfoMsg'] = _NODEINFOMSG
DESCRIPTOR.message_types_by_name['NodeInfoRequest'] = _NODEINFOREQUEST
DESCRIPTOR.message_types_by_name['NewNodeAck'] = _NEWNODEACK
DESCRIPTOR.message_types_by_name['NodeExitMsg'] = _NODEEXITMSG
DESCRIPTOR.message_types_by_name['HelloMsg'] = _HELLOMSG
DESCRIPTOR.message_types_by_name['RuleDesc'] = _RULEDESC

CmdDesc = _reflection.GeneratedProtocolMessageType('CmdDesc', (_message.Message,), dict(
  DESCRIPTOR = _CMDDESC,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.CmdDesc)
  ))
_sym_db.RegisterMessage(CmdDesc)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), dict(
  DESCRIPTOR = _DEVICE,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.Device)
  ))
_sym_db.RegisterMessage(Device)

Module = _reflection.GeneratedProtocolMessageType('Module', (_message.Message,), dict(

  Attribute = _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), dict(
    DESCRIPTOR = _MODULE_ATTRIBUTE,
    __module__ = 'management_pb2'
    # @@protoc_insertion_point(class_scope:wishful_controller.framework.Module.Attribute)
    ))
  ,

  Function = _reflection.GeneratedProtocolMessageType('Function', (_message.Message,), dict(
    DESCRIPTOR = _MODULE_FUNCTION,
    __module__ = 'management_pb2'
    # @@protoc_insertion_point(class_scope:wishful_controller.framework.Module.Function)
    ))
  ,

  Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
    DESCRIPTOR = _MODULE_EVENT,
    __module__ = 'management_pb2'
    # @@protoc_insertion_point(class_scope:wishful_controller.framework.Module.Event)
    ))
  ,

  Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), dict(
    DESCRIPTOR = _MODULE_SERVICE,
    __module__ = 'management_pb2'
    # @@protoc_insertion_point(class_scope:wishful_controller.framework.Module.Service)
    ))
  ,
  DESCRIPTOR = _MODULE,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.Module)
  ))
_sym_db.RegisterMessage(Module)
_sym_db.RegisterMessage(Module.Attribute)
_sym_db.RegisterMessage(Module.Function)
_sym_db.RegisterMessage(Module.Event)
_sym_db.RegisterMessage(Module.Service)

NodeInfoMsg = _reflection.GeneratedProtocolMessageType('NodeInfoMsg', (_message.Message,), dict(
  DESCRIPTOR = _NODEINFOMSG,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.NodeInfoMsg)
  ))
_sym_db.RegisterMessage(NodeInfoMsg)

NodeInfoRequest = _reflection.GeneratedProtocolMessageType('NodeInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _NODEINFOREQUEST,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.NodeInfoRequest)
  ))
_sym_db.RegisterMessage(NodeInfoRequest)

NewNodeAck = _reflection.GeneratedProtocolMessageType('NewNodeAck', (_message.Message,), dict(
  DESCRIPTOR = _NEWNODEACK,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.NewNodeAck)
  ))
_sym_db.RegisterMessage(NewNodeAck)

NodeExitMsg = _reflection.GeneratedProtocolMessageType('NodeExitMsg', (_message.Message,), dict(
  DESCRIPTOR = _NODEEXITMSG,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.NodeExitMsg)
  ))
_sym_db.RegisterMessage(NodeExitMsg)

HelloMsg = _reflection.GeneratedProtocolMessageType('HelloMsg', (_message.Message,), dict(
  DESCRIPTOR = _HELLOMSG,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.HelloMsg)
  ))
_sym_db.RegisterMessage(HelloMsg)

RuleDesc = _reflection.GeneratedProtocolMessageType('RuleDesc', (_message.Message,), dict(

  Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
    DESCRIPTOR = _RULEDESC_EVENT,
    __module__ = 'management_pb2'
    # @@protoc_insertion_point(class_scope:wishful_controller.framework.RuleDesc.Event)
    ))
  ,

  Filter = _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), dict(
    DESCRIPTOR = _RULEDESC_FILTER,
    __module__ = 'management_pb2'
    # @@protoc_insertion_point(class_scope:wishful_controller.framework.RuleDesc.Filter)
    ))
  ,

  Match = _reflection.GeneratedProtocolMessageType('Match', (_message.Message,), dict(
    DESCRIPTOR = _RULEDESC_MATCH,
    __module__ = 'management_pb2'
    # @@protoc_insertion_point(class_scope:wishful_controller.framework.RuleDesc.Match)
    ))
  ,

  Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), dict(
    DESCRIPTOR = _RULEDESC_ACTION,
    __module__ = 'management_pb2'
    # @@protoc_insertion_point(class_scope:wishful_controller.framework.RuleDesc.Action)
    ))
  ,
  DESCRIPTOR = _RULEDESC,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.RuleDesc)
  ))
_sym_db.RegisterMessage(RuleDesc)
_sym_db.RegisterMessage(RuleDesc.Event)
_sym_db.RegisterMessage(RuleDesc.Filter)
_sym_db.RegisterMessage(RuleDesc.Match)
_sym_db.RegisterMessage(RuleDesc.Action)


# @@protoc_insertion_point(module_scope)
