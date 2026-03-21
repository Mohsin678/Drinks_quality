import os
import logging 
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')


project_name = "Datascience"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "app.py"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir,filename  = os.path.split(filepath)

    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"creating directory{file_dir} for filename{filename}")

    if(not os.path.exists(filepath))or(os.path.getsize(filepath)==0):
        with open(filepath,"w")as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
            