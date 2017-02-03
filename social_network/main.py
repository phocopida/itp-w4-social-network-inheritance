from social_network.accounts import User
from social_network.posts import TextPost, PicturePost, CheckInPost


def main():
    john = User("John", "Lennon", "john@rmotr.com")
    paul = User("Paul", "McCartney", "paul@rmotr.com")
    george = User("George", "Harrison", "george@rmotr.com")
    ringo = User("Ringo", "Starr", "ringo@rmotr.com")

    # John > Paul, George, Ringo
    # George > Paul, John
    # Ringo > John
    # Paul > /

    john.follow(paul)
    john.follow(george)
    john.follow(ringo)

    george.follow(paul)
    george.follow(john)

    ringo.follow(john)

    john.add_post(TextPost("All you need is love!"))
    john.add_post(PicturePost("Check my new submarine.",
                              image_url='imgur.com/submarine.jpg'))

    george.add_post(TextPost("My guitar gently weeps..."))
    george.add_post(TextPost("For you, I'd go full blue..."))

    paul.add_post(PicturePost("Check my new guitar",
                              image_url="imgur.com/guitar.png"))
    paul.add_post(CheckInPost(
        "At 20 Forthlin Road", latitude="20.111", longitude="-10.2222"))

    paul.add_post(CheckInPost(
        "At Abbey Road Studios", latitude="19.111", longitude="-9.2222"))

    print("### John's timeline")
    for post in john.get_posts_by_followers():
        print(post)

if __name__ == '__main__':
    main()
