#!/bin/bash -x

cd protocol_buffers || exit
python -m grpc_tools.protoc -I../proto --python_out=. --pyi_out=. --grpc_python_out=. ../proto/employee_report.proto
sed -i ./*_pb2_grpc.py -e 's/^import [^ ]*_pb2/from . \0/'
cd - || exit