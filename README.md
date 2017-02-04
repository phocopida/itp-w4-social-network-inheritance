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

## Following users

Users will be able to follow other users. The `follow` method is super simple:

```python
john = User("John", "Lennon", "john@rmotr.com")
paul = User("Paul", "McCartney", "paul@rmotr.com")

john.follow(paul)
print(john.followers)
>>> [<User: "Paul McCartney">]
```

## A user's timeline

This is should be exactly like twitter. A user will have a timeline, that's just a list of posts created by other users that we're following, sorted by datetime (last first).

```python
john = User("John", "Lennon", "john@rmotr.com")
paul = User("Paul", "McCartney", "paul@rmotr.com")
george = User("George", "Harrison", "george@rmotr.com")

john.follow(paul)
john.follow(george)

paul.add_post(TextPost("Post 1"))
george.add_post(TextPost("Post 2"))
paul.add_post(TextPost("Post 3"))

print(john.get_timeline())
>>> [<TextPost: Post 3>, <TextPost: Post 2>, <TextPost: Post 1>
```

## Reading Posts

Finally, one of the most interesting use cases of this project is going to be realted to the "visual representation" of the posts. It's a great example of [Polymorphism](https://en.wikipedia.org/wiki/Polymorphism_(computer_science)). The concept is simple. If I try to print different types of posts, I'm going to get different representations. Example:


```python
john = User("John", "Lennon", "john@rmotr.com")
post_1 = TextPost("All you need is love!")
post_2 = PicturePost("Check my new submarine.", image_url='imgur.com/submarine.jpg')
post_3 = CheckInPost("At Abbey Road Studios", latitude="19.111", longitude="-9.2222")
john.add_post(post_1)
john.add_post(post_2)
john.add_post(post_3)

print(post_1)
"""
John Lennon: "All you need is love!"
  Friday, Feb 03, 2017
"""

print(post_2)
"""
John Lennon: "Check my new guitar"
  Pic URL: imgur.com/guitar.png
  Friday, Feb 03, 2017
"""

print(post_3)
"""
John Checked In: "At Abbey Road Studios"
  19.111, -9.2222
  Friday, Feb 03, 2017
"""
```
**(check tests to see more examples)**
