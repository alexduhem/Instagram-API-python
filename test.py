#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
import json

from InstagramAPI import InstagramAPI

api = InstagramAPI("ragematism", "3A5x(9MPG2iaw|Rr'")
if (api.login()):
    api.getSelfUserFeed()  # get self user feed
    print(api.LastJson)  # print last response JSON
    print("IN TEST ITS GOOD")

    otherApi = InstagramAPI()
    print(json.dumps(api.to_json(), indent=4, sort_keys=True))
    otherApi.from_json(api.to_json())
    otherApi.searchUsername("natgeo")
    print(json.dumps(otherApi.LastJson, indent=4, sort_keys=True))
else:
    print("Can't login!")
