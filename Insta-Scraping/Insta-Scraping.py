import sys
import instaloader

sys.stdin.reconfigure(encoding='utf-8')

bot = instaloader.Instaloader()
Username = input('Enter the Account Username: ')

bot.download_profile(Username, profile_pic_only = True)
profile = instaloader.Profile.from_username(bot.context, Username)

original_stdout = sys.stdout
with open('UserInfo.txt', 'w',encoding='utf-8') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print("Username: ", profile.username)
    print("User ID: ", profile.userid)
    print("Number of Posts: ", profile.mediacount)
    print("Followers: ", profile.followers)
    print("Followees: ", profile.followees)
    print("Bio: ", profile.biography,profile.external_url)
    sys.stdout = original_stdout # Reset the standard output to its original value

posts = profile.get_posts()
try:
    for index, post in enumerate(posts, 1):
        bot.download_post(post, target=f"Post{profile.username}_{index}")
except Exception as e:    
    print(repr(e))
    
finally:
    print("All Done!")
exit()