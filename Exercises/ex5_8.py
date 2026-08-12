profiles = []
if profiles:
    for profile in profiles:
        if profile == 'a':
            print(f"Hello {profile}, would you like to see a status report?")
        else:
            print(f"Hello {profile}, thank you for logging in again.")
else:
    print("We need to find some users!")