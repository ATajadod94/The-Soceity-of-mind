class Mind:
    # A society of mind

    def __init__(self, dict):
        self.dict = dict

    def __str__(self):
        return self._template % self

    def __getitem__(self, key):
        l = key.split("|")
        if len(l) == 1:
            return self.dict[key]
        else:
            return getattr(self, l[1])(self.dict[l[0]])

    def li(self, l):
        return "\n".join(["\t<li>%s</li>" % x for x in l])


print Template({"list": ["foo", "bar", "baz"]})