#! /usr/bin/env python3

import torch
import os
from dotenv import load_dotenv, dotenv_values

# Specify the path to your .env file
dotenv_path = os.path.expanduser('/home/kolim/.env_hftoken')
load_dotenv(dotenv_path=dotenv_path)

config = dotenv_values("/home/kolim/.env_hftoken")

if torch.backends.mps.is_available():
    print("apple mps available")
elif torch.cuda.is_available():
    print("cuda available")
else:
    print("Only cpu available")

# check for HF_TOKEN
hf_token = os.getenv('HF_TOKEN') # doesn't override existing setting
hf_token = config['HF_TOKEN']
pass