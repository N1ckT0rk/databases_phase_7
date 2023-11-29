from lib.posts import Post

# Test that Post constructs with id, title, content, number_of_views
# and user_id
def test_init():
    post = Post(1, "Title", "Content", 0, 1)
    assert post.id == 1
    assert post.title =="Title"
    assert post.content == "Content"
    assert post.number_of_views == 0
    assert post.user_id == 1


# Test that we can compare two identical users
# and have them be equal
def test_users_are_equal():
    post1 = Post(1, "Title", "Content", 0, 1)
    post2 = Post(1, "Title", "Content", 0, 1)
    assert post1 == post2