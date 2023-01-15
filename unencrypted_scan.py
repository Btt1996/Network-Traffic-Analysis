import socket

def scan_unencrypted(url):
    # extract hostname from URL
    hostname = url.split('//')[-1]

    try:
        # get IP address of host
        ip = socket.gethostbyname(hostname)

        # create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)

        # connect to host
        result = sock.connect_ex((ip, 80))

        if result == 0:
            print("[INFO] Unencrypted connection found:", url)
    except:
        pass

if __name__ == "__main__":
    # list of URLs to scan
    urls = ['http://example1.com', 'https://example2.com', 'http://example3.com']

    # scan each URL
    for url in urls:
        scan_unencrypted(url)
