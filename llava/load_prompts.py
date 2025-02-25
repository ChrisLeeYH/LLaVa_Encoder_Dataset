import os
from pathlib import Path

def load_prompts(prompt_folder):
    """
    Loads all the prompts from text files in the given folder.
    
    :param prompt_folder: Path to the folder containing prompt files.
    :return: List of prompts with their file names and content.
    """
    prompts = []
    for prompt_file in Path(prompt_folder).glob("*.txt"):
        with open(prompt_file, 'r', encoding='utf-8') as file:
            prompts.append({
                'file_name': prompt_file.stem,  # Store the file name to use in CSV naming
                'content': file.read().strip()  # Read the prompt content and strip extra whitespace
            })
    return prompts
