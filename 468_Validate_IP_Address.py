def validIPAddress(queryIP):
    ipv4 = queryIP.split(".")
    ipv6 = queryIP.split(":")

    if len(ipv4) == 4:
        for i in ipv4:
            if len(i) == 0:
                return "Neither"
            if i.startswith("0") and len(i) > 1:
                return "Neither"
            for el in i:
                if not el.isdigit():
                    return "Neither"
            if int(i) < 0 or int(i) > 255:
                return "Neither"
        return "IPv4"

    if len(ipv6) == 8:
        for i in ipv6:
            if len(i) == 0:
                return "Neither"
            elif len(i) > 4:
                return "Neither"
            for el in i:
                if not (48 <= ord(el) <= 57 or 97 <= ord(el) <= 102 or 65 <= ord(el) <= 70):
                    return "Neither"
        return "IPv6"

    return "Neither"

if __name__ == '__main__':
    print(validIPAddress(queryIP = "172.16.254.1"))
    print(validIPAddress(queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"))
    print(validIPAddress(queryIP = "256.256.256.256"))