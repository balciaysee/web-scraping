import httpx

resp = httpx.get("https://www.usom.gov.tr/url-list.txt").text
urls = resp.split("\n")

for url in urls:
    try:
        resp = httpx.get("http://%s" % url, timeout=5)

        if resp.status_code == 200:
            print("[active] %s" % url)
    except:
        pass