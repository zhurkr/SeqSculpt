This readme describes the user-friendly program SeqSculpt for performing various operations with DNA, RNA or amino acid sequences.


## Usage
1. Clone this repo using SSH or HTTPS:
```bash
git clone git@github.com:zhurkr/SeqSculpt.git
``` 
**or**
```bash
git clone https://github.com/zhurkr/SeqSculpt.git
``` 
2. Launch the program with the required function (listed below) in a code interpreter like Jupyter Notebook.
3. Enjoy your results!


Import??

Internal function

# fastq_processing
fastq_processing performs filtration based on a specified GC composition interval (in percent), 
sequence length and average read quality threshold for filtering.

Input: seqs - a dictionary consisting of fastq sequences. The structure is as follow: key - string, sequence name,
the value is a tuple of two strings: sequence and quality.
Output:function returns a similar dictionary consisting only of those sequences that pass all the filtration conditions.

Usage example:
```python
seqs = {
    '@SRX079804:1:SRR292678:1:1101:21885:21885': ('ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA', 'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD'),
    '@SRX079804:1:SRR292678:1:1101:24563:24563': ('ATTAGCGAGGAGGAGTGCTGAGAAGATGTCGCCTACGCCGTTGAAATTCCCTTCAATCAGGGGGTACTGGAGGATACGAGTTTGTGTG', 'BFFFFFFFB@B@A<@D>BDDACDDDEBEDEFFFBFFFEFFDFFF=CC@DDFD8FFFFFFF8/+.2,@7<<:?B/:<><-><@.A*C>D'),
    '@SRX079804:1:SRR292678:1:1101:30161:30161': ('GAACGACAGCAGCTCCTGCATAACCGCGTCCTTCTTCTTTAGCGTTGTGCAAAGCATGTTTTGTATTACGGGCATCTCGAGCGAATC', 'DFFFEGDGGGGFGGEDCCDCEFFFFCCCCCB>CEBFGFBGGG?DE=:6@=>A<A>D?D8DCEE:>EEABE5D@5:DDCA;EEE-DCD'),
    '@SRX079804:1:SRR292678:1:1101:47176:47176': ('TGAAGCGTCGATAGAAGTTAGCAAACCCGCGGAACTTCCGTACATCAGACACATTCCGGGGGGTGGGCCAATCCATGATGCCTTTG', 'FF@FFBEEEEFFEFFD@EDEFFB=DFEEFFFE8FFE8EEDBFDFEEBE+E<C<C@FFFFF;;338<??D:@=DD:8DDDD@EE?EB')
   }

fastq_processing.filter_fastq(seqs, gc_bounds=(20, 80), length_bounds=(10, 500), quality_threshold=35)

#{'@SRX079804:1:SRR292678:1:1101:21885:21885': ('ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA',
  'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD')}
```
# run_dna_rna_tools
The `run_dna_rna_tools` function takes as input DNA or RNA sequences (*str*), as well as the name of the procedure to be performed. After this, the command performs the specified action.

## List of functions:
dna_rna_tools can perform different operations:
* transcribe — print the transcribed sequence
* reverse — print the reversed sequence
* complement — print the complementary sequence
* reverse_complement — print the reverse complementary sequence

Usage example:
```python
run_dna_rna_tools('ATG', 'transcribe') # 'AUG'
run_dna_rna_tools('ATG', 'reverse') # 'GTA'
run_dna_rna_tools('AtG', 'complement') # 'TaC'
run_dna_rna_tools('ATg', 'reverse_complement') # 'cAT'
```

# aamigo_v.1
For all functions of aamigo_v.1 amino acids in the sequences should be indicated as one-letter symbols. Letters can be uppercase or lowercase.

## List of functions:
aamigo_v.1 can perform different operations:
* Calculate the mass of a protein.
* Calculate the ratio of amino acids with different polarities in a protein
* Find for a particular amino acid(s) in the entire sequence
* Calculate amino acid's occurrence in a sequence
* Calculate amino acid sequence(s) length
* Finds essential amino acids (in humans) in a sequence(s)


