class TablenameHelper:

    @staticmethod
    def generate_tn(model: str) -> str:
        name = model.lower()
        if name.endswith("y"):
            return name[:-1] + "ies"
        elif name.endswith("s"):
            return name
        else:
            return name + "s"
