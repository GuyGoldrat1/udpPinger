import socket
import sys
import time

def main():
    if len(sys.argv) != 7 or sys.argv[1] != '-p' or sys.argv[3] != '-s' or sys.argv[5] != '-c':
        print("Usage: python udp_pinger.py <ip_address> -p <port> -s <timeout_seconds> -c <count>")
        sys.exit(1)

    ip_address = sys.argv[1]
    port = int(sys.argv[4])
    timeout_seconds = int(sys.argv[6])
    count = int(sys.argv[8])

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(timeout_seconds)
        sequence_number = 0

        for i in range(count):
            send_time = time.time()
            message_id = sequence_number

            # Create ping request
            ping_request = create_ping_request(message_id)
            sock.sendto(ping_request, (ip_address, port))

            try:
                data, address = sock.recvfrom(1024)
                recv_time = time.time()
                opcode, reply_id, payload = parse_message(data)

                if opcode == 1 and reply_id == message_id:
                    rtt = round((recv_time - send_time) * 1000, 3)
                    print(f"{len(data)} bytes from {ip_address}: seq={sequence_number} rtt={rtt} ms")
                else:
                    print(f"Received invalid reply for sequence {sequence_number}")

            except socket.timeout:
                print(f"Request timeout for icmp_seq {sequence_number}")

            sequence_number += 1

        print(f"--- {ip_address} statistics --- {count} packets transmitted, {sequence_number} packets received, "
              f"{((sequence_number - count) / sequence_number) * 100:.1f}% packet loss")

def create_ping_request(message_id):
    opcode = 0
    payload = "Hello, Pinger!"
    ping_request = bytes([opcode]) + message_id.to_bytes(4, byteorder='big') + payload.encode('utf-8')
    return ping_request

def parse_message(data):
    opcode = data[0] >> 7
    reply_id = int.from_bytes(data[1:5], byteorder='big')
    payload = data[5:].decode('utf-8')
    return opcode, reply_id, payload

if __name__ == "__main__":
    main()
