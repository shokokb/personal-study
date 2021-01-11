class Codec:
    def __init__(self):
        self.i = 0
        self.dictionary = dict()
        
    def encode(self, longUrl: str) -> str:
        try:
            key = self.dictionary[self.i]
            return "http://tinyurl.com/" + str(self.i)
        except KeyError:
            self.dictionary[self.i] = longUrl
            self.i += 1
            return "http://tinyurl.com/" + str(self.i-1)
        
    def decode(self, shortUrl: str) -> str:       
        i = int(shortUrl.split("/")[-1])
        return self.dictionary[i] 