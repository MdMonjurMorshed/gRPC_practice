import grpc
import calculator_pb2
import calculator_pb2_grpc

def run(num1, num2):
    with grpc.insecure_channel('localhost:50051') as channel:
        print('channel=========>',channel)
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        print('stub====>',stub)
        response = stub.Add(calculator_pb2.AddRequest(num1=num1, num2=num2))
        sub_res = stub.Sub(calculator_pb2.SubRequest(num1=num1, num2=num2))
        
        print('response=========>',response)
    print(f"Result: {response.result}")
    print("sub response result:",sub_res.result)

if __name__ == '__main__':
    # Get user Input 
    num1 = int(input("Please input num1: "))
    num2 = int(input("Please input num2: "))
    run(num1, num2)