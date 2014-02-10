
def lazy_property(fn):
    attr_name = '_lazy_' + fn.__name__

    @property
    def __lazy_property__(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return __lazy_property__
