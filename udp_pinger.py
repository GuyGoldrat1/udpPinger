import socket
import sys
import time

def pinger(ip,port,size,count,timeout):

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(timeout/1000)
        sequence_number = 0
        resived = 0

        for i in range(count):
            send_time = time.time()
            message_id = sequence_number

            # Create ping request
            ping_request = create_ping_request(message_id, size)
            sock.sendto(ping_request, (ip, port))

            try:
                data, address = sock.recvfrom(1024)
                recv_time = time.time()
                opcode, reply_id, payload = parse_message(data)

                if opcode == 1 and reply_id == message_id:
                    rtt = round((recv_time - send_time) * 1000, 3)
                    resived+=1
                    print(f"{len(data)} bytes from {ip}: seq={sequence_number} rtt={rtt} ms")
                else:
                    print(f"Received invalid reply for sequence {sequence_number}")

            except socket.timeout:
                print(f"Request timeout for icmp_seq {sequence_number}")

            sequence_number += 1

        print(f"---{ip} statistics--- \n{sequence_number} packets transmitted, {resived} packets received, "
              f"{((sequence_number - resived) / sequence_number) * 100:.1f}% packet loss")

def create_ping_request(message_id, size):
    opcode = 0
    payload = "a" * size
    ping_request = bytes([opcode]) + message_id.to_bytes(4, byteorder='big') + payload.encode()
    return ping_request

def parse_message(data):
    opcode = data[0] >> 7
    reply_id = int.from_bytes(data[1:5], byteorder='big')
    payload = data[5:].decode('utf-8')
    return opcode, reply_id, payload

if __name__ == "__main__":
    ip = sys.argv[1]
    port=1337
    size=100
    count=10
    timeout=1000
    i=2
    while(i<len(sys.argv)):
        if sys.argv[i] == "-p":
            port=int(sys.argv[i+1])
        if sys.argv[i] == "-s":
            size=int(sys.argv[i+1])
        if sys.argv[i] == "-c":
            count=int(sys.argv[i+1])
        if sys.argv[i] == "-t":
            timeout=int(sys.argv[i+1])
        i+=1

    

    pinger(ip,port,size,count,timeout)