### calculate_protein_mass
This function calculates the mass (Da) of a protein based on its amino acid sequence. As input, it takes a string of amino acids and returns the molecular weight in Da.

Usage example:
```python
aa_tools('MARY', 'calculate_protein_mass') #593 (in Da)
```
### profile_amino_acid
This function displays the proportion of hydrophobic, polar, negatively, and positively charged amino acids in the protein. It takes a string of amino acids, and returns a dictionary with the result.

Usage example:
```python
aa_tools('EEKFG', 'profile_amino_acid') #{'hydrophobic': 0.4, 'polar': 0.0, '- charged': 0.4, '+ charged': 0.2}
```
### find_amino_acid 
This function searches for the presence of particular amino acid(s) in the entire amino acid sequence. As input, it takes a string of amino acids and a substring that needs to be found. All sequences and subsequence should be comma-separated. Any number of amino acid sequences is possible. The searched substring should be one and it should be pointed last.  As an output, the function returns the position in the original sequence where the searched element was found for the first time.

Usage example:
```python
aa_tools('RNwDeACEQEZ', 'E','find_amino_acid') #4
aa_tools('RNwDeACEQEZ', 'DFKAaaE','A','find_amino_acid') #[5, 3]
```
### count_pattern_in_seqs
This function finds how many times a particular amino acid or sequence of several amino acids occurs in the original sequence. As input, it takes a string of amino acids and a substring that needs to be counted. All sequences and subsequence should be comma-separated. Any number of amino acid sequences is possible. The searched substring should be one and it should be pointed last. As an output, the function returns the count of searched amino acid(s).

Usage example:
```python
aa_tools('GHcLfKF','f','count_pattern_in_seqs') #2
aa_tools('HILAKMaF', 'GDaKFAAE','A','count_pattern_in_seqs') #[2, 3]
```
### protein_length
This function can analyze an aminoacid sequence and gives a length of it (number of amino acids). Any number of amino acid sequences is possible. All sequences should be comma-separated. As input, it takes a string or strings of amino acids, as an output, the function returns the length of each protein.

Usage example:
```python
aa_tools('KKNNfF', 'KKFFRRVV', 'KK', 'protein_length') #[6, 8, 2]
```
### count_essential_amino_acids
This function can analyze an amino acid sequence and gives a list of essential amino acids (in humans) that are present in the sequence.
Any number of amino acid sequences is possible. All sequences should be comma-separated. As input, it takes a string or strings of amino acids, as an output, the function returns essential amino acids for each sequence.

Usage example:
```python
aa_tools('KKNNfF', 'KKFFRRVV', 'KK', 'count_essential_amino_acids') #[['K', 'K', 'f', 'F'], ['K', 'K', 'F', 'F', 'V', 'V'], ['K', 'K']]
```

## Troubleshooting
* In function `'find_amino_acid'` the position counting starts at 0, so don't be confused if the second element in the sequence has the output [1]. 
* In functions `'find_amino_acid'` and `'count_pattern_in_seqs'` output [-1] means that there is no such element in the sequence.
* In functions `'find_amino_acid'` and `'count_pattern_in_seqs'` the error message "name '..' is not defined" means that the given argument is not quoted in the input string.

## Bibliography
[1] Wu G. Amino acids: metabolism, functions, and nutrition. Amino Acids. 2009 May;37(1):1-17. doi: 10.1007/s00726-009-0269-0.

## Developers and contacts
* Maria Uzun - contributed to `'amino_acid_substring'`, `'amino_acid_count'`, and `'aa_tools'` functions.
* Maria Babaeva - contributed to `'protein_mass'` and `'amino_acid_profile'` functions.
* Kristina Zhur - contributed to `'fastq_processing'`, `'protein_length'` and `'essential_amino_acids'` functions.


In case of non-working code:

* Please blame the one who has the paws
* Report any problems directly to the GitHub issue tracker

or

* Send your feedback to zhur.kv@gmail.com
