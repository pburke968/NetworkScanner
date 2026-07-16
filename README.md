# Network Scanner

## What It Does

- Scans a user-specified IPv4 /24 network
- Sends ICMP echo requests (pings) to each host
- Identifies responsive devices on the network
- Records active hosts for later review
- Displays results from the most recent scan


## Features

- Interactive terminal menu
- Network-wide ping sweep
- Host availability detection
- Round-trip time (RTT) measurement
- Previous scan result storage
- Simple and lightweight design
- 
## Example

Scan network:

```text
192.168.1
```

Output:

```text
Online 192.168.1.1 2.14 ms
Online 192.168.1.10 3.87 ms
Online 192.168.1.25 8.42 ms

SCAN COMPLETE!
```

View previous results:

```text
Previous Scan:

192.168.1.1
192.168.1.10
192.168.1.25
```

## Requirements

- icmplib

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Purpose

This project was created as a learning exercise to develop practical skills in:

- Python programming
- Network troubleshooting
- Working with loops and lists
- Function design and program flow
- Data storage and retrieval
- Building real-world command-line utilities
