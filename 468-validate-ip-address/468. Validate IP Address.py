class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_valid_ipv4(ip):
            parts = ip.split(".")
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit():
                    return False
                if not 0 <= int(part) <= 255:
                    return False
                if len(part) > 1 and part[0] == '0':  # No leading zeros allowed
                    return False
            return True

        def is_valid_ipv6(ip):
            parts = ip.split(":")
            if len(parts) != 8:
                return False
            for part in parts:
                if len(part) == 0 or len(part) > 4:
                    return False
                for char in part:
                    if char not in "0123456789abcdefABCDEF":
                        return False
            return True

        if queryIP.count('.') == 3 and is_valid_ipv4(queryIP):
            return "IPv4"
        elif queryIP.count(':') == 7 and is_valid_ipv6(queryIP):
            return "IPv6"
        else:
            return "Neither"
