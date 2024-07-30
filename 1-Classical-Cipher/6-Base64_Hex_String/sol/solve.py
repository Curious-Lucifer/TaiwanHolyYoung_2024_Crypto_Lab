import base64

payload = 'NDY0YzQxNDc3YjYwNjI3OTc0NjU3MzYwNWYyNjVmNjA3Mzc0NzI2MDVmNjE3MjY1NWY2NDY5NjY2NjY1NzI2NTZlNzQ1ZjY5NmU1ZjUwNzk3NDY4NmY2ZTdk'
payload = base64.b64decode(payload.encode()).decode()
flag = bytes.fromhex(payload)

print(flag)