# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rec_svc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rrec_svc.proto\x12\x05proto\x1a\x1bgoogle/protobuf/empty.proto\"7\n\x11\x43ourseRecsRequest\x12\x11\n\tcourse_id\x18\x01 \x01(\t\x12\x0f\n\x07recs_nr\x18\x02 \x01(\x04\"3\n\x0fUserRecsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0f\n\x07recs_nr\x18\x02 \x01(\x04\"\\\n\x06\x43ourse\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x12\n\ncategories\x18\x04 \x03(\t\x12\x0e\n\x06\x61uthor\x18\x05 \x01(\t\"&\n\tCourseRec\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\".\n\x0cRecsResponse\x12\x1e\n\x04recs\x18\x01 \x03(\x0b\x32\x10.proto.CourseRec2\xc2\x01\n\nRecService\x12\x41\n\x10GetRecsForCourse\x12\x18.proto.CourseRecsRequest\x1a\x13.proto.RecsResponse\x12=\n\x0eGetRecsForUser\x12\x16.proto.UserRecsRequest\x1a\x13.proto.RecsResponse\x12\x32\n\tAddCourse\x12\r.proto.Course\x1a\x16.google.protobuf.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rec_svc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_COURSERECSREQUEST']._serialized_start=53
  _globals['_COURSERECSREQUEST']._serialized_end=108
  _globals['_USERRECSREQUEST']._serialized_start=110
  _globals['_USERRECSREQUEST']._serialized_end=161
  _globals['_COURSE']._serialized_start=163
  _globals['_COURSE']._serialized_end=255
  _globals['_COURSEREC']._serialized_start=257
  _globals['_COURSEREC']._serialized_end=295
  _globals['_RECSRESPONSE']._serialized_start=297
  _globals['_RECSRESPONSE']._serialized_end=343
  _globals['_RECSERVICE']._serialized_start=346
  _globals['_RECSERVICE']._serialized_end=540
# @@protoc_insertion_point(module_scope)