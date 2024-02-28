from registry import Registry


class ModelFactory(Registry):
    @classmethod
    def register_model(cls, key: str):
        return cls._register(key)

    @classmethod
    def build_model(cls, model_config):
        model_builder = cls._lookup(model_config['type'])
        return model_builder(cfg=model_config)
