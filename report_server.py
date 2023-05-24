from concurrent import futures
from signal import signal, SIGTERM, SIGINT
import grpc
import logging

from google.protobuf.empty_pb2 import Empty

from protocol_buffers import employee_report_pb2_grpc, employee_report_pb2


class EmployeeReportService(employee_report_pb2_grpc.EmployeeReportServiceServicer):

    def __init__(self):
        self.reports = []
        self.reports_by_user = {}
        self.reports_by_project = {}

    def CreateReport(self, request, context):
        logging.info('call CreateReport')
        logging.info(request)
        report = request
        report.id = len(self.reports) + 1
        self.reports.append(report)
        self._add_report_to_collections(report)
        return report

    def GetReportById(self, request, context):
        index, report = self._find_report_by_id(request.id)
        if report is not None:
            return report
        else:
            context.set_details('Report not found')
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return employee_report_pb2.Report()

    def GetReportsByUser(self, request, context):
        if request.user_id in self.reports_by_user:
            reports = self.reports_by_user[request.user_id]
            return employee_report_pb2.ReportsByUser(reports=reports)
        else:
            return employee_report_pb2.ReportsByUser()

    def GetReportsByProject(self, request, context):
        if request.project_id in self.reports_by_project:
            reports = self.reports_by_project[request.project_id]
            return employee_report_pb2.ReportsByProject(reports=reports)
        else:
            return employee_report_pb2.ReportsByProject()

    def EditReport(self, request, context):
        report_id = request.id
        index, report = self._find_report_by_id(report_id)

        if report is None:
            context.set_details('Report not found')
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return employee_report_pb2.Report()

        for field, value in request.ListFields():
            if field.name == 'id':
                continue
            if request.HasField(field.name):
                setattr(report, field.name, getattr(request, field.name))

        self.reports[index] = report
        self._remove_report_from_collections(report)
        self._add_report_to_collections(report)

        return report

    def DeleteReportById(self, request, context):
        index, report = self._find_report_by_id(request.id)
        if report is not None:
            self.reports.remove(report)
            self._remove_report_from_collections(report)
            return Empty()
        else:
            context.set_details('Report not found')
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return Empty()

    def _find_report_by_id(self, report_id):
        for index, report in enumerate(self.reports):
            if report.id == report_id:
                return index, report
        return None, None

    def _add_report_to_collections(self, report):
        if report.user_id not in self.reports_by_user:
            self.reports_by_user[report.user_id] = []
        self.reports_by_user[report.user_id].append(report)

        if report.project_id not in self.reports_by_project:
            self.reports_by_project[report.project_id] = []
        self.reports_by_project[report.project_id].append(report)

    def _remove_report_from_collections(self, report):
        if report.user_id in self.reports_by_user:
            self.reports_by_user[report.user_id].remove(report)

        if report.project_id in self.reports_by_project:
            self.reports_by_project[report.project_id].remove(report)

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
