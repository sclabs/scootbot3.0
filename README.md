scootbot3.0
===========

custom multi-purpose slack chatbot

Quick start
-----------

1. Clone this repository with

        git clone git://github.com/sclabs/scootbot3.0.git

   and change directory into the repo root directory.

2. Set the following environment variables, for example in `~/.bashrc`

        export SCOOTBOT_TOKEN=...
        export SCOOTBOT_APP_TOKEN=...
        export SCOOTBOT_SIGNING_SECRET=...
        export SCOOTBOT_OSU_API_KEY=...
        export SCOOTBOT_STEAM_API_KEY=...
        export SCOOTBOT_TWITCH_CLIENT_ID=...

3. Set up a python3.8 venv with all dependencies

        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements-dev.in
        pip install -r requirements.txt
        pip install -e .

4. Test the bot locally

        scootbot3

Secrets
-------

### Slack App

Create a Slack App, set it up as a bot, install it to your workspace, and make
the following secrets, saving them to the indicated environment variables:

- `SCOOTBOT_TOKEN`: Bot User OAuth Token (`xoxb-`) with following scopes
  - channels:history
  - channels:read
  - chat:write
  - groups:history
  - groups:read
  - im:history
  - mpim:history
  - reactions:write
  - user:read
- `SCOOTBOT_APP_TOKEN`: App-Level Token (`xapp-`) with connections:write
- `SCOOTBOT_SIGNING_SECRET`: Slack App Signing Secret

Under Event Subscriptions > Subscribe to bot events make sure to subscrube to
 - message.channels
 - message.groups
 - message.in
 - message.mpim

### Integrations

- `SCOOTBOT_OSU_API_KEY`
- `SCOOTBOT_STEAM_API_KEY`
- `SCOOTBOT_TWITCH_CLIENT_ID`

Compiling dependencies
----------------------

    pip-compile --annotation-style=line
