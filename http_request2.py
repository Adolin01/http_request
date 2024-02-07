import http.client

# Establish a connection to the desired URL
con = http.client.HTTPSConnection('www.google.com')(

# Send a get request for the root path
con.request("GET", "/")

# Retrieve the response
r = con.getresponse()

# Print the response type and some information
print(type(r))
print(r.status, r.reason)

if r.status == 200:
    print("Status: ", r.status)
    print("Response: ")
    print(r.read().decode())
