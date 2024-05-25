def find_the_key(messages, secrets):
    texts = dict(zip(messages, secrets))
    keys = {}
    for key, value in texts.items():
        for a, b in zip(key, value):
            if a == b:
                continue
            k = min(a, b)
            v = max(a, b)
            keys[k] = v
    ret = ""
    for k in sorted(keys.keys()):
        ret += k+keys[k]

    return ret


def test_this():
    messages = ["dance on the table",  "hide my beers", "scouts rocks"]
    secrets = ["egncd pn thd tgbud", "hked mr bddys", "scplts ypcis"]
    assert find_the_key(messages, secrets) == "agdeikluopry"
