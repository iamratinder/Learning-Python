import requests
r = requests.get("https://www.google.com")
print(r.status_code)

# Status codes :
# 200 -> OK  (request is sent and received successfully)
# 403 -> forbidden (you didn't sent authentication correctly) [google being public don't need authentication to be sent]
# 404 -> Not found

print(r.headers)            # give some info of request
print(r.headers["Date"])    # give some info of request
print(r.text)