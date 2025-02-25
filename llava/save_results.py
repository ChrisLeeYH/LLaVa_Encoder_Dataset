import csv
import os

def save_results(results, prompt_name, output_folder):
    """
    Saves the results of the processing into a CSV file.
    
    :param results: List of tuples (image_name, output_1, output_2, ...).
    :param prompt_name: The name of the prompt file (to be used in the CSV filename).
    :param output_folder: Folder where the CSV file will be saved.
    """
    output_file = os.path.join(output_folder, f"llava_{prompt_name}.csv")
    
    num_outputs = len(results[0]) - 1

    header = ['Image Name'] + [f'Output {i+1}' for i in range(num_outputs)]
    
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header) 
        
        # Write the result rows
        for result in results:
            writer.writerow(result)

