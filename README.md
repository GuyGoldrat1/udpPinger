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
