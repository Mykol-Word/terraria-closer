# Terraria Closer

Terraria Closer runs an automated mouse click/move sequence upon a user-specified close tag being sent from a specific channel in Dicord. I made it to close my Terraria game remotely but you can program anything to be done with just left clicks and mouse movements. 

## Setting up virtual environment

After downloading and unzipping the project, set the "terraria-closer" project folder as your working directory and run:

*Unix/Mac:*
`python3 -m venv .venv`

*Windows:*
`py -m venv .venv`

Then you must activate your virtual environment with:

*Unix/Mac:*
`.venv/bin/python`

*Windows:*
`.venv\Scripts\activate`

## Installing requirements

Once your virtual environment is set up, download the project requirements with:

`pip install -r requirements.txt`

## Configuring keys.json

The project comes with a "keys_template.json" file which will contain both your Discord authorization token and specified channel ID. These keys are what allow the program to check for a specific closing within a Discord chat you have access to. Upon first execution, your "keys_template.json" file will be renamed to "keys.json" so that Git will not track it in the event that you push a rendition of the project to GitHub.

*Note that your Discord token is essentially a password to your account (and should be treated as such) that gives the program authorization to read your Discord chats.*

*This program in no way collects or stores your Discord token beyond your local "keys.json" file, nor does it collect or store any of your private Discord information (e.g. private messages, joined servers, etc.). The chat information requested using your Discord token is solely used when checking for a specific closing tag and is not used or stored beyond program termination or completion.*

*If you are to leak access to your Discord token, you should change your password immediately. This will invalidate that token.* 

To find your Discord token, [follow this simple guide](https://www.androidauthority.com/get-discord-token-3149920/). To get your desired channel ID, simply right click any discord text channel or direct message chat and select "Copy Channel ID" at the bottom of the pop-up. Use these values to replace the template values for "user_key" and "chat_key" in "keys_template.json" respectively. 

## Running Terraria Closer

To run the project, use:

*Unix/Mac:*
`python3 terraria_closer.py`

*Windows:*
`py terraria_closer.py`
