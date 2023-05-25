import grpc
from google.protobuf.json_format import MessageToJson, ParseDict
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

import employee_report_pb2
import employee_report_pb2_grpc

# Establish a gRPC channel
channel = grpc.insecure_channel('[::]:50051', options=(('grpc.enable_http_proxy', 0),))
stub = employee_report_pb2_grpc.EmployeeReportServiceStub(channel)


# Create your views here.
class ReportsView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        report = ParseDict(request.data, employee_report_pb2.Report())
        response = stub.CreateReport(request=report)
        json = MessageToJson(response, preserving_proto_field_name=True)
        return Response(json, status=status.HTTP_201_CREATED)


class EditReportsView(APIView):

    def get(self, request, id):
        pass

    def put(self, request, id):
        pass

    def patch(self, request, id):
        pass


class UserReportsView(APIView):
    def get(self, request, id):
        request = employee_report_pb2.GetReportsByUserRequest(user_id=id)
        response = stub.GetReportsByUser(request=request)
        # TODO: check response for empty set and return error instead of OK
        json = MessageToJson(response, preserving_proto_field_name=True)
        return Response(json, status=status.HTTP_200_OK)


class ProjectsReportsView(APIView):
    def get(self, request, id):
        report = ParseDict(request.data, employee_report_pb2.GetReportsByProjectRequest())
        response = stub.GetReportsByProject(request=report)
        # TODO: check response for empty set and return error instead of OK
        json = MessageToJson(response, preserving_proto_field_name=True)
        return Response(json, status=status.HTTP_200_OK)
