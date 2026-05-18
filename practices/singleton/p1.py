class AppConfig:
    _instance = None
    def __new__(cls):
        print(AppConfig.__bases__)
        if cls._instance is None:
            cls._instance = super(AppConfig, cls).__new__(cls)
            cls._instance.config = {} # type: ignore
        return cls._instance
    
    def get(self, key):
        return self._instance.config.get(key)
    def set(self, key, value):
        self._instance.config[key] = value
    def all(self):
        return self._instance.config

config1 = AppConfig()
config2 = AppConfig()

print(config1 is config2)  # True
config1.set('debug', True)
print(config2.get('debug'))  # True

config2.set('debug', False)
print(config1.get('debug'))  # False
print(config2.get('debug'))  # False
config1.set('region', 'us-east-1')
print(config2.all())  # {'debug': False, 'region': 'us-east-1'}



## test 
TEST_SETTINGS = [
    ("env", "production"),
    ("debug", False),
    ("region", "ap-southeast-1"),
    ("version", "1.0.0"),
]
#

def test_app_config():
    config = AppConfig()
    for key, value in TEST_SETTINGS:
        config.set(key, value)
    for key, value in TEST_SETTINGS:
        assert config.get(key) == value
    for key, value in TEST_SETTINGS:
        assert config.all()[key] == value
    return "All tests passed!"

print(test_app_config())