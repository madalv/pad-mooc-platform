# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: course_svc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63ourse_svc.proto\x12\x0cproto.course\"\x16\n\x08\x43ourseId\x12\n\n\x02id\x18\x01 \x01(\t\"\x14\n\x06UserId\x12\n\n\x02id\x18\x01 \x01(\t\"\x18\n\tCourseIds\x12\x0b\n\x03ids\x18\x01 \x03(\t2U\n\rCourseService\x12\x44\n\x13GetCourseIdsForUser\x12\x14.proto.course.UserId\x1a\x17.proto.course.CourseIdsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'course_svc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_COURSEID']._serialized_start=34
  _globals['_COURSEID']._serialized_end=56
  _globals['_USERID']._serialized_start=58
  _globals['_USERID']._serialized_end=78
  _globals['_COURSEIDS']._serialized_start=80
  _globals['_COURSEIDS']._serialized_end=104
  _globals['_COURSESERVICE']._serialized_start=106
  _globals['_COURSESERVICE']._serialized_end=191
# @@protoc_insertion_point(module_scope)
