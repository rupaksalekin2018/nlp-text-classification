'''
Certainly! Below is the full 
code that you can run on your PC. 
This code reads the CSV file containing YouTube comments, 
applies sentiment labeling based on English, Bangla,
and Banglish keywords, and then saves the labeled data
to a new CSV file. Ensure you have the necessary libraries 
installed (like pandas) and update the
file path according to your file's location.
'''

import pandas as pd

def label_multilingual_comment_with_banglish(comment):
    # Handle non-string values
    if not isinstance(comment, str):
        return 2  # Neutral for missing or non-string comments

    # Converting comment to lower case for easier comparison
    comment_lower = comment.lower()

    # Checking for positive and negative keywords in the comment
    if any(word in comment_lower for word in positive_keywords_final):
        return 1  # Positive
    elif any(word in comment_lower for word in negative_keywords_final):
        return 0  # Negative
    else:
        return 2  # Neutral

# File path to your CSV file
file_path = 'path_to_your_file.csv'

# Load the dataset
comments_df = pd.read_csv(file_path)

# Updated lists of positive and negative keywords including English, Bangla, and Banglish
positive_keywords_final = [
    'best', 'thank', 'great', 'love', 'amazing', 'good',
    'সেরা', 'ধন্যবাদ', 'দুর্দান্ত', 'ভালোবাসা', 'অসাধারণ', 'ভালো',
    'sera', 'dhonnobad', 'durdanto', 'bhalobasha', 'osadharon', 'bhalo'
]

negative_keywords_final = [
    'worst', 'bad', 'hate', 'terrible', 'poor', 'problem',
    'সবচেয়ে খারাপ', 'খারাপ', 'ঘৃণা', 'ভয়ানক', 'দরিদ্র', 'সমস্যা',
    'sobcheye kharap', 'kharap', 'ghrina', 'bhoyanok', 'doridro', 'somossa'
]

# Apply the final labeling function to the 'Comment' column
comments_df['Label'] = comments_df['Comment'].apply(label_multilingual_comment_with_banglish)

# Path for the output file
output_file_path = 'path_to_output_file.csv'

# Save the updated dataframe to a new CSV file
comments_df.to_csv(output_file_path, index=False)

print(f"Labeled data saved to {output_file_path}")

'''
Remember to replace 'path_to_your_file.csv' with the 
path to your input CSV file and 'path_to_output_file.csv'
with the desired path for the output file. 
This script should work in any standard
 Python environment where pandas is available.
'''