# AAmigo
This readme describes the user-friendly program AAmigo for performing various operations with amino acid sequences.

AAmigo can perform different operations:
* Calculate the mass of a protein.
* Calculate the ratio of amino acids with different polarities in a protein
* Find for a particular amino acid(s) in the entire sequence
* Calculate amino acid's occurrence in a sequence
* Calculate amino acid sequence(s) length
* Finds essential amino acids (in humans) in a sequence(s)

## Usage
1. Clone this repo using SSH or HTTPS:
```bash
git clone git@github.com:uzunmasha/HW4_Functions2.git
``` 
**or**
```bash
git clone https://github.com/uzunmasha/HW4_Functions2.git
``` 
2. Launch the program with the required function (listed below) in a code interpreter like Jupyter Notebook.
3. Enjoy your results!

## List of functions:
For all functions, amino acids in the sequences should be indicated as one-letter symbols. Letters can be uppercase or lowercase.

### protein_mass
This function calculates the mass (Da) of a protein based on its amino acid sequence. As input, it takes a string of amino acids and returns the molecular weight in Da.
Usage example:
```python
aa_tools('MARY', 'protein_mass') #593 (in Da)
```
### amino_acid_profile
This function displays the proportion of hydrophobic, polar, negatively, and positively charged amino acids in the protein. It takes a string of amino acids, and returns a dictionary with the result.
Usage example:
```python
aa_tools('EEKFG', 'amino_acid_profile') #{'hydrophobic': 0.4, 'polar': 0.0, '- charged': 0.4, '+ charged': 0.2}
```
### amino_acid_substring 
This function searches for the presence of particular amino acid(s) in the entire amino acid sequence. As input, it takes a string of amino acids and a substring that needs to be found. All sequences and subsequence should be comma-separated. Any number of amino acid sequences is possible. The searched substring should be one and it should be pointed last.  As an output, the function returns the position in the original sequence where the searched element was found for the first time.
Usage example:
```python
aa_tools('RNwDeACEQEZ', 'E','amino_acid_substring') #4
aa_tools('RNwDeACEQEZ', 'DFKAaaE','A','amino_acid_substring') #[5, 3]
```
### amino_acid_count
This function finds how many times a particular amino acid or sequence of several amino acids occurs in the original sequence. As input, it takes a string of amino acids and a substring that needs to be counted. All sequences and subsequence should be comma-separated. Any number of amino acid sequences is possible. The searched substring should be one and it should be pointed last. As an output, the function returns the count of searched amino acid(s).
Usage example:
```python
aa_tools('GHcLfKF','f','amino_acid_count') #2
aa_tools('HILAKMaF', 'GDaKFAAE','A','amino_acid_count') #[2, 3]
```
### protein_length
This function can analyze an aminoacid sequence and gives a length of it (number of amino acids). Any number of amino acid sequences is possible. All sequences should be comma-separated. As input, it takes a string or strings of amino acids, as an output, the function returns the length of each protein.
Usage example:
```python
aa_tools('KKNNfF', 'KKFFRRVV', 'KK', 'protein_length') #[6, 8, 2]
```
### essential_amino_acids
This function can analyze an amino acid sequence and gives a list of essential amino acids (in humans) that are present in the sequence.
Any number of amino acid sequences is possible. All sequences should be comma-separated. As input, it takes a string or strings of amino acids, as an output, the function returns essential amino acids for each sequence.
Usage example:
```python
aa_tools('KKNNfF', 'KKFFRRVV', 'KK', 'essential_amino_acids') #[['K', 'K', 'f', 'F'], ['K', 'K', 'F', 'F', 'V', 'V'], ['K', 'K']]
```

## Troubleshooting
* In function `'amino_acid_substring'` the position counting starts at 0, so don't be confused if the second element in the sequence has the output [1]. 
* In functions `'amino_acid_substring'` and `'amino_acid_count'` output [-1] means that there is no such element in the sequence.
* In functions `'amino_acid_substring'` and `'amino_acid_count'` the error message "name '..' is not defined" means that the given argument is not quoted in the input string.

## Bibliography
[1] Wu G. Amino acids: metabolism, functions, and nutrition. Amino Acids. 2009 May;37(1):1-17. doi: 10.1007/s00726-009-0269-0.

## Developers and contacts
* Maria Uzun - contributed to `'amino_acid_substring'`, `'amino_acid_count'`, and `'aa_tools'` functions.
* Maria Babaeva - contributed to `'protein_mass'` and `'amino_acid_profile'` functions.
* Kristina Zhur - contributed to `'protein_length'` and `'essential_amino_acids'` functions.
* Julia the Cat - team's emotional support.


![photo_2023-09-26_18-33-49_3](https://github.com/uzunmasha/HW4_Functions2/assets/44806106/63fdea24-5c0a-4650-8bed-181871aa540f)


In case of non-working code:

* Please blame the one who has the paws
* Report any problems directly to the GitHub issue tracker

or

* Send your feedback to uzunmasha@gmail.com
