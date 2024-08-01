import requests

class OperationsClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def list_operations(self):
        url = f"{self.base_url}/operations"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def perform_operation(self, operation_name, param1, param2):
        operations = self.list_operations()

        operation = next((op for op in operations["operations"] if op["name"].lower() == operation_name.lower()), None)
        if not operation:
            raise ValueError(f"Operação '{operation_name}' não encontrada")

        operation_url = self.base_url + operation["path"].replace("param1", str(param1)).replace("param2", str(param2))

        response = requests.post(operation_url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()



if __name__ == "__main__":
    client = OperationsClient("https://calculadora-fxpc.onrender.com")

    operations = client.list_operations()
    print("Operações disponíveis:", operations)

    result = client.perform_operation("Soma", 5, 3)
    print("Resultado da soma:", result)

    result = client.perform_operation("Divisao", 10, 2)
    print("Resultado da divisão:", result)

    result = client.perform_operation("Subtracao", 10, 2)
    print("Resultado da subtracao:", result)

    result = client.perform_operation("vasco", 10, 2)
    print("Resultado da multiplicação:", result)