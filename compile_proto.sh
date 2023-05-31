#!/bin/bash -x

cd protocol_buffers || exit
python -m grpc_tools.protoc -I../proto --python_out=. --pyi_out=. --grpc_python_out=. ../proto/employee_report.proto
cd - || exit