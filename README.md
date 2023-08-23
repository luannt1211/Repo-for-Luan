# Repo-for-Luan
Just another repo

This repository houses the Python files prepared to conduct simple text analysis for the JICA Shikoku project.
This project include several different stages of analysis, including:
1. EDA
2. Text Analysis
3. Presentation of Result to JICA counterpart


This repository includes only the necessary Python files for the Text Analysis portion of the Analysis work.
The files include:
- word_frequency_analysis Jupyter Notebook
- text_analysis .py
- Python-try .csv (original file delivered by JICA for analysis)

**1. Word_Frequency_Analysis**
The notebook include the setup and preparation for the analysis of the text found in 'Python-try.csv'.
These steps include (1) cleaning of raw data (drop NaN, transform data), (2) breaking data into sub-category for further analysis in Excel (e.g. separate into multiple files by project type), (3) writing functions to extract tokens in columns of varchar data for word-cloud visualization, and text frequency analysis

**2. Text_analysis.py**
This is the .py file that includes a list of words in Japanese that doesn't carry meaning.
By removing these from the text, I can form Word Cloud visualization as well as conduct meaningful analysis with the file 1. above.

**3. tokens_df**
Example output file for words and their frequency of appearance in the original .csv file given by JICA

**4. Python-try.csv**
Original file given by JICA

**5. NotoSansCJjp-Light.otf**
Necessary for MeCab to work to analyze Japanese-language data
