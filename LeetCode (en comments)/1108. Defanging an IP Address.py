# Given a valid(IPv4) IP address, return a defanged version of that IP address.
#
# A defanged IP address replaces every period "." with "[.]".
#
# Example 1:
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
#
# Example 2:
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"

# def defang_ip_addr(address: str) -> str:
#     ip = ""
#     for digit in range(0, len(address)):
#         if address[digit - 1] == ".":
#             ip += "]"
#         ip += address[digit]
#         if digit < len(address) - 1 and address[digit + 1] == ".":
#             ip += "["
#
#     return ip

def defang_ip_addr(address: str) -> str:
    return address.replace(".", "[.]")


print(defang_ip_addr("255.100.50.0"))
