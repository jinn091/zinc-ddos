# Zinc HTTP Load Simulation Tool

⚠️ DISCLAIMER ⚠️  
This tool is for **educational, research, and defensive security purposes only**.  
Do not use this script to target any system without **explicit permission**.  
The creator is not responsible for any misuse. Unauthorized use may be **illegal**.

## Overview

Zinc Ddos is a Python-based Distributed Denial of Service (DDoS) attack script that simulates multiple HTTP requests to a specified target URL. It generates random request paths and sends them concurrently through multiple threads to the target server, aiming to simulate a high traffic load.

> **Warning:** This script should only be used for ethical purposes, such as load testing on servers you own or have explicit permission to test. Using this script for malicious purposes, such as attacking websites or servers without permission, is illegal and unethical.

## Features

-   Simulate a DDoS attack by sending HTTP requests with random paths.
-   Allows for user-specified target URL and number of threads.
-   Prints request status codes and any errors encountered.
-   Fully customizable with a list of paths to request.

## Requirements

-   Python 3.x
-   `requests` module (can be installed using `pip install requests`)

## Installation

1. **Clone this repository**:

    ```bash
    git clone https://github.com/jinn091/zinc-ddos.git
    cd zinc-ddos
    ```

2. Alternatively, install `requests` manually if you don’t have `requirements.txt`:
    ```bash
    pip install requests
    ```

## Usage

1. **Run the script**:

    ```bash
    python zinc_ddos.py
    ```

2. **Provide the following inputs** when prompted:
    - **Target URL**: The URL of the server you wish to send traffic to (e.g., `https://example.com`).
    - **Number of threads**: The number of threads you want to use to simulate multiple requests (e.g., `100`).

Example:

```bash
Enter the target URL (e.g., https://example.com)
Enter the number of threads (e.g., 100): 100
```

3. **The script will start sending HTTP requests** with random paths to the target server, and you will see the output with request status codes.

## How it Works

-   The script generates random strings to be appended as query parameters to the request URL.
-   A list of predefined paths is used (e.g., `/contact`, `/about`, etc.), and the script cycles through them.
-   Requests are sent concurrently through multiple threads to simulate high traffic load on the server.
-   The script prints the status code of each request and any errors that occur.

## Example Output

When the script is running, you will see output like:

```
Sent request to https://example.com/contact?id=AbC12345 with status code 200
Sent request to https://example.com/ijodas?id=K9LpA345 with status code 200
Sent request to https://example.com/about?id=3LkA2f57 with status code 200
Error: Max retries exceeded with url: /jkadsa
...
```

## Legal Use Only

By using this software, you agree to use it **only on systems you own or have written permission to test**.

This software is intended strictly for:

-   Penetration testing environments
-   Defensive security testing
-   Load balancing validation
-   Web application firewall (WAF) tuning
-   Red team/blue team cyber training

Unauthorized use of this software against networks, services, or websites you do not own or control is likely to be **illegal** and may lead to criminal or civil penalties.

If in doubt, **do not run this script**.

## Disclaimer

The author of this script is not responsible for any misuse of this tool. By using this script, you agree to take full responsibility for your actions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
