# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from flow.legacy.execution import execution_pb2 as flow_dot_legacy_dot_execution_dot_execution__pb2


class ExecutionAPIStub(object):
    """ExecutionAPI is the API provided by the execution nodes.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
                '/execution.ExecutionAPI/Ping',
                request_serializer=flow_dot_legacy_dot_execution_dot_execution__pb2.PingRequest.SerializeToString,
                response_deserializer=flow_dot_legacy_dot_execution_dot_execution__pb2.PingResponse.FromString,
                )
        self.GetAccountAtBlockID = channel.unary_unary(
                '/execution.ExecutionAPI/GetAccountAtBlockID',
                request_serializer=flow_dot_legacy_dot_execution_dot_execution__pb2.GetAccountAtBlockIDRequest.SerializeToString,
                response_deserializer=flow_dot_legacy_dot_execution_dot_execution__pb2.GetAccountAtBlockIDResponse.FromString,
                )
        self.ExecuteScriptAtBlockID = channel.unary_unary(
                '/execution.ExecutionAPI/ExecuteScriptAtBlockID',
                request_serializer=flow_dot_legacy_dot_execution_dot_execution__pb2.ExecuteScriptAtBlockIDRequest.SerializeToString,
                response_deserializer=flow_dot_legacy_dot_execution_dot_execution__pb2.ExecuteScriptAtBlockIDResponse.FromString,
                )
        self.GetEventsForBlockIDs = channel.unary_unary(
                '/execution.ExecutionAPI/GetEventsForBlockIDs',
                request_serializer=flow_dot_legacy_dot_execution_dot_execution__pb2.GetEventsForBlockIDsRequest.SerializeToString,
                response_deserializer=flow_dot_legacy_dot_execution_dot_execution__pb2.GetEventsForBlockIDsResponse.FromString,
                )
        self.GetTransactionResult = channel.unary_unary(
                '/execution.ExecutionAPI/GetTransactionResult',
                request_serializer=flow_dot_legacy_dot_execution_dot_execution__pb2.GetTransactionResultRequest.SerializeToString,
                response_deserializer=flow_dot_legacy_dot_execution_dot_execution__pb2.GetTransactionResultResponse.FromString,
                )


class ExecutionAPIServicer(object):
    """ExecutionAPI is the API provided by the execution nodes.
    """

    def Ping(self, request, context):
        """Ping is used to check if the access node is alive and healthy.
        Accounts
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAccountAtBlockID(self, request, context):
        """GetAccountAtBlockID gets an account by address at the given block ID
        Scripts
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecuteScriptAtBlockID(self, request, context):
        """ExecuteScriptAtBlockID executes a ready-only Cadence script against the execution state at the block with the given ID.
        Events
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEventsForBlockIDs(self, request, context):
        """GetEventsForBlockIDs retrieves events for all the specified block IDs that have the given type
        Transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTransactionResult(self, request, context):
        """GetTransactionResult gets the result of a transaction.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExecutionAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=flow_dot_legacy_dot_execution_dot_execution__pb2.PingRequest.FromString,
                    response_serializer=flow_dot_legacy_dot_execution_dot_execution__pb2.PingResponse.SerializeToString,
            ),
            'GetAccountAtBlockID': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccountAtBlockID,
                    request_deserializer=flow_dot_legacy_dot_execution_dot_execution__pb2.GetAccountAtBlockIDRequest.FromString,
                    response_serializer=flow_dot_legacy_dot_execution_dot_execution__pb2.GetAccountAtBlockIDResponse.SerializeToString,
            ),
            'ExecuteScriptAtBlockID': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteScriptAtBlockID,
                    request_deserializer=flow_dot_legacy_dot_execution_dot_execution__pb2.ExecuteScriptAtBlockIDRequest.FromString,
                    response_serializer=flow_dot_legacy_dot_execution_dot_execution__pb2.ExecuteScriptAtBlockIDResponse.SerializeToString,
            ),
            'GetEventsForBlockIDs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEventsForBlockIDs,
                    request_deserializer=flow_dot_legacy_dot_execution_dot_execution__pb2.GetEventsForBlockIDsRequest.FromString,
                    response_serializer=flow_dot_legacy_dot_execution_dot_execution__pb2.GetEventsForBlockIDsResponse.SerializeToString,
            ),
            'GetTransactionResult': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTransactionResult,
                    request_deserializer=flow_dot_legacy_dot_execution_dot_execution__pb2.GetTransactionResultRequest.FromString,
                    response_serializer=flow_dot_legacy_dot_execution_dot_execution__pb2.GetTransactionResultResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'execution.ExecutionAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ExecutionAPI(object):
    """ExecutionAPI is the API provided by the execution nodes.
    """

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/execution.ExecutionAPI/Ping',
            flow_dot_legacy_dot_execution_dot_execution__pb2.PingRequest.SerializeToString,
            flow_dot_legacy_dot_execution_dot_execution__pb2.PingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAccountAtBlockID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/execution.ExecutionAPI/GetAccountAtBlockID',
            flow_dot_legacy_dot_execution_dot_execution__pb2.GetAccountAtBlockIDRequest.SerializeToString,
            flow_dot_legacy_dot_execution_dot_execution__pb2.GetAccountAtBlockIDResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExecuteScriptAtBlockID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/execution.ExecutionAPI/ExecuteScriptAtBlockID',
            flow_dot_legacy_dot_execution_dot_execution__pb2.ExecuteScriptAtBlockIDRequest.SerializeToString,
            flow_dot_legacy_dot_execution_dot_execution__pb2.ExecuteScriptAtBlockIDResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEventsForBlockIDs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/execution.ExecutionAPI/GetEventsForBlockIDs',
            flow_dot_legacy_dot_execution_dot_execution__pb2.GetEventsForBlockIDsRequest.SerializeToString,
            flow_dot_legacy_dot_execution_dot_execution__pb2.GetEventsForBlockIDsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTransactionResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/execution.ExecutionAPI/GetTransactionResult',
            flow_dot_legacy_dot_execution_dot_execution__pb2.GetTransactionResultRequest.SerializeToString,
            flow_dot_legacy_dot_execution_dot_execution__pb2.GetTransactionResultResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
