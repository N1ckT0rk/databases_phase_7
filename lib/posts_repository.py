from lib.posts import Post

class PostRepository:

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            item = Post(row['id'], row['title'], row['content'], row['number_of_views'], row['user_id'])
            posts.append(item)
        return posts
    
    def find(self, post_id):
        rows = self.connection.execute('SELECT * FROM posts WHERE id = %s', [post_id])
        item = Post(rows[0]["id"], rows[0]["title"], rows[0]["content"], rows[0]["number_of_views"], rows[0]["user_id"])
        return item

    def create(self, post):
        self.connection.execute('INSERT INTO posts (title, content, number_of_views, user_id) VALUES (%s, %s, %s, %s)', 
            [post.title, post.content, post.number_of_views, post.user_id])
        return None

    def delete(self, post_id):
        self.connection.execute('DELETE FROM posts WHERE id = %s', [post_id])
        return None