# Rmotrgram

Today we're going to build a clone of a social network (really similar to the blue bird one, but keep it a secret).

As any other social network we're going to have different types of `Post`s. All these different types of Posts should inherit from the parent `Post` class:

* `TextPost`: Just a simple text post. Should be constructed as `TextPost(text="Post Text").
* `PicturePost`: A post containing text and the URL of a picture: Should be constructed as `PicturePost(text="Post Text").
* `CheckInPost`: A post containing text and coordinates of the user's position. Should be constructed as `CheckInPost(text="Post Text", latitude="40.741895", longitude="-73.989308")`.

Rmotrgram also has users. A user is a simple class that can be created as: `User(first_name, last_name, email)`.

## Creating posts

Posts are going to be created by users. Once we have our user created, we're going to use the `add_post` method from the user class. Example, to create a text post for our user John, we'll do something like:

```python
john = User("John", "Lennon", "john@rmotr.com")
text_post = TextPost("All you need is love!")
text_post.user = None  # Important!

john.add_post(text_post)

text.post.user == john  # Important!
```

As you can see from our previous example, a post is created without a user. It's "orphan" we might say. But once we add that post to a user, the post's user attribute should be assigned.

```python
```
