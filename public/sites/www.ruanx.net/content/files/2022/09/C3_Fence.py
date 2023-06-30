from Crypto.Random import random
from Crypto.Util import number
from secret import flag3 as flag

def convert(msg):
    msg = msg ^ msg >> x
    msg = msg ^ msg << 13 & 296229569
    msg = msg ^ msg << 20 & 2345273571
    msg = msg ^ msg >> 14
    return msg

def transform(message):
    assert len(message) % 4 == 0
    new_message = ''
    for i in range(len(message) / 4):
        block = message[i * 4 : i * 4 +4]
        block = number.bytes_to_long(block)
        block = convert(block)
        block = number.long_to_bytes(block, 4)
        new_message += block
    return new_message

enFlag = transform(flag[5:-1].decode('hex')).encode('hex')
print('transformed_flag:', enFlag)

# transformed_flag: fb9cd6ab42f2be75ae2637794196159de16e49522ed55e83462b0802a0325e1a4e9cbad3
