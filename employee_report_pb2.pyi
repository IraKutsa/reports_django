from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteReportByIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class EditReportRequest(_message.Message):
    __slots__ = ["creation_date", "id", "project_id", "report_date", "task_description", "task_name", "time_span_minutes"]
    CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_DATE_FIELD_NUMBER: _ClassVar[int]
    TASK_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_SPAN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    creation_date: str
    id: int
    project_id: int
    report_date: str
    task_description: str
    task_name: str
    time_span_minutes: int
    def __init__(self, id: _Optional[int] = ..., project_id: _Optional[int] = ..., creation_date: _Optional[str] = ..., report_date: _Optional[str] = ..., time_span_minutes: _Optional[int] = ..., task_name: _Optional[str] = ..., task_description: _Optional[str] = ...) -> None: ...

class GetReportByIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetReportsByProjectRequest(_message.Message):
    __slots__ = ["project_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: int
    def __init__(self, project_id: _Optional[int] = ...) -> None: ...

class GetReportsByUserRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class Report(_message.Message):
    __slots__ = ["creation_date", "id", "project_id", "report_date", "task_description", "task_name", "time_span_minutes", "user_id"]
    CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_DATE_FIELD_NUMBER: _ClassVar[int]
    TASK_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_SPAN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    creation_date: str
    id: str
    project_id: int
    report_date: str
    task_description: str
    task_name: str
    time_span_minutes: int
    user_id: int
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[int] = ..., project_id: _Optional[int] = ..., creation_date: _Optional[str] = ..., report_date: _Optional[str] = ..., time_span_minutes: _Optional[int] = ..., task_name: _Optional[str] = ..., task_description: _Optional[str] = ...) -> None: ...

class ReportsByProject(_message.Message):
    __slots__ = ["project_id", "reports"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    project_id: int
    reports: _containers.RepeatedCompositeFieldContainer[Report]
    def __init__(self, project_id: _Optional[int] = ..., reports: _Optional[_Iterable[_Union[Report, _Mapping]]] = ...) -> None: ...

class ReportsByUser(_message.Message):
    __slots__ = ["reports", "user_id"]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    reports: _containers.RepeatedCompositeFieldContainer[Report]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ..., reports: _Optional[_Iterable[_Union[Report, _Mapping]]] = ...) -> None: ...
