""" Given a key in the form GA-DE-RY-PO-LU-KI genrate cyper text based
on subsitution g->a a->g letters not in the key are unchanged"""


class CodeRing():

    def encode(self, clear, key):
        pairs = []
        for i in range(0, len(key), 2):
            pairs.append(key[i:i+2])
        self.swap = {}
        for pair in pairs:
            self.swap[pair[0].lower()] = pair[1].lower()
            self.swap[pair[1].lower()] = pair[0].lower()
            self.swap[pair[0].upper()] = pair[1].upper()
            self.swap[pair[1].upper()] = pair[0].upper()
        res = ""
        for x in clear:
            if x in self.swap:
                res += self.swap[x]
            else:
                res += x
        return res

    def decode(self, text, key):
        return self.encode(text, key)


def test():
    ring = CodeRing()
    assert ring.encode("ABCD", "agedyropulik") == "GBCE"
    assert ring.encode("Ava has a cat", "gaderypoluki") == "Gvg hgs g cgt"
    assert ring.decode("Dkucr pu yhr ykbir", "politykarenu") \
        == "Dance on the table"
    assert ring.decode("Hmdr nge brres", "regulaminowy") == "Hide our beers"
