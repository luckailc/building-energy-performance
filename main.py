from model_factory import ModelFactory

@ModelFactory.register_model("typeA")
def build_model_A(cfg):
    print("Building Model A with config:", cfg)

@ModelFactory.register_model("typeB")
def build_model_B(cfg):
    print("Building Model B with config:", cfg)


config_A = {'type': 'typeA', 'other_config': 'some_value'}
config_B = {'type': 'typeB', 'other_config': 'another_value'}

model_A = ModelFactory.build_model(config_A)
model_B = ModelFactory.build_model(config_B)