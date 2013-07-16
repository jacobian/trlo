# trlo

This is `trlo`, a minimalist Trello API client. It's really nothing more than  an ultra-thin layer on top of [requests](http://python-requests.org/) that  helpswith the OAuth flow. You'll still need to read [Trello's API docs]() and know how to use [requests](http://python-requests.org/), and generally be comfortable consuming REST resources by hand. If you want something more abstract with crazy new-fangled things like classes and such then look elsewhere.

## Quickstart

1. Install: `pip install trlo`, natch.

2. Authorize: `python -m trlo --key=KEY --secret=SECRET`. [Find your key and secret here.](https://trello.com/1/appKey/generate). This saves your creds to `~/.trlo` for later user.

3. Do stuff:

```python
import trlo

trello = trlo.TrelloSession.from_config_file()
for board in trello.get('members/me/boards').json():
    print board['name']
```

