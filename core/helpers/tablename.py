class TablenameHelper:

    @staticmethod
    def generate_tn(model) -> str:
        if isinstance(model, str):
            name = model
        else:
            name = model.__name__

        name = name.lower()

        if name.endswith("y"):
            return name[:-1] + "ies"
        elif name.endswith("s"):
            return name
        else:
            return name + "s"
