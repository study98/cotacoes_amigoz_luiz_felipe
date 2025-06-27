from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime
import time
import random

class CotacaoMockHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        now = datetime.now().isoformat()

        if self.path == "/cotacao/dolar":
            data = {
                "moeda": "Dolar",
                "sigla": "USD",
                "valor": round(random.uniform(1.0, 10.0),2),
                "momento_cotacao": now
            }

        elif self.path == "/cotacao/euro":
            time.sleep(round(random.uniform(0.9, 4.9),2))  # Atraso de até 5 segundos para simular latência
            data = {
                "moeda": "euro",
                "sigla": "EUR",
                "valor": round(random.uniform(1.0, 10.0),2),
                "momento_cotacao": now
            }

        else:
            self.send_response(404)
            self.end_headers()
            return

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

def run_mock_server():
    server_address = ("localhost", 3000)
    httpd = HTTPServer(server_address, CotacaoMockHandler)
    print("🔧 Mock da API rodando em http://localhost:3000")
    httpd.serve_forever()

if __name__ == "__main__":
    run_mock_server()