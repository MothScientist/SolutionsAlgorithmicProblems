class Codec:
    urls = []
    def encode(self, longUrl: str) -> str:
        n = len(self.urls)
        k = 10
        code = "/"
        while "/" in code:
            code = longUrl[-k:-1]
            k -= 1
        tiny_url = "http://tinyurl.com/" + str(n) + str(n**2) + code
        self.urls.append([longUrl, tiny_url])
        return tiny_url
        

    def decode(self, shortUrl: str) -> str:
        for i in self.urls:
            if shortUrl in i:
                return i[0]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))