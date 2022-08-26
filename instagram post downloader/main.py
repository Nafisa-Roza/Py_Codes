import instaloader
mod = instaloader.Instaloader()
a=input("Enter The Profile Name - ")
mod.download_profile(a,profile_pic_only=True)


#pip install instaloader