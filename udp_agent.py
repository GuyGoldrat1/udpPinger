import socket
import sys

def agent(host, port):

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((host, port))

        print(f"UDP Agent listening on port {port}...")

        while True:
            data, address = sock.recvfrom(1024)
            opcode, message_id, payload = parse_message(data)

            if opcode == 0:
                # Ping request received
                reply_data = create_ping_reply(message_id, payload)
                sock.sendto(reply_data, address)

def parse_message(data):
    opcode = data[0] >> 7
    message_id = int.from_bytes(data[1:5], byteorder='big')
    payload = data[5:].decode('utf-8')
    return opcode, message_id, payload

def create_ping_reply(message_id, payload):
    opcode = 1 << 7
    reply_data = bytes([opcode]) + message_id.to_bytes(4, byteorder='big') + payload.encode('utf-8')
    return reply_data

if __name__ == "__main__":

    PORT = 1337 if len(sys.argv) < 3 else int(sys.argv[2])
    HOST = 'localhost'
    agent(HOST, PORT)
