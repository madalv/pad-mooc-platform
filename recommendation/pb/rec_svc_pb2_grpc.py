# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import rec_svc_pb2 as rec__svc__pb2


class RecServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetRecsForCourse = channel.unary_unary(
                '/proto.rec.RecService/GetRecsForCourse',
                request_serializer=rec__svc__pb2.CourseRecsRequest.SerializeToString,
                response_deserializer=rec__svc__pb2.RecsResponse.FromString,
                )
        self.GetRecsForUser = channel.unary_unary(
                '/proto.rec.RecService/GetRecsForUser',
                request_serializer=rec__svc__pb2.UserRecsRequest.SerializeToString,
                response_deserializer=rec__svc__pb2.RecsResponse.FromString,
                )
        self.AddCourse = channel.unary_unary(
                '/proto.rec.RecService/AddCourse',
                request_serializer=rec__svc__pb2.Course.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetServerStatus = channel.unary_unary(
                '/proto.rec.RecService/GetServerStatus',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=rec__svc__pb2.ServerStatus.FromString,
                )


class RecServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetRecsForCourse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRecsForUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddCourse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServerStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetRecsForCourse': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRecsForCourse,
                    request_deserializer=rec__svc__pb2.CourseRecsRequest.FromString,
                    response_serializer=rec__svc__pb2.RecsResponse.SerializeToString,
            ),
            'GetRecsForUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRecsForUser,
                    request_deserializer=rec__svc__pb2.UserRecsRequest.FromString,
                    response_serializer=rec__svc__pb2.RecsResponse.SerializeToString,
            ),
            'AddCourse': grpc.unary_unary_rpc_method_handler(
                    servicer.AddCourse,
                    request_deserializer=rec__svc__pb2.Course.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetServerStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServerStatus,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=rec__svc__pb2.ServerStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.rec.RecService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RecService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetRecsForCourse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.rec.RecService/GetRecsForCourse',
            rec__svc__pb2.CourseRecsRequest.SerializeToString,
            rec__svc__pb2.RecsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRecsForUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.rec.RecService/GetRecsForUser',
            rec__svc__pb2.UserRecsRequest.SerializeToString,
            rec__svc__pb2.RecsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddCourse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.rec.RecService/AddCourse',
            rec__svc__pb2.Course.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServerStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.rec.RecService/GetServerStatus',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            rec__svc__pb2.ServerStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
