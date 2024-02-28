class Registry:
    REGISTRY = {}

    @classmethod
    def _register(cls, key: str):
        def decorator(func_or_class):
            if key in cls.REGISTRY:
                raise KeyError("Function or class {} already exists.".format(key))
            cls.REGISTRY[key] = func_or_class
            return func_or_class
        return decorator

    @classmethod
    def _lookup(cls, key: str):
        if key not in cls.REGISTRY:
            raise LookupError("Function or class at {} is never registered".format(key))
        return cls.REGISTRY[key]
