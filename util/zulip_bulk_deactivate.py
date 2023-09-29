#!/usr/bin/env python3

import zulip

# Pass the path to your zuliprc file here.
client = zulip.Client(config_file="~/.zuliprc_ucsc-cse232")

# Get all users in the realm
result = client.get_members()

staff_emails_2023 = [
    'lkuper@ucsc.edu' ]

if result['result'] == 'success':
    for user in result['members']:
        # Don't deactivate staff
        if user['delivery_email'] in staff_emails_2023:
            print("Keeping this user:", user['delivery_email'])
        # Deactivate everyone else
        else:
            print("DEACTIVATING this user:", user['delivery_email'], user['user_id'])
            client.deactivate_user_by_id(user['user_id'])
