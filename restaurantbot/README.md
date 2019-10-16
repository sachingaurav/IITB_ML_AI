# Restaurant Bot

## Prerequisite
Install Visual studio code (Preferably)
Set tab width to 4 spaces in your favorite text editor

In windows 10, enable creating symbolic links using instruction in link https://learn.upgrad.com/v/course/132/question/92071. 
You need to update policy mentioned in https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links
using gpedit.msc. Make sure to do 'gpupdate /force' and then reboot system afterwards.

Create python virtual environment or new conda environment for Python 3.6.5
- conda create -n nlp python=3.6.5

Start new virtual environment or conda environment in command prompt

Open prerequisites folder

- Copy rasa_core-master.zip and rasa_nlu-master.zip outside the repository to some temporary location.
- Unzip rasa_core-master.zip to folder rasa_core-master
- Unzip rasa_nlu-master.zip to folder rasa_nlu-master
- Copy rasa_nlu_requirements.txt in folder rasa_nlu-master
- Copy rasa_core_requirements.txt in folder rasa_core-master

cd rasa_nlu-master

- pip install -r rasa_nlu_requirements.txt
- pip install -e .
- pip install rasa_nlu[spacy]
- python -m spacy download en_core_web_md 
- python -m spacy link en_core_web_md en

cd rasa_core-master

- pip install -r rasa_core_requirements.txt
- pip install -e .

Install node.js and NPM if not installed already. DO below from any folder.
- npm i -g rasa-nlu-trainer

## Preparation
Create folder secrets in top level of your downloaded code.
Create file secrets.yml inside folder secrets. DO not commit this file in repository.
Format of secrets.yml files is as follows

```
zomato_api_key: 'a872d709e02d92e67f9b'
sender_email: 'purnendu.ghosh@iiitb.net'
sender_password: 'password'
```

## Run the bot

Start new virtual environment or conda environment in command prompt that was 
created in prerequisites step

Run below

- python nlu_model.py
- python train_init.py
- python dialogue_management_model.py

## Create new stories
Run as follows
- python train_online.py
- Save stories file as other than stories.md, say as stories2357.md
- Copy content of stories2357.md to stories.md and update
- Don't forget to mark your stories like
```
## Generated Story AK-355706069323404492
## Generated Story SM-355706069323404492
## Generated Story SG-355706069323404492
## Generated Story PG-355706069323404492
```
- Add your initials in the heading for sure. It will make for better reading