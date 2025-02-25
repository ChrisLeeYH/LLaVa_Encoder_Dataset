import os
import argparse
import time
from llava.load_prompts import load_prompts
from llava.process_images import process_images
from llava.save_results import save_results

def save_runtime(total_runtime, output_folder):
    """
    Saves the total runtime to a text file in the output folder.
    
    :param total_runtime: The total runtime in seconds.
    :param output_folder: The folder where the runtime text file will be saved.
    """
    runtime_file_path = os.path.join(output_folder, 'total_runtime.txt')
    with open(runtime_file_path, 'w') as f:
        f.write(f"Total runtime: {total_runtime:.2f} seconds")
    print(f"\nTotal runtime saved to {runtime_file_path}")

def process_all_prompts(image_folder, prompt_folder, repeat=2):
    """
    Processes each prompt in the prompt folder and generates CSV files with results.

    :param image_folder: Path to the folder containing images.
    :param prompt_folder: Path to the folder containing prompt text files.
    :param repeat: The number of times to repeat the inference per image (default is 2).
    """
    start_time = time.time()

    output_folder = prompt_folder

    prompts = load_prompts(prompt_folder)
    
    for prompt in prompts:
        print(f"Processing prompt: {prompt['file_name']}")
        
        results = process_images(image_folder, prompt['content'], repeat)
        
        save_results(results, prompt['file_name'], output_folder)
        print(f"Results saved to {output_folder}/llava_{prompt['file_name']}.csv")

    end_time = time.time()
    total_runtime = end_time - start_time
    
    save_runtime(total_runtime, output_folder)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process images with LLaVA model using prompts.")
    parser.add_argument('image_folder', type=str, help="Path to the folder containing images.")
    parser.add_argument('prompt_folder', type=str, help="Path to the folder containing prompt text files.")
    parser.add_argument('--repeat', type=int, default=2, help="Number of times to repeat inference for each image (default is 2).")
    
    args = parser.parse_args()
    
    process_all_prompts(args.image_folder, args.prompt_folder, args.repeat)

# python AADB.py ./test Raw/AADB

