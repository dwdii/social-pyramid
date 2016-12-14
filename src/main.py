#
# Author: Daniel Dittenhafer
#
#     Created: Dec 1, 2016
#
# Description: Main entry point for Trump Cabinet network analysis.
#
from linkedin import linkedin
import twitter
import csv
import os.path
import time

_CLIENTID = "78mswaaquqtli4"
_CLIENTSECRET = "aU4kKE5rRSkuwvZj"

_AUTHORIZATION_CODE = "AQQLynVv-_kRyA_4iQTeTPPIjv44mu9tGwZycumWICpVyUgbf9fRtwAKG7WI-6Dayi_nBz8V_statGcfuyGjYuAoJR5m-XFl41rPhxzXlqz6iekQHCo" \
                      #"AQR83lzo5lZJgjldp7wlRe1ZEEaJtEvYxrr9V25ecTLe0WWwmMzdHeIN_WcWd-n7cZw9xL5b7ckwH6RaKrzFsDKO3IpAM6Jb_X-yqwI1RCPrGLwa7rw"

_ACCESS_TOKEN = "AQX7pBIXjAccD6APfjBWzElRkmMRxJk8qkaQ0HZL5t8glJN4pN2tZ9Ja8pXGMUVFVnkpbXXZ5s7SHMZmTKtiYWGgVpIWD_Xhsn0m_D1pliukshg1w6e0NpkMp1tbWK57LdAHxaXKafUSGa_O5Ss1rqLlbj_kRuQhU0ggt_k95iZ0eZUbXtQ"
_ACCESS_TOKEN_EXPIRES_IN = 5183999

def linkedin_test():
    authentication = linkedin.LinkedInAuthentication(_CLIENTID, _CLIENTSECRET, "http://localhost/",
                                                     [linkedin.PERMISSIONS.BASIC_PROFILE])
    # authentication = linkedin.LinkedInDeveloperAuthentication(_CLIENTID, _CLIENTSECRET,
    #                                                          USER_TOKEN, USER_SECRET,
    #                                                          RETURN_URL, linkedin.PERMISSIONS.enums.values())


    print authentication.authorization_url
    authentication.token = linkedin.AccessToken(_ACCESS_TOKEN, _ACCESS_TOKEN_EXPIRES_IN)

    # authentication.authorization_code = _AUTHORIZATION_CODE
    # authentication.get_access_token()
    print authentication.token

    # Pass it in to the app...

    application = linkedin.LinkedInApplication(authentication)

    # Use the app....

    g = application.get_profile(selectors="first-name,last-name,formatted-name,positions")
    print g

    params = {'keywords': 'Justin Hink'}

    g = application.search_profile([{'people': ['first-name', 'last-name']}], params)
    print g

def twitter_test(screenname):

    api = twitter.Api(consumer_key='UzF8FKAMeVc1crLEhUtTQyEgI',
                           consumer_secret='uKdaftSyh9opBfeJ5ohVlK1HkA7xGB5hMDNpMO7dX8nOmeto5H',
                           access_token_key='85418124-FzzYpLl4BPwNjPTNqWWQtFm2D9xEttazXfL6Px61O',
                           access_token_secret='K4LudWpqqz86b6A1DcbpdSw1vYVk6XDBcNJkPqDL816cn')

    print(api.VerifyCredentials())

    bContinue = True
    cursor = -1
    followDict = {}
    file = 'trump_followers_plus.csv'
    mode = 'w'

    if os.path.isfile(file):
        mode = 'a'
        with open(file, 'r') as mycsvfile:
            dw = csv.reader(mycsvfile)
            for f in dw:
                followDict[f[0]] = int(f[1])

    while bContinue:

        next_cursor, previous_cursor, followers = api.GetFollowersPaged(screen_name=screenname, count=200, skip_status=True)

        print(followers[1])
        with open(file, mode) as mycsvfile:
            dw = csv.writer(mycsvfile)
            for f in followers:
                if(f.screen_name not in followDict):
                    followDict[f.screen_name] = f.followers_count
                    dw.writerow([f.screen_name, f.followers_count, f.lang, f.location, f.time_zone])

        if next_cursor:
            cursor = next_cursor
            time.sleep(60)

        if next_cursor == 0 or next_cursor == previous_cursor:
            break

    return None

def main():
    #linkedin_test()

    twitter_test("realDonaldTrump")


# This is the main of the program.
if __name__ == "__main__":
    main()