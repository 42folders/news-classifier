"""
Text preprocessing script for Huffington Post news dataset.
Contains functions to clean and format training, validation and test datasets
"""
import os
import pandas as pd

# CONFIG
# root = r"/content" # For Google colab notebook
ROOT = r"/Users/cathytay/60-69-Code/61.06-TextClassification/data" #r"/data" # For github (else change to point to local path)
USECOLS = ['headline', 'short_description', 'category']
CAT_COL = 'category'
TXT_COL = 'text'

# FILENAMES
TRAIN_RAW = "train"
VAL_RAW = "val"
TEST_RAW = "test"

TRAIN_PROC = TRAIN_RAW + '_proc'
VAL_PROC = VAL_RAW + '_proc'
TEST_PROC = TEST_RAW + '_proc'

# LABELS
CATEGORIES = ['PARENTING', 'POLITICS', 'ENTERTAINMENT', 'WELLNESS', 'BUSINESS', 'TRAVEL',
              'FOOD & DRINK', 'QUEER VOICES', 'STYLE & BEAUTY', 'HEALTHY LIVING', 'SPORTS', 'COMEDY']

NUM_LABELS = len(CATEGORIES)

# FUNCTIONS
def process(file, cols, output_file):
    """Ingest a raw csv file; 
    exports dataframe with processed 'text' and 'label' columns to csv
    """
    # Load a dataset (train/val/test) and input columns
    df = pd.read_csv(os.path.join(ROOT, file + r'.csv'), usecols=cols, encoding='utf-8')
   
    # Keep only target categories 
    df = df.loc[df[CAT_COL].isin(CATEGORIES)]
    # Concatenate headline and short description into 'text' column
    df.loc[:, TXT_COL] = df['headline'] + ' ' + df['short_description']
    df = df[[TXT_COL, CAT_COL]]
    df.rename(columns={CAT_COL:'label'}, inplace=True)
    df = df.loc[df[TXT_COL].isna()!=True]

    output_path = os.path.join(ROOT, output_file + r'.csv')
    df.to_csv(output_path, index=False)
    print(f"Exported {output_path}.")

# TODO Is it necessary to remove emojis from input texts?
# U_CHARS = ['\u201c', '\u201d', '\u2019']
# def clean_char(df):
#     # Remove entries with emojis or emoticons (encode and decode)
#     df.loc[:, TXT_COL] = df[TXT_COL].apply(lambda x: x.encode('unicode-escape').decode('utf-8')) #'ASCII'
#     df = df.loc[~df[TXT_COL].str.contains(r'\\U00\S+', regex=True)]
#     # Check if any \u201c \u201d \u2019
#     quo = df.loc[df['text'].str.contains(r'\\u\S+', regex=True)]
#     if len(quo) > 0:
#         print(f"Lines containing unparsed left and right quote chars: {len(quo)}")

#     return df

def run():
    process(TRAIN_RAW, USECOLS, TRAIN_PROC)
    process(VAL_RAW, USECOLS, VAL_PROC)
    process(TEST_RAW, USECOLS, TEST_PROC)

if __name__ == "__main__":
    run()