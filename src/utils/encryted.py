import cryptocode


class EncryptedController:
    def __init__(self, key: str | None = None):
        if key is None or key == "":
            raise Exception("The encryption key must not be null")  # noqa: TRY002
        self.key = key

    def encrypt(self, data: str) -> str:
        return cryptocode.encrypt(data, self.key)

    def decrypt(self, encrypted_data: str) -> str:
        return cryptocode.decrypt(encrypted_data, self.key)
