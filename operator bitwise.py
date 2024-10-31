#operator bitwise
#and
a = 12  # Dalam biner: 1100
b = 5   # Dalam biner: 0101
result = a & b  # Hasil: 0100 (4)
print(f"{a} & {b} = {result}")  # Output: 4
#or
a = 12  # Dalam biner: 1100
b = 5   # Dalam biner: 0101
result = a | b  # Hasil: 1101 (13)
print(f"{a} | {b} = {result}")  # Output: 13
#not
a = 12  # Dalam biner: 1100
result = ~a  # Hasil: -13 (karena dua's complement)
print(f"~{a} = {result}")  # Output: -13
