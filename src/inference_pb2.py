# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inference.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finference.proto\"!\n\x10InferenceRequest\x12\r\n\x05image\x18\x01 \x03(\x0c\"\x1e\n\x0eInferenceReply\x12\x0c\n\x04pred\x18\x01 \x03(\r2D\n\x0fInferenceServer\x12\x31\n\tinference\x12\x11.InferenceRequest\x1a\x0f.InferenceReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inference_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INFERENCEREQUEST._serialized_start=19
  _INFERENCEREQUEST._serialized_end=52
  _INFERENCEREPLY._serialized_start=54
  _INFERENCEREPLY._serialized_end=84
  _INFERENCESERVER._serialized_start=86
  _INFERENCESERVER._serialized_end=154
# @@protoc_insertion_point(module_scope)
