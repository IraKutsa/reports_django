from concurrent import futures
from signal import signal, SIGTERM, SIGINT
import grpc
import logging

from google.protobuf.empty_pb2 import Empty
from pymongo import MongoClient

import employee_report_pb2_grpc, employee_report_pb2


class EmployeeReportService(employee_report_pb2_grpc.EmployeeReportServiceServicer):

    def __init__(self):
        # self.reports = []
        # self.reports_by_user = {}
        # self.reports_by_project = {}
        client = MongoClient('localhost', 27017)
        self.db = client.service_db

    def CreateReport(self, request, context):
        logging.info('call CreateReport')
        logging.info(request)
        report = request
        # report.id = len(self.reports) + 1
        # self.reports.append(report)
        # self._add_report_to_collections(report)
        report.id = self.db.reports.insert_one(report).inserted_id
        return report

    def GetReportById(self, request, context):
        report = self.db.reports.find_one({"_id": request.id})
        if report is not None:
            return report
        else:
            context.set_details('Report not found')
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return employee_report_pb2.Report()

    def GetReportsByUser(self, request, context):
        reports = self.db.reports.find({"user": request.user})
        if reports:
            return employee_report_pb2.ReportsByUser(reports=reports)
        else:
            return employee_report_pb2.ReportsByUser()

    def GetReportsByProject(self, request, context):
        reports = self.db.reports.find({"project": request.project})
        if reports:
            return employee_report_pb2.ReportsByProject(reports=reports)
        else:
            return employee_report_pb2.ReportsByProject()

    def EditReport(self, request, context):
        report = self.db.reports.find_one({"_id": request.id})

        if report is None:
            context.set_details('Report not found')
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return employee_report_pb2.Report()

        for field, value in request.ListFields():
            if field.name == 'id':
                continue
            if request.HasField(field.name):
                setattr(report, field.name, getattr(request, field.name))

        self.db.reports.delete_one({ "_id": request.id })
        report.id = self.db.reports.insert_one(report).inserted_id
        # self.reports[index] = report
        # self._remove_repreportsort_from_collections(report)
        # self._add_report_to_collections(report)
        return report

    def DeleteReportById(self, request, context):
        # index, report = self._find_report_by_id(request.id)
        result = self.db.reports.delete_one({"_id": request.id})
        if result.deleted_count > 0:
            return Empty()
        else:
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
