import pandas as pd

# def readMentions(pathFile = r".\Game and mentions_Validated.xlsx"):
#     mentionsDF = pd.read_excel(rf'{pathFile}')
import os
import pandas as pd

def readMentions(pathFile="Game and mentions_Validated.xlsx"):
    # Construct the full path
    full_path = os.path.join(os.getcwd(), pathFile)
    print(f"Reading file from: {full_path}")  # For debugging, to see the full path

    # Read the Excel file
    mentionsDF = pd.read_excel(full_path)




    print(mentionsDF)
    targetGameNames = list(mentionsDF['Game name'])
    print(targetGameNames)
    return mentionsDF, targetGameNames



