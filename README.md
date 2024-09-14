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

## Running Terraria Closer

To run the project, use:

*Unix/Mac:*
`python3 terraria_closer.py`

*Windows:*
`py terraria_closer.py`
