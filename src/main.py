#
# Author: Daniel Dittenhafer
#
#     Created: Dec 1, 2016
#
# Description: Main entry point for Trump Cabinet network analysis.
#
from linkedin import linkedin

_CLIENTID = "78mswaaquqtli4"
_CLIENTSECRET = "aU4kKE5rRSkuwvZj"

_AUTHORIZATION_CODE = "AQR83lzo5lZJgjldp7wlRe1ZEEaJtEvYxrr9V25ecTLe0WWwmMzdHeIN_WcWd-n7cZw9xL5b7ckwH6RaKrzFsDKO3IpAM6Jb_X-yqwI1RCPrGLwa7rw"

_ACCESS_TOKEN = "AQX7pBIXjAccD6APfjBWzElRkmMRxJk8qkaQ0HZL5t8glJN4pN2tZ9Ja8pXGMUVFVnkpbXXZ5s7SHMZmTKtiYWGgVpIWD_Xhsn0m_D1pliukshg1w6e0NpkMp1tbWK57LdAHxaXKafUSGa_O5Ss1rqLlbj_kRuQhU0ggt_k95iZ0eZUbXtQ"
_ACCESS_TOKEN_EXPIRES_IN = 5183999

def main():
    authentication = linkedin.LinkedInAuthentication(_CLIENTID, _CLIENTSECRET, "http://localhost/",
                                                     [linkedin.PERMISSIONS.BASIC_PROFILE])
    #authentication = linkedin.LinkedInDeveloperAuthentication(_CLIENTID, _CLIENTSECRET,
    #                                                          USER_TOKEN, USER_SECRET,
    #                                                          RETURN_URL, linkedin.PERMISSIONS.enums.values())


    print authentication.authorization_url
    authentication.token = linkedin.AccessToken(_ACCESS_TOKEN, _ACCESS_TOKEN_EXPIRES_IN)


    #authentication.authorization_code = _AUTHORIZATION_CODE
    #authentication.get_access_token()
    print authentication.token

    # Pass it in to the app...

    application = linkedin.LinkedInApplication(authentication)

    # Use the app....

    g = application.get_profile(selectors="first-name,last-name,formatted-name,positions")
    print g

    g = application.search_profile("Justin Hink")
    print g


# This is the main of the program.
if __name__ == "__main__":
    main()