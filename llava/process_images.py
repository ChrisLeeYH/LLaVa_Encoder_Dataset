import time
from pathlib import Path
import ollama

def chat_with_llava(image_path, prompt):
    """
    Uses the LLaVA model for inference, taking an image and a text prompt as input.
    
    :param image_path: Path to the image file.
    :param prompt: The text prompt corresponding to the image.
    :return: Model-generated text output.
    """
    res = ollama.chat(
        model="llava:34b",
        messages=[
            {
                'role': 'user',
                'content': prompt,
                'images': [image_path]
            }
        ],
        options={'temperature': 0.5}, 
    )
    return res['message']['content']

def process_images(image_folder, prompt, repeat=2):
    """
    Process all images in the given folder using the provided prompt, repeating the process for each image.
    
    :param image_folder: Path to the folder containing images.
    :param prompt: Text prompt to use with the images.
    :param repeat: The number of times to repeat the inference per image (default is 2).
    :return: List of tuples (image_name, output_1, output_2, ...)
    """
    results = []
    
    image_files = list(Path(image_folder).glob("*"))
    total_images = len(image_files)
    
    if total_images == 0:
        raise Exception("No images found.")
    
    start_time = time.time()
    
    for idx, image_path in enumerate(image_files):  
        if image_path.is_file():
            image_name = image_path.stem
            outputs = []
            
            for _ in range(repeat):
                output = chat_with_llava(image_path, prompt)
                outputs.append(output)
            
            results.append((image_name, *outputs))
        print(f"Processed image {idx + 1}/{total_images} ({(idx + 1) / total_images * 100:.2f}%)")
    
    end_time = time.time()
    total_runtime = end_time - start_time
    print(f"\nTotal runtime: {total_runtime:.2f} seconds")
    
    return results
