import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        print('function called from server')
        result = request.num1 + request.num2
        return calculator_pb2.AddResponse(result=result)
    def Sub(self,request,context):
        print('sub function called from server')
        result = request.num1 - request.num2
        return calculator_pb2.AddResponse(result=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("==========server started at port 50051 =========")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()