import requests

class OperationsClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def operations(self):
        url = f"{self.base_url}/operations"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def _get_operation_path(self, operation_name, param1, param2):
        operations = self.operations()
        operation = next((op for op in operations["operations"] if op["name"].lower() == operation_name.lower()), None)
        if not operation:
            raise ValueError(f"Operação '{operation_name}' não encontrada")
        return operation["path"].replace("param1", str(param1)).replace("param2", str(param2))

    def soma(self, param1, param2):
        path = self._get_operation_path("Soma", param1, param2)
        return self._perform_post_request(path)

    def divisao(self, param1, param2):
        path = self._get_operation_path("Divisao", param1, param2)
        return self._perform_post_request(path)

    def subtracao(self, param1, param2):
        path = self._get_operation_path("Subtracao", param1, param2)
        return self._perform_post_request(path)

    def _perform_post_request(self, path):
        url = self.base_url + path
        response = requests.post(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

if __name__ == "__main__":
    client = OperationsClient("https://calculadora-fxpc.onrender.com")

    try:
        # Testar operações específicas
        result = client.soma(5, 3)
        print("Resultado da soma:", result)

        result = client.divisao(10, 2)
        print("Resultado da divisão:", result)

        result = client.subtracao(10, 2)
        print("Resultado da subtração:", result)
    except ValueError as e:
        print(e)
    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")
