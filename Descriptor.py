class Desc:

    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if float(value) > 0:
            setattr(instance, self.name, value)
        else:
            raise ValueError("габаритные размеры должны быть положительными числами")

    # @staticmethod
    # def varify(instance, value):
    #     return instance.MIN_DIMENSION <= value <= instance.MAX_DIMENSION