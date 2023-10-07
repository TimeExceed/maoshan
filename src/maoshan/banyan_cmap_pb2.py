# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: banyan_cmap.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='banyan_cmap.proto',
  package='banyan',
  syntax='proto3',
  serialized_options=b'Z\003/pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x62\x61nyan_cmap.proto\x12\x06\x62\x61nyan\"6\n\x04Tile\x12\x0e\n\x06supply\x18\x01 \x01(\x01\x12\x0e\n\x06\x64\x65mand\x18\x02 \x01(\x01\x12\x0e\n\x06\x61\x63tive\x18\x03 \x01(\x08\"\x89\x01\n\x04\x43map\x12\x0e\n\x06wgrids\x18\x01 \x01(\x03\x12\x0e\n\x06hgrids\x18\x02 \x01(\x03\x12\x11\n\ttileWidth\x18\x03 \x01(\x01\x12\x12\n\ntileHeight\x18\x04 \x01(\x01\x12\x1c\n\x06vtiles\x18\x05 \x03(\x0b\x32\x0c.banyan.Tile\x12\x1c\n\x06htiles\x18\x06 \x03(\x0b\x32\x0c.banyan.TileB\x05Z\x03/pbb\x06proto3'
)




_TILE = _descriptor.Descriptor(
  name='Tile',
  full_name='banyan.Tile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='supply', full_name='banyan.Tile.supply', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='demand', full_name='banyan.Tile.demand', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active', full_name='banyan.Tile.active', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=29,
  serialized_end=83,
)


_CMAP = _descriptor.Descriptor(
  name='Cmap',
  full_name='banyan.Cmap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='wgrids', full_name='banyan.Cmap.wgrids', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hgrids', full_name='banyan.Cmap.hgrids', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tileWidth', full_name='banyan.Cmap.tileWidth', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tileHeight', full_name='banyan.Cmap.tileHeight', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vtiles', full_name='banyan.Cmap.vtiles', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='htiles', full_name='banyan.Cmap.htiles', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=86,
  serialized_end=223,
)

_CMAP.fields_by_name['vtiles'].message_type = _TILE
_CMAP.fields_by_name['htiles'].message_type = _TILE
DESCRIPTOR.message_types_by_name['Tile'] = _TILE
DESCRIPTOR.message_types_by_name['Cmap'] = _CMAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Tile = _reflection.GeneratedProtocolMessageType('Tile', (_message.Message,), {
  'DESCRIPTOR' : _TILE,
  '__module__' : 'banyan_cmap_pb2'
  # @@protoc_insertion_point(class_scope:banyan.Tile)
  })
_sym_db.RegisterMessage(Tile)

Cmap = _reflection.GeneratedProtocolMessageType('Cmap', (_message.Message,), {
  'DESCRIPTOR' : _CMAP,
  '__module__' : 'banyan_cmap_pb2'
  # @@protoc_insertion_point(class_scope:banyan.Cmap)
  })
_sym_db.RegisterMessage(Cmap)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
