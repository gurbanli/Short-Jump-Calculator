import sys

bytes_of_jump = sys.argv[1]
direction = sys.argv[2]


if direction == 'forward':
    jmp_code = f"\\xeb\\x{hex(int(bytes_of_jump)).split('x')[-1].zfill(2)}"
    print(jmp_code)
elif direction == 'backward':
    bytes_of_jump = 254 - int(bytes_of_jump)
    jmp_code = f"\\xeb\\x{hex(int(bytes_of_jump)).split('x')[-1].zfill(2)}"
    print(jmp_code)
    