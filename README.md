## Expected Program Execution

To run the UDP Pinger and Agent, follow the steps below:

### UDP Agent

1. Open a terminal window.
2. Navigate to the directory containing the `udp_agent.py` script.
3. Run the following command:

    ```bash
    python udp_agent.py -p <port>
    ```

   Replace `<port>` with the desired port number where the UDP Agent will listen for incoming requests.

### UDP Pinger

1. Open a separate terminal window.
2. Navigate to the directory containing the `udp_pinger.py` script.
3. Run the following command:

    ```bash
    python udp_pinger.py <ip_address> -p <port> -s <size> -c <count> -t <timeout>
    ```

   - `<ip_address>`: The IP address of the UDP Agent.
   - `-p <port>` (Optional, Default: 1337): Specifies the port on which the UDP Pinger will send messages.
   - `-s <size>` (Optional, Default: 100): Specifies the size of the ping message in bytes.
   - `-c <count>` (Optional, Default: 10): Specifies the number of ping requests to send.
   - `-t <timeout>` (Optional, Default: 1000): Specifies the timeout for each ping request in milliseconds.

### Sample Usage

```bash
python udp_agent.py -p 1337
python udp_pinger.py 127.0.0.1 -p 1337 -s 60 -c 4 -t 500
```

## Program Functionality

The UDP Pinger and Agent program facilitate network communication using UDP (User Datagram Protocol). The program is designed to exchange simple ping messages between the Pinger and the Agent. Below is an overview of the messages and their representation:

### Ping Request (Pinger to Agent)

The Pinger sends a ping request to the Agent with the following structure:

1. **OPCODE:** 1 bit, set to 0 to represent a ping request.
2. **ID of the Message:** 4 bytes integer, initialized at 0 and incremented by 1 at each send.
3. **Data:** A string of 'a' characters repeated `size` times.

Example:
```plaintext
OPCODE: 0 | ID: 0 | Data: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
Ping Reply (Agent to Pinger)
The Agent responds to the ping request with a ping reply containing:

OPCODE: 1 bit, set to 1 to represent a ping reply.
ID of the Message: Same as the ID of the received request.
Data: Contains the data received in the ping request.
Example:

plaintext
Copy code
OPCODE: 1 | ID: 0 | Data: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
Message Exchange Process
The Pinger initiates the communication by sending a ping request to the Agent.
The Agent receives the ping request, processes it, and forms a ping reply.
The Agent sends the ping reply back to the Pinger.
The Pinger receives the ping reply and measures round-trip time (RTT).
Example Output
During the execution of the program, the Pinger prints information about each sent and received message, including the size of the message, source and destination IP addresses, sequence number, and round-trip time.

Example:

plaintext
Copy code
65 bytes from 1.2.3.4: seq=0 rtt=20.288 ms
This indicates that a 65-byte message was successfully received from the IP address 1.2.3.4 with a sequence number of 0 and a round-trip time of 20.288 milliseconds.


