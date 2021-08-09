#!/usr/bin/env python3
# coding: utf8
from mastodon import Mastodon

app_name = 'MastodonPyApp'
api_base_url = 'https://mstdn.jp/'
secret_file = '/home/pi/root/work/record/pc/account/mastodon/mstdn.jp.ytyaru.secret'
Mastodon.create_app(
     app_name,
     api_base_url = api_base_url,
     to_file = 'client_key.txt'
#     to_file = secret_file
)

