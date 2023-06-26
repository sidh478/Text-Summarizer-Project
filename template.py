import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

#local packages
list_of_files = [
    ".github/workflows/.gitkeep", #gitkeep is hidden file
    f"src/{project_name}/__init__.py", #__init__.py is construtor
    f"src/{project_name}/components/__init__.py", #create components folder with constructor file inside
    f"src/{project_name}/utils/__init__.py", #create utils folder with constructor file inside
    f"src/{project_name}/utils/common.py", #create utils folder with common.py file inside
    f"src/{project_name}/logging/__init__.py", #create logging folder with constructor file inside
    f"src/{project_name}/config/__init__.py", #create config folder with constructor file inside
    f"src/{project_name}/config/configuration.py", #create config folder with configuration.py file
    f"src/{project_name}/pipeline/__init__.py", #create pipeline folder with constructor file
    f"src/{project_name}/entity/__init__.py", #create entity folder with constructor file
    f"src/{project_name}/constants/__init__.py", #create constants folder with constructor file
    "config/config.yaml", #create config folder with config.yaml file
    "app.py", #create app.py
    "main.py", #create main.py
    "Dockerfile", #create Docker
    "requirements.txt", #create requirements.txt
    "setup.py", #package
    "research/trials.ipy" #research folder with trials.ipy file
]

for filepath in list_of_files:
    filepath = Path(filepath) #creates windows path
    filedir,filename = os.path.split(filepath) #split file path into directory and filename

    if filedir !="": 
        os.makedirs(filedir, exist_ok=True) #create file if does not exist in the current directory
        logging.info(f"Creating directory:{filedir} for the file {filename}") #logging details

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #checking filepath exits or size of file is empty
        with open(filepath, 'w') as f: #if empty replace it
            pass
            logging.info(f"Creating empty file:{filepath}") #logging detatils
        
    else:
        logging.info(f"{filename} is already exists") #logging details
