import argparse
import json
import os
from requests_oauthlib import OAuth1Session

OAUTH_REQUEST_TOKEN_URL = 'https://trello.com/1/OAuthGetRequestToken'
OAUTH_BASE_AUTHORIZE_URL = 'https://trello.com/1/OAuthAuthorizeToken'
OAUTH_ACCESS_TOKEN_URL = 'https://trello.com/1/OAuthGetAccessToken'
CONFIG_FILE = os.path.expanduser('~/.trlo')

class TrelloSession(OAuth1Session):
    @classmethod
    def from_config_file(cls, fname=CONFIG_FILE):
        creds = json.load(open(fname))
        return cls(**creds)

    def request(self, method, url, *args, **kwargs):
        if '://' not in url:
            url = 'https://trello.com/1/' + url.lstrip('/')
        return super(TrelloSession, self).request(method, url, *args, **kwargs)

def authorize(client_key, client_secret, credfile=CONFIG_FILE, app='trlo.py',
              expiration='never', scope='read,write'):
    """
    Authorize with Trello, saving creds to `credfile`.
    """
    # 1. Obtain the request token.
    oauth = OAuth1Session(client_key, client_secret=client_secret)
    request_token = oauth.fetch_request_token(OAUTH_REQUEST_TOKEN_URL)

    # 2. Authorize the user (in the browser).
    authorization_url = oauth.authorization_url(OAUTH_BASE_AUTHORIZE_URL,
        name=app, expiration=expiration, scope=scope)
    print("Please visit the following URL to authorize this app:")
    print(authorization_url)
    print('')
    print("Once you've authorized, copy and paste the token Trello gives you below.")
    # Py3K backwards-compatibility shim
    global input
    try:
        input = raw_input
    except NameError:
        pass
    verifier = input("Trello's token: ").strip()

    # 3. Obtain the access token
    oauth = OAuth1Session(client_key, client_secret=client_secret,
        resource_owner_key=request_token['oauth_token'],
        resource_owner_secret=request_token['oauth_token_secret'],
        verifier=verifier)
    access_token = oauth.fetch_access_token(OAUTH_ACCESS_TOKEN_URL)

    # Save all our creds to ~/.trlo so we can get at 'em later.
    # The names are specially chosen so we can do OAuth1Session(**creds)
    creds = {
        'client_key': client_key,
        'client_secret': client_secret,
        'resource_owner_key': access_token['oauth_token'],
        'resource_owner_secret': access_token['oauth_token_secret'],
    }
    with open(credfile, 'w') as fp:
        json.dump(creds, fp)

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Authorize with Trello")
    parser.add_argument('--key', required=True,
        help="Your Trello key, the first value at https://trello.com/1/appKey/generate")
    parser.add_argument('--secret', required=True,
        help="Your Trello secret, the second value at https://trello.com/1/appKey/generate")
    args = parser.parse_args()
    authorize(args.key, args.secret)
