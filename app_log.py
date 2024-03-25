from datetime import datetime
import socketserver
import sys
import json

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            self.data = self.request.recv(1024).strip()
        except KeyboardInterrupt:
            raise KeyboardInterrupt()
        except Exception as e:
            print("Exception: (%s)", e)
            return

        # Assuming the data is JSON formatted and contains a userId
        try:
            data_json = json.loads(self.data.decode('utf-8'))
            userId = data_json.get('userId')
            if userId is None:
                print("No userId in received data")
                return
        except json.JSONDecodeError as e:
            print("Received data is not valid JSON:", e)
            return

        filename = f"logs/{userId}_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.txt"
        with open(filename, 'w') as f:
            f.write(f"{self.client_address[0]} wrote at {datetime.now()}:\n")
            json.dump(data_json, f, indent=4)
        
        # Here, you would have additional logic to write to a database
        # Removed for brevity

def main():
    IP_IR = '0.0.0.0'  # Listen on all network interfaces
    PORT_IR = 12345

    print(f'starting server on port {PORT_IR}...')
    
    with socketserver.TCPServer((IP_IR, PORT_IR), MyTCPHandler) as server_ir:
        server_ir.allow_reuse_address = True
        try:
            server_ir.serve_forever()
        except KeyboardInterrupt:
            print("Server is shutting down.")
        except Exception as e:
            print("Exception:", e)
        finally:
            server_ir.server_close()

if __name__ == '__main__':
    main()
