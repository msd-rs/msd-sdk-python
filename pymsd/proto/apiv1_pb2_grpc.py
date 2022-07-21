# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pymsd.proto import apiv1_pb2 as pymsd_dot_proto_dot_apiv1__pb2


class DataFrameServiceStub(object):
    """数据服务
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/apiv1.DataFrameService/Get',
                request_serializer=pymsd_dot_proto_dot_apiv1__pb2.GetDataFrameRequest.SerializeToString,
                response_deserializer=pymsd_dot_proto_dot_apiv1__pb2.GetDataFrameResponse.FromString,
                )
        self.ListObject = channel.unary_unary(
                '/apiv1.DataFrameService/ListObject',
                request_serializer=pymsd_dot_proto_dot_apiv1__pb2.ListObjectRequest.SerializeToString,
                response_deserializer=pymsd_dot_proto_dot_apiv1__pb2.ListObjectResponse.FromString,
                )
        self.Update = channel.stream_unary(
                '/apiv1.DataFrameService/Update',
                request_serializer=pymsd_dot_proto_dot_apiv1__pb2.UpdateDataFrameRequest.SerializeToString,
                response_deserializer=pymsd_dot_proto_dot_apiv1__pb2.UpdateDataFrameResponse.FromString,
                )
        self.GetTable = channel.unary_unary(
                '/apiv1.DataFrameService/GetTable',
                request_serializer=pymsd_dot_proto_dot_apiv1__pb2.GetTableRequest.SerializeToString,
                response_deserializer=pymsd_dot_proto_dot_apiv1__pb2.GetTableResponse.FromString,
                )
        self.UpdateMeta = channel.unary_unary(
                '/apiv1.DataFrameService/UpdateMeta',
                request_serializer=pymsd_dot_proto_dot_apiv1__pb2.UpdateMetaRequest.SerializeToString,
                response_deserializer=pymsd_dot_proto_dot_apiv1__pb2.UpdateMetaResponse.FromString,
                )
        self.Forward = channel.unary_unary(
                '/apiv1.DataFrameService/Forward',
                request_serializer=pymsd_dot_proto_dot_apiv1__pb2.ForwardRequest.SerializeToString,
                response_deserializer=pymsd_dot_proto_dot_apiv1__pb2.ForwardResponse.FromString,
                )


class DataFrameServiceServicer(object):
    """数据服务
    """

    def Get(self, request, context):
        """获取数据请求
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListObject(self, request, context):
        """获取某个表中符合条件的 Object 信息
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request_iterator, context):
        """更新数据请求
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTable(self, request, context):
        """获取表信息请求
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateMeta(self, request, context):
        """更新元数据
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Forward(self, request, context):
        """转发相关的操作
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataFrameServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=pymsd_dot_proto_dot_apiv1__pb2.GetDataFrameRequest.FromString,
                    response_serializer=pymsd_dot_proto_dot_apiv1__pb2.GetDataFrameResponse.SerializeToString,
            ),
            'ListObject': grpc.unary_unary_rpc_method_handler(
                    servicer.ListObject,
                    request_deserializer=pymsd_dot_proto_dot_apiv1__pb2.ListObjectRequest.FromString,
                    response_serializer=pymsd_dot_proto_dot_apiv1__pb2.ListObjectResponse.SerializeToString,
            ),
            'Update': grpc.stream_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=pymsd_dot_proto_dot_apiv1__pb2.UpdateDataFrameRequest.FromString,
                    response_serializer=pymsd_dot_proto_dot_apiv1__pb2.UpdateDataFrameResponse.SerializeToString,
            ),
            'GetTable': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTable,
                    request_deserializer=pymsd_dot_proto_dot_apiv1__pb2.GetTableRequest.FromString,
                    response_serializer=pymsd_dot_proto_dot_apiv1__pb2.GetTableResponse.SerializeToString,
            ),
            'UpdateMeta': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateMeta,
                    request_deserializer=pymsd_dot_proto_dot_apiv1__pb2.UpdateMetaRequest.FromString,
                    response_serializer=pymsd_dot_proto_dot_apiv1__pb2.UpdateMetaResponse.SerializeToString,
            ),
            'Forward': grpc.unary_unary_rpc_method_handler(
                    servicer.Forward,
                    request_deserializer=pymsd_dot_proto_dot_apiv1__pb2.ForwardRequest.FromString,
                    response_serializer=pymsd_dot_proto_dot_apiv1__pb2.ForwardResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'apiv1.DataFrameService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataFrameService(object):
    """数据服务
    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/apiv1.DataFrameService/Get',
            pymsd_dot_proto_dot_apiv1__pb2.GetDataFrameRequest.SerializeToString,
            pymsd_dot_proto_dot_apiv1__pb2.GetDataFrameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/apiv1.DataFrameService/ListObject',
            pymsd_dot_proto_dot_apiv1__pb2.ListObjectRequest.SerializeToString,
            pymsd_dot_proto_dot_apiv1__pb2.ListObjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/apiv1.DataFrameService/Update',
            pymsd_dot_proto_dot_apiv1__pb2.UpdateDataFrameRequest.SerializeToString,
            pymsd_dot_proto_dot_apiv1__pb2.UpdateDataFrameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/apiv1.DataFrameService/GetTable',
            pymsd_dot_proto_dot_apiv1__pb2.GetTableRequest.SerializeToString,
            pymsd_dot_proto_dot_apiv1__pb2.GetTableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateMeta(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/apiv1.DataFrameService/UpdateMeta',
            pymsd_dot_proto_dot_apiv1__pb2.UpdateMetaRequest.SerializeToString,
            pymsd_dot_proto_dot_apiv1__pb2.UpdateMetaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Forward(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/apiv1.DataFrameService/Forward',
            pymsd_dot_proto_dot_apiv1__pb2.ForwardRequest.SerializeToString,
            pymsd_dot_proto_dot_apiv1__pb2.ForwardResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
