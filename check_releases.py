import ssl, urllib.request, json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://api.github.com/repos/Soulter/AstrBot/releases?per_page=10"
req = urllib.request.Request(url, headers={"User-Agent": "Python"})
resp = urllib.request.urlopen(req, context=ctx, timeout=10)
data = json.loads(resp.read())
for r in data:
    print(f"{r['tag_name']}: {r['name']}")
    body = r.get("body", "")[:1000]
    print(body)
    print("---")
