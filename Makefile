compile:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto


requirements:
	pip3 install -r requirements.txt