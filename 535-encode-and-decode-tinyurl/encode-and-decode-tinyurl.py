import hashlib

class Codec:
    def __init__(self):
        self.mapping = {}

    def encode(self, longUrl: str) -> str:
        code = hashlib.sha256(longUrl.encode()).hexdigest()[:6]
        self.mapping[code] = longUrl
        return f"http://tinyurl.com/{code}"

    def decode(self, shortUrl: str) -> str:
        code = shortUrl[-6:]
        if code in self.mapping:
            return self.mapping[code]