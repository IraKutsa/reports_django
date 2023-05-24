# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: employee_report.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x65mployee_report.proto\x12\x0f\x65mployee_report\x1a\x1bgoogle/protobuf/empty.proto\"\xad\x01\n\x06Report\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x12\n\nproject_id\x18\x03 \x01(\x05\x12\x15\n\rcreation_date\x18\x04 \x01(\t\x12\x13\n\x0breport_date\x18\x05 \x01(\t\x12\x19\n\x11time_span_minutes\x18\x06 \x01(\x05\x12\x11\n\ttask_name\x18\x07 \x01(\t\x12\x18\n\x10task_description\x18\x08 \x01(\t\"J\n\rReportsByUser\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12(\n\x07reports\x18\x02 \x03(\x0b\x32\x17.employee_report.Report\"P\n\x10ReportsByProject\x12\x12\n\nproject_id\x18\x01 \x01(\x05\x12(\n\x07reports\x18\x02 \x03(\x0b\x32\x17.employee_report.Report\"\"\n\x14GetReportByIdRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"*\n\x17GetReportsByUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"0\n\x1aGetReportsByProjectRequest\x12\x12\n\nproject_id\x18\x01 \x01(\x05\"\xaf\x02\n\x11\x45\x64itReportRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x17\n\nproject_id\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x1a\n\rcreation_date\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0breport_date\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x1e\n\x11time_span_minutes\x18\x05 \x01(\x05H\x03\x88\x01\x01\x12\x16\n\ttask_name\x18\x06 \x01(\tH\x04\x88\x01\x01\x12\x1d\n\x10task_description\x18\x07 \x01(\tH\x05\x88\x01\x01\x42\r\n\x0b_project_idB\x10\n\x0e_creation_dateB\x0e\n\x0c_report_dateB\x14\n\x12_time_span_minutesB\x0c\n\n_task_nameB\x13\n\x11_task_description\"%\n\x17\x44\x65leteReportByIdRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x32\x9c\x04\n\x15\x45mployeeReportService\x12\x42\n\x0c\x43reateReport\x12\x17.employee_report.Report\x1a\x17.employee_report.Report\"\x00\x12Q\n\rGetReportById\x12%.employee_report.GetReportByIdRequest\x1a\x17.employee_report.Report\"\x00\x12^\n\x10GetReportsByUser\x12(.employee_report.GetReportsByUserRequest\x1a\x1e.employee_report.ReportsByUser\"\x00\x12g\n\x13GetReportsByProject\x12+.employee_report.GetReportsByProjectRequest\x1a!.employee_report.ReportsByProject\"\x00\x12K\n\nEditReport\x12\".employee_report.EditReportRequest\x1a\x17.employee_report.Report\"\x00\x12V\n\x10\x44\x65leteReportById\x12(.employee_report.DeleteReportByIdRequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'employee_report_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REPORT._serialized_start=72
  _REPORT._serialized_end=245
  _REPORTSBYUSER._serialized_start=247
  _REPORTSBYUSER._serialized_end=321
  _REPORTSBYPROJECT._serialized_start=323
  _REPORTSBYPROJECT._serialized_end=403
  _GETREPORTBYIDREQUEST._serialized_start=405
  _GETREPORTBYIDREQUEST._serialized_end=439
  _GETREPORTSBYUSERREQUEST._serialized_start=441
  _GETREPORTSBYUSERREQUEST._serialized_end=483
  _GETREPORTSBYPROJECTREQUEST._serialized_start=485
  _GETREPORTSBYPROJECTREQUEST._serialized_end=533
  _EDITREPORTREQUEST._serialized_start=536
  _EDITREPORTREQUEST._serialized_end=839
  _DELETEREPORTBYIDREQUEST._serialized_start=841
  _DELETEREPORTBYIDREQUEST._serialized_end=878
  _EMPLOYEEREPORTSERVICE._serialized_start=881
  _EMPLOYEEREPORTSERVICE._serialized_end=1421
# @@protoc_insertion_point(module_scope)
