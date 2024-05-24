""" Given a key in the form GA-DE-RY-PO-LU-KI genrate cyper text based
on subsitution g->a a->g letters not in the key are unchanged"""


class CodeRing():

    def __init__(self, key):
        pairs = key.split('-')
        self.swap = {}
        for pair in pairs:
            self.swap[pair[0].lower()] = pair[1].lower()
            self.swap[pair[1].lower()] = pair[0].lower()
            self.swap[pair[0].upper()] = pair[1].upper()
            self.swap[pair[1].upper()] = pair[0].upper()

    def encode(self, clear):
        res = ""
        for x in clear:
            if x in self.swap:
                res += self.swap[x]
            else:
                res += x
        return res

    def decode(self, text):
        return self.encode(text)


def test():
    key = "GA-DE-RY-PO-LU-KI"
    ring = CodeRing(key)
    assert ring.encode("ABCD") == "GBCE"
    assert ring.encode("Ava has a cat") == "Gvg hgs g cgt"
    assert ring.encode("gaderypoluki") == "agedyropulik"
    assert ring.decode("Gvg hgs g cgt") == "Ava has a cat"
    assert ring.decode("agedyropulik") == "gaderypoluki"
    assert ring.decode("GBCE") == "ABCD"
