def defang_ip_addr(address: str) -> str:
    return address.replace(".", "[.]")


print(defang_ip_addr("255.100.50.0"))
