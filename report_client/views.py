import grpc
from django.http import Http404
from google.protobuf.json_format import MessageToJson, ParseDict
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from protocol_buffers import employee_report_pb2
from protocol_buffers import employee_report_pb2_grpc

# Establish a gRPC channel
channel = grpc.insecure_channel('[::]:50051', options=(('grpc.enable_http_proxy', 0),))
stub = employee_report_pb2_grpc.EmployeeReportServiceStub(channel)


# Create your views here.
class ReportsView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        try:
            report = ParseDict(request.data, employee_report_pb2.Report())
            response = stub.CreateReport(request=report)
            json = MessageToJson(response, preserving_proto_field_name=True)
            return Response(json, status=status.HTTP_201_CREATED)
        except grpc.RpcError as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetEditReportsView(APIView):

    def get(self, request, id):
        try:
            request_by_id = employee_report_pb2.GetReportByIdRequest(id=id)
            report = stub.GetReportById(request=request_by_id)
            json = MessageToJson(report, preserving_proto_field_name=True)
            return Response(json, status=status.HTTP_200_OK)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise Http404

    def put(self, request, id):
        try:
            report = ParseDict(request.data, employee_report_pb2.EditReportRequest(), ignore_unknown_fields=True)
            report.id = id
            response = stub.EditReport(request=report)
            json = MessageToJson(response, preserving_proto_field_name=True)
            return Response(json, status=status.HTTP_200_OK)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise Http404

    def patch(self, request, id):
        return self.put(request,  id)

    def delete(self, request, id):
        try:
            request_by_id = employee_report_pb2.DeleteReportByIdRequest(id=id)
            stub.DeleteReportById(request=request_by_id)
            return Response(status=status.HTTP_200_OK)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise Http404


class UserReportsView(APIView):
    def get(self, request, id):
        try:
            request = employee_report_pb2.GetReportsByUserRequest(user_id=id)
            response = stub.GetReportsByUser(request=request)
            json = MessageToJson(response, preserving_proto_field_name=True)
            return Response(json, status=status.HTTP_200_OK)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise Http404


class ProjectsReportsView(APIView):
    def get(self, request, id):
        try:
            request = ParseDict(request.data, employee_report_pb2.GetReportsByProjectRequest(project_id=id))
            response = stub.GetReportsByProject(request=request)
            json = MessageToJson(response, preserving_proto_field_name=True)
            return Response(json, status=status.HTTP_200_OK)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise Http404
