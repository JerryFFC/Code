import json
from pprint import pprint
import pandas as pd

# def readJSON(path = r'.\FourthFloorCreativeJSON.json'):
#     with open(rf'{path}') as filePath:
import os

def readJSON(path='FourthFloorCreativeJSON.json'):
    # Ensure the path is correct
    full_path = os.path.join(os.getcwd(), path)
    print(f"Trying to read file at: {full_path}")  # This line is for debugging purposes

    with open(full_path, 'r') as filePath:
        # Your code to read and process the file

        d = json.load(filePath)
    return d


def transcriptFromJSON(json = readJSON()):
    result = list(json.values())
    transcript = result
    transcript = "".join(transcript)
    return transcript

import pandas as pd

def extract_context(transcript, target_phrase, num_words=5):
    """
    Extracts the context around a target phrase from a transcript.

    Args:
    transcript (str): The transcript text.
    target_phrase (str): The target phrase to search for.
    num_words (int): Number of words to extract before and after the target phrase.

    Returns:
    DataFrame: A DataFrame with preceding words, target phrase, and following words.
    """

    # Split the transcript and target phrase into words
    words = transcript.split()
    target_words = target_phrase.split()

    # Find all occurrences of the target phrase
    occurrences = []
    for i in range(len(words) - len(target_words) + 1):
        if words[i:i + len(target_words)] == target_words:
            occurrences.append(i)

    # Extract the context for each occurrence
    context_data = []
    for index in occurrences:
        start = max(0, index - num_words)
        end = min(len(words), index + len(target_words) + num_words)

        # Extract preceding and following words
        preceding_words = words[start:index]
        following_words = words[index + len(target_words):end]

        # Adjust the lists to have exactly num_words elements
        preceding_words = ([''] * (num_words - len(preceding_words))) + preceding_words
        following_words = following_words + ([''] * (num_words - len(following_words)))

        context_data.append([' '.join(preceding_words), target_phrase, ' '.join(following_words)])

    # Create a DataFrame
    df = pd.DataFrame(context_data, columns=[f'{num_words} Preceding', 'Target Phrase', f'{num_words} Following'])

    return df




# df = extract_context(transcriptFromJSON(), 'lethal company', num_words=5)
# print(df)