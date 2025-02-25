# LLaVA Image Processing with Prompts For Each Dataset

This project leverages the LLaVA (Large Language and Vision Assistant) model to process images from a given folder and respond to prompts stored in text files. The results for each image and prompt combination are saved in CSV files, and the total runtime of the processing is logged in a separate text file.

## Features

- Process multiple images with a set of prompts.
- Use the LLaVA model for inference.
- Repeat inference multiple times per image (default: 2).
- Save all results in `CSV files` with image names and outputs.
- Log the total runtime in a `total_runtime.txt` file in the same folder as the prompts.

## Requirements

- Python 3.10
- `ollama` localhost
- Required Python libraries: `requiremnets.text`

## Full Deployment Flows
1. **Ollama Localhost Depolyment (NECESSARY!)**
- Download `ollama.exe` from the following link: https://ollama.com/
- After installing `ollama.exe`, in cmd (win+R):
```bash
ollama run llava:34b
```

- Here, due to some issues of prompts, the outputs from LLaVa 13b are not ideal in tests, so llava:34b is strongly recommended.

- We use this step to download and to deploy llava:34b locally for further use.

2. **Environment Deployment**
- Clone this repository and navigate to LLaVA folder, seeting the folder as the root directory.
```bash
git clone https://github.com/ChrisLeeYH/LLaVa_Encoder_Dataset.git
cd LLaVA_Encoder_Dataset
```

- Deploy the virtual environment and install packages.

```Shell
conda create -n llava python=3.10 -y
conda activate llava
pip install --upgrade pip  # enable PEP 660 support
pip install -r requirements.txt
```

## Insturctions For Use
1. **Directory Structure**

    - `image_folder/`: Directory containing the images to be processed.
    - `prompt_folder/`: Directory containing the text files with the prompt.
    - `output_folder/`: Folder where the results will be saved (in this case, the output folder will be the same as the prompt folder).

2. **Run the Script**

    To process images with the LLaVA model using the prompts in the specified folder, run the following command:

    ```bash
    python <Dataset_Name>.py <image_folder_path> <prompt_folder_path>
    ```

    - `<image_folder>`: Path to the folder containing the images, which need to be replaced with the real folder path.
    - `<prompt_folder>`: Path to the folder containing the prompt text files, which I have set already.

    Example:

    ```bash
    python AADB.py ./AADB_IMAGES ./AADB
    ```

    This will process all the images in `./AADB_IMAGES/` using the prompts in `./AADB/`, repeating the inference 2 times per image.

3. **Output**

    - **CSV Files**: For each prompt, a corresponding CSV file will be saved in the `prompt_folder`. The CSV file will have the following columns:
        - `Image name`: The name of the image.
        - `output_1`, `output_2`, ...: The model's output for each repetition.
        
        Example of a CSV file:

        ```
        Image name, output_1, output_2
        pic01, "output from LLaVA", "output from LLaVA"
        pic02, "output from LLaVA", "output from LLaVA"
        ```

    - **Total Runtime**: A `total_runtime.txt` file will be created in the `prompt_folder`, containing the total time taken to process all the images.

    Example of the `total_runtime.txt` file:

    ```
    Total runtime: 120.45 seconds
    ```

4. **Takeaway**
All we need to do for run the script on each dataset can be concluded as follows:

    - Deploy the Ollama and llava:34b locally.
    - Clone and Navigate to this folder, setting it as root directory.
    - Because the Ollama must be deployed and applied locally, directly accessing the dataset through the url (i.e., googld drive link) is impractical. Directly downloading and puting all datasets folders in the `./Data` folder, which I have set already, is highly recommended and efficient. For each dataset, check the last line of the script (which is a comment) and replace the <image_folder_path> with the real folder path. All commands could be concluded like:

    ```
    python <Dataset_Name>.py(no need to change) <image_folder_path>(should be changed to real folder path) <prompt_folder_path>(no need to change)
    ```

    ```shell
    $ python AADB.py Data/AADB Raw/AADB # For AADB Datasets

    $ python ACI.py Data/ACI Raw/ACI # For ACI Datasets

    $ python Fauci_Meme.py Data/Fauci_Meme Raw/Fauci_Meme # For Fauci Meme Datasets

    $ python GAPED.py Data/GAPED Raw/GAPED # For GAPED Datasets

    $ python IAPS_Mikels.py Data/IAPS_Mikels Raw/IAPS_Mikels # For IAPS Mikels Datasets

    $ python IAPS.py Data/IAPS Raw/IAPS # For IAPS Datasets

    $ python Media_Bias_Politician_Attitudes.py Data/Media_Bias_Politician_Attitudes Raw/Media_Bias_Politician_Attitudes # For Politician Attitudes in Media Bias Datasets

    $ python Media_Bias_Politician_Traits.py Data/Media_Bias_Politician_Traits Raw/Media_Bias_Politician_Traits # For Politician Traits in Media Bias Datasets

    $ python NAPSBE.py Data/NAPSBE Raw/NAPSBE # For NAPSBE Datasets

    $ python UCLA_Protest_Attributes.py Data/UCLA_Protest_Attributes Raw/UCLA_Protest_Attributes # For Protest Attributes in UCLA Datasets

    $ python UCLA_Protest_Occurence.py Data/UCLA_Protest_Occurence Raw/UCLA_Protest_Occurence # For Protest Occurence in UCLA Datasets
    ```
    **All we need to do is to replace the `<Data/Dataset_Name>` with the `<real folder path for the dataset>`, and run the script in terminal.**






