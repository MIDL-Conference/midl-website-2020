#!/usr/bin/env python3

import json
from sys import argv
from pathlib import Path
from secrets import token_hex
from subprocess import check_output, CalledProcessError


CREATE_TEMPLATE = '''curl -s -H "X-Auth-Token: {TOKEN}" \\
 -H "X-User-Id: {USERID}" \\
 -H "Content-type: application/json" \\
 http://localhost:3000/api/v1/users.create \\
 -d '{{ "name": "{name}", "email": "{email}", "password": "{password}", "username": "{username}", "requirePasswordChange": true, "verified": false, "sendWelcomeEmail": true }}' '''

GET_CHANNEL_ID_TEMPLATE = '''curl -s -H "X-Auth-Token: {TOKEN}" \\
     -H "X-User-Id: {USERID}" \\
     http://localhost:3000/api/v1/channels.info?roomName={title} '''

GET_USER_ID_TEMPLATE = '''curl -s -H "X-Auth-Token: {TOKEN}" \\
     -H "X-User-Id: {USERID}" \\
     http://localhost:3000/api/v1/users.info?username={username} '''

ADD_CHANNEL_TEMPLATE = '''curl -s -H "X-Auth-Token: {TOKEN}" \\
 -H "X-User-Id: {USERID}" \\
 -H "Content-type: application/json" \\
 http://localhost:3000/api/v1/channels.invite \\
 -d '{{ "roomId": "{channel_id}", "userId": "{user_id}" }}' '''


if __name__ == "__main__":
    assert len(argv) == 4

    csv_path: Path = Path(argv[1])
    assert csv_path.exists()

    TOKEN: str = argv[2]
    USERID: str = argv[3]

    print(">>> Creating users...")
    tot: int = 1
    skipped: int = 0
    with open(csv_path, 'r') as f:
        for line in f.read().splitlines():
            name, email, paper_id = line.split(',')
            sanitized_name = name.replace("'", '.').replace('"', '.')
            username: str = name.casefold().replace(' ', '.').replace('-', '.').replace("'", '.').replace('"', '.')
            password: str = token_hex(4)

            print(f">> Creating for {sanitized_name}, {email}, {password}, {username}")

            try:
                # Pay attention: I do not lower case the name, but the channel url will be lowercased
                create_output = check_output(CREATE_TEMPLATE.format(TOKEN=TOKEN,
                                                                    USERID=USERID,
                                                                    name=sanitized_name,
                                                                    email=email,
                                                                    password=password,
                                                                    username=username),
                                             shell=True)
                create_json = json.loads(create_output)
            except CalledProcessError as e:
                print(e.output)
                print(e.args)
                exit(-1)
            except json.decoder.JSONDecodeError as e:
                print(e)
                print(create_output)
                exit(-1)

            if not create_json["success"] and create_json["errorType"] == 'error-field-unavailable':
                print(f"> email {email} or username {username} already in use, skipping..")
                skipped += 1
            elif not create_json["success"]:
                print(f"\t{create_json}")
                exit(-1)

            # if paper_id:
            #     if create_json["success"]:
            #         user_id = create_json["user"]["_id"]
            #     else:
            #         getuid_json = json.loads(check_output(GET_USER_ID_TEMPLATE.format(TOKEN=TOKEN,
            #                                                                           USERID=USERID,
            #                                                                           username=username),
            #                                               shell=True))
            #         user_id = getuid_json['user']["_id"]
            #         print(user_id)

            #     # getcid_output = check_output(GET_CHANNEL_ID_TEMPLATE.format(TOKEN=TOKEN,
            #     #                                                             USERID=USERID,
            #     #                                                             title='authors'),
            #     #                              shell=True)
            #     # print(getcid_output)
            #     # getcid_json = json.loads(getcid_output)
            #     # print(f"\t{getcid_json}")
            #     # channel_id = getcid_json['channel']["_id"]

            #     # Fuck this, let's hardcore the room channel
            #     channel_id = "TTgcSRh83SD8TMwdv"
            #     # channel_id = "S6FLrrDXpJmeQqGd4"

            #     print(channel_id, user_id)
            #     add_channel_json = json.loads(check_output(ADD_CHANNEL_TEMPLATE.format(TOKEN=TOKEN,
            #                                                                            USERID=USERID,
            #                                                                            channel_id=channel_id,
            #                                                                            user_id=user_id),
            #                                                shell=True))
            #     assert add_channel_json["success"], add_channel_json
            #     print("> added to the #author channel.")

            tot += 1

    print(f"\nCreation complete for {tot} users ({skipped} skipped)")
