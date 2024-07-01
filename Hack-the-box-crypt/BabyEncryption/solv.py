# import string
# from secret import MSG

# def encryption(msg):
#     ct = []
#     for char in msg:
#         ct.append((123 * char + 18) % 256)
#     return bytes(ct)

# ct = encryption(MSG)
# f = open('./msg.enc','w')
# f.write(ct.hex())
# f.close()

ciphertext =list(bytes.fromhex('6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921'))

flag=''
for i in ciphertext:
    found = False
    for char in range(256):  # Try all possible values of char from 0 to 255
        if (123 * char + 18) % 256 == i:
            print(f"Found char: {char}, i: {i}")
            found = True
            flag+=chr(char)
            break
    
    if not found:
        print(f"No char found for i: {i}")

print(flag)
