# BigLittlePairing
An application of the Gale-Shapley algorithm to pair bigs and littles for clubs

## Installation
Run `pip install openpyxl` in your terminal. The `openpyxl` package facilitates the reading and writing of Excel spreadsheets.

## How to use
Ensure you ran `pip install openpyxl` in your terminal.

Download sm.py and paths.txt.

If you are using responses from a Google Form, download the responses .csv file from your Google Form. Make sure the format of your .csv should resemble that of the example bigs.csv or littles.csv. The values of the first row and first column do not matter as long as they are filled with non-important values (empty values are fine). You can have as many bigs and as many littles as you want. Each big and each little can have as many preferences as you want. Make sure these .csv files are in the same directory as the sm.py and paths.txt.

Open paths.txt. Replace the current values of bigs-pref-file and littles-pref-file with the names of your .csv files.

Open command prompt. Navigate to the directory containing all four files.

Run `python sm.py`

A pairs.xlsx with all the pairs will be created in that same directory. Any name with a star next to it suggests it is a duplicate name due to the different number of bigs and littles. Starred people have multiple bigs/littles.
