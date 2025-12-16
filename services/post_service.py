class PostService:
    def __init__(self, client):
        self.client = client
        self.endpoint = "/posts"

    def get_single_post(self, post_id):
        return self.client.get(f"{self.endpoint}/{post_id}")

    def get_all_posts(self):
        return self.client.get(self.endpoint)

    def create_new_post(self, title, body, user_id):
        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        return self.client.post(self.endpoint, payload)

    def update_post_title(self, post_id, new_title):
        payload = {"title": new_title}
        return self.client.patch(f"{self.endpoint}/{post_id}", payload)

    def delete_post(self, post_id):
        return self.client.delete(f"{self.endpoint}/{post_id}")