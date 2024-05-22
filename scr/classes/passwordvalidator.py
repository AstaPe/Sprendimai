class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def _has_uppercase(self):
        for char in self.password:
            if char.isupper():
                return True
        return False

    def _has_lowercase(self):
        for char in self.password:
            if char.islower():
                return True
        return False

    def _has_digit(self):
        for char in self.password:
            if char.isdigit():
                return True
        return False

    def is_valid(self):
        return self._has_uppercase() and self._has_lowercase() and self._has_digit()
