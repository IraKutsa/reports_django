from concurrent import futures
from signal import signal, SIGTERM, SIGINT
import grpc
import logging

from bson import ObjectId
from google.protobuf.empty_pb2 import Empty
from google.protobuf.json_format import MessageToDict, ParseDict
from pymongo import MongoClient

import employee_report_pb2_grpc, employee_report_pb2


def convert(report):
    report["id"] = str(report["_id"])
    return ParseDict(report, employee_report_pb2.Report(), ignore_unknown_fields=True)


class EmployeeReportService(employee_report_pb2_grpc.EmployeeReportServiceServicer):

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.service_db

    def CreateReport(self, request, context):
        logging.info('call CreateReport')
        logging.info(request)
        report = MessageToDict(request, preserving_proto_field_name=True)
        self.db.reports.insert_one(report)
        return convert(report)

    def GetReportById(self, request, context):
        logging.info('call GetReportById')
        logging.info(request)
        report = self.db.reports.find_one({"_id": ObjectId(request.id)})
        if report is not None:
            return convert(report)
        else:
            context.set_details('Report not found')
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return employee_report_pb2.Report()

    def GetReportsByUser(self, request, context):
        logging.info('call GetReportsByUser')
        logging.info(request)
        reports = self.db.reports.find({"userId": request.user_id})
        by_user = employee_report_pb2.ReportsByUser(user_id=request.user_id)
        if reports:
            by_user.reports.extend([convert(report) for report in reports])
        return by_user

    def GetReportsByProject(self, request, context):
        logging.info('call GetReportsByProject')
        logging.info(request)
        reports = self.db.reports.find({"projectId": request.project_id})
        by_project = employee_report_pb2.ReportsByProject(project_id=request.project_id)
        if reports:
            by_project.reports.extend([convert(report) for report in reports])
        return by_project

    def EditReport(self, request, context):
        logging.info('call EditReport')
        logging.info(request)
        report = self.db.reports.find_one({"_id": ObjectId(request.id)})
        if report is None:
            context.set_details('Report not found')
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return employee_report_pb2.Report()

        for field, value in request.ListFields():
            if field.name == 'id':
                continue
            if request.HasField(field.name):
                setattr(report, field.name, getattr(request, field.name))

        self.db.reports.delete_one({ "_id": ObjectId(request.id) })
        self.db.reports.insert_one(report).inserted_id
        return convert(report)

    def DeleteReportById(self, request, context):
        logging.info('call DeleteReportById')
        logging.info(request)
        result = self.db.reports.delete_one({"_id": ObjectId(request.id)})
        if result.deleted_count < 1:
            context.set_details('Report not found')
            context.set_code(grpc.StatusCode.NOT_FOUND)
        return Empty()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port('[::]:50051')
    employee_report_pb2_grpc.add_EmployeeReportServiceServicer_to_server(EmployeeReportService(), server)

    server.start()
    logging.info('Server started')

    def handle_sigterm(*_):
        logging.info("Received shutdown signal")
        all_rpcs_done_event = server.stop(30)
        all_rpcs_done_event.wait(30)
        logging.info("Shut down gracefully")

    signal(SIGTERM, handle_sigterm)
    signal(SIGINT, handle_sigterm)
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()
