from lib.posts_repository import PostRepository
from lib.posts import Post
# When we call UserRepository#all
# We get a list of Artist objects reflecting the seed data.
def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    post_repository = PostRepository(db_connection)
    posts = post_repository.all()
    assert posts == [
        Post(1, 'faketitle', 'fakecontent', 0, 1),
        Post(2, 'faketitle2', 'fakecontent2', 0, 2),
    ]

# # When we call UserRepository#find
# # We get a single Artist object reflecting the seed data.
def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    post_repository = PostRepository(db_connection)
    assert post_repository.find(1) == Post(1, 'faketitle', 'fakecontent', 0, 1)


# # When we call UserRepository#create
# # We get a new record in the database.
def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    post_repository = PostRepository(db_connection)
    new_post = Post(None, 'Title3', 'Content2', 0, 2)

    post_repository.create(new_post)

    assert post_repository.all() == [
        Post(1, 'faketitle', 'fakecontent', 0, 1),
        Post(2, 'faketitle2', 'fakecontent2', 0, 2),
        Post(3, 'Title3', 'Content2', 0, 2),
    ]

# # When we call UserRepository#delete
# # We remove a record from the database.
def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    post_repository = PostRepository(db_connection)


    post_repository.delete(2)

    assert post_repository.all() == [
        Post(1, 'faketitle', 'fakecontent', 0, 1),
    ] 