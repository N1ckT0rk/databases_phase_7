from lib.user_repository import UserRepository
from lib.user import User

# When we call UserRepository#all
# We get a list of Artist objects reflecting the seed data.
def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repository = UserRepository(db_connection)

    assert user_repository.all() == [
        User(1, 'notreal@notreal.com', 'NotReal'),
        User(2, 'defonotreal@defonotreal.com', 'DefoNotReal')
    ]
# When we call UserRepository#find
# We get a single Artist object reflecting the seed data.
def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repository = UserRepository(db_connection)

    assert user_repository.find(1) == User(1, 'notreal@notreal.com', 'NotReal')


# When we call UserRepository#create
# We get a new record in the database.
def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repository = UserRepository(db_connection)
    new_user = User(3, 'scam@scam.com', 'ScamUser')

    user_repository.create(new_user)

    assert user_repository.all() == [
        User(1, 'notreal@notreal.com', 'NotReal'),
        User(2, 'defonotreal@defonotreal.com', 'DefoNotReal'),
        User(3, 'scam@scam.com', 'ScamUser')
    ]

# When we call UserRepository#delete
# We remove a record from the database.
def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repository = UserRepository(db_connection)
    # new_user = User(3, 'scam@scam.com', 'ScamUser')
    # user_repository.create(new_user)

    user_repository.delete(2)

    assert user_repository.all() == [
        User(1, 'notreal@notreal.com', 'NotReal'),
        # User(2, 'defonotreal@defonotreal.com', 'DefoNotReal')
    ] 