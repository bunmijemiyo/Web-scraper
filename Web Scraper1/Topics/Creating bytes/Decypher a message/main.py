text = input()
num = sum((int(input())).to_bytes(2, byteorder="little"))
result = [ord(i) + num for i in text]
print("".join(chr(item) for item in result))
