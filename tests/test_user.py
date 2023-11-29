from lib.user import User

# Test that User constructs with id, email_address
# and username
def test_init():
    user = User(1, "fakeemail@fake.com", "fakeusername")
    assert user.id == 1
    assert user.email_address =="fakeemail@fake.com"
    assert user.username == "fakeusername"

# Test that we can compare two identical users
# and have them be equal
def test_users_are_equal():
    user1 = User(1, "fakeemail@fake.com", "fakeusername")
    user2 = User(1, "fakeemail@fake.com", "fakeusername")
    assert user1 == user2