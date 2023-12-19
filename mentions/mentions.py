import pandas as pd

# def readMentions(pathFile = r".\Game and mentions_Validated.xlsx"):
#     mentionsDF = pd.read_excel(rf'{pathFile}')
import os
import pandas as pd

def readMentions(pathFile="Game and mentions_Validated.xlsx"):
    # Construct the full path
    full_path = os.path.join(os.getcwd(), pathFile)

    # Read the Excel file
    mentionsDF = pd.read_excel(full_path)
    targetGameNames = list(mentionsDF['Game name'])
    return mentionsDF, targetGameNames



