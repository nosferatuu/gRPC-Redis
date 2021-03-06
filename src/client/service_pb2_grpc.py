# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import service_pb2 as service__pb2


class GrpcServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RecordDB = channel.unary_unary(
                '/proto.GrpcService/RecordDB',
                request_serializer=service__pb2.SetPerson.SerializeToString,
                response_deserializer=service__pb2.ServerResponse.FromString,
                )
        self.GetRecordDB = channel.unary_unary(
                '/proto.GrpcService/GetRecordDB',
                request_serializer=service__pb2.GetPerson.SerializeToString,
                response_deserializer=service__pb2.ServerResponse.FromString,
                )


class GrpcServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RecordDB(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRecordDB(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GrpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RecordDB': grpc.unary_unary_rpc_method_handler(
                    servicer.RecordDB,
                    request_deserializer=service__pb2.SetPerson.FromString,
                    response_serializer=service__pb2.ServerResponse.SerializeToString,
            ),
            'GetRecordDB': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRecordDB,
                    request_deserializer=service__pb2.GetPerson.FromString,
                    response_serializer=service__pb2.ServerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.GrpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GrpcService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RecordDB(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.GrpcService/RecordDB',
            service__pb2.SetPerson.SerializeToString,
            service__pb2.ServerResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRecordDB(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.GrpcService/GetRecordDB',
            service__pb2.GetPerson.SerializeToString,
            service__pb2.ServerResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
