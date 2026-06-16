import hashlib

class Codec:
    mapping = {}
    def encode(self, longUrl: str) -> str:
        code = hashlib.sha256().hexdigest()[:6]
        self.mapping[code] = longUrl
        return f"http://tinyurl.com/{code}"

    def decode(self, shortUrl: str) -> str:
        code = shortUrl[-6:]
        if code in self.mapping:
            return self.mapping[code]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))