import platform
import time
import urllib.request

def check_network_speed():
    url = "https://ovh.net"
    start = time.time()
    req = urllib.request.urlopen(url)
    data = req.read()
    elapsed = time.time() - start
    mbps = (len(data) * 8) / (elapsed * 1_000_000)
    print(f"Downloaded 100MB in {elapsed:.2f}s (~{mbps:.2f} Mbps)")

def main():
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor()}")
    check_network_speed()

    # Add your automated build, download, or processing logic below
    print("Running automated task...")

if __name__ == "__main__":
    main()
