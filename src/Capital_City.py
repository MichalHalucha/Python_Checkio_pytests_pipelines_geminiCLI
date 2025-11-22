class Capital:
    _instance = None
    _name = None

    def __new__(cls, city_name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._name = city_name
        return cls._instance

    def name(self):
        return self._name
