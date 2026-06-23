class User:
    total_users = 0

    def __init__(self, name):
        self.name = name
        User.total_users += 1

    @classmethod
    def get_total_users(cls):
        return cls.total_users
    
    @staticmethod
    def is_valid_name(name):
        if (len(name) >= 3):
            return True
        return False
    
u1 = User("Arshdeep")
u2 = User("Sam")

print(User.get_total_users())     # 2
print(User.is_valid_name("Jo"))   # False
print(User.is_valid_name("John")) # True