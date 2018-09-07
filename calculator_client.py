import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)


def addRequestGRPC(a, b):
    addRequest = calculator_pb2.AddRequest(a=a, b=b)
    response = stub.Add(addRequest)
    return response.value


if __name__ == '__main__':
    print(addRequestGRPC(10, 20))
    print(addRequestGRPC(20, 20))
    print(addRequestGRPC(30, 30))
    print(addRequestGRPC(333, 333))
    print(addRequestGRPC(222, 2222))
