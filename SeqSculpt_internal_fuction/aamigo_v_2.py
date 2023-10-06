AA_MASS_DICT = dict({'A': 89, 'R': 174, 'N': 132, 'D': 133, 'C': 121, 'Q': 146, 'E': 147, 'Z': 147,
                            'G': 75, 'H': 155, 'I': 131, 'L': 131, 'K': 146, 'M': 149, 'F': 165, 'P': 115, 'S': 105,
                            'T': 119, 'W': 204, 'Y': 181, 'V': 117})

AA_BIOCHEMISTRY = dict(
        {'hydrophobic': ['G', 'A', 'V', 'L', 'I', 'P', 'F', 'M', 'W'], 'polar': ['S', 'T', 'C', 'N', 'Q', 'Y'],
         '- charged': ['E', 'D'], '+ charged': ['K', 'H', 'R']})

PROFILE = dict({'hydrophobic': 0.0, 'polar': 0.0, '- charged': 0.0, '+ charged': 0.0})

ESSENTIAL_AMINO_ACIDS = ['H', 'I', 'K', 'L', 'M', 'F', 'T', 'W', 'V', 'h', 'i', 'k', 'l', 'm', 'f', 't', 'w', 'v']


def calculate_protein_mass(seq: str) -> float:
    """

    Calculate the mass (Da) of a protein based on its amino acids sequence.
    Takes a string of amino acids, returns the molecular weight in Da.
    Amino acids in the string should be indicated as one-letter symbols.

    """
    aa_seq = list(seq.upper())
   
    mass = 0
    for amino_acid in aa_seq:
        mass += AA_MASS_DICT[amino_acid]
    return mass


def profile_amino_acid(seq: str):
    """

     Return the proportion of hydrophobic, polar, negatively and positively charged amino acids in the protein.
     Takes a string of amino acids, returns a dictionary.
     Amino acids in the string should be indicated as one-letter symbols.

    """
    aa_seq = list(seq.upper())
   
    for amino_acid in aa_seq:
        for group_name, group_list in AA_BIOCHEMISTRY.items():
            if amino_acid in group_list:
                PROFILE[group_name] += 1

    for group, count in PROFILE.items():
        PROFILE[group] = round((count/len(seq)), 2)
    return PROFILE


def find_amino_acid(seq: str):
    """

    Searches for a substring of amino acids in the entire amino acid sequence.
    Takes a strings of amino acids and a substring, which should be found.
    Returns the position where the searched one was found for the first time.
    Amino acids in the string should be indicated as one-letter symbols.

    """
    aa_seq = list(seq)
    aa_seq_upper = []
    for sequences in aa_seq:
        upper_case = sequences.upper()
        aa_seq_upper.append(upper_case)
    amino_acids = aa_seq_upper[:-1]
    substring = aa_seq_upper[-1]
    results = []
    for sequences in amino_acids:
        subst = sequences.find(substring)
        results.append(subst)
    return results


def count_pattern_in_seqs(seqs: list[str], pattern: str) -> list[int]: 
    """

    Finds how many times a particular sequence(s) occurs in the original one.
    Takes a string of amino acids and a substring, which should be counted.
    Returns the count of searched amino acids.
    Amino acids in the string should be indicated as one-letter symbols.

    """
    aa_seq = list(seq)
    aa_seq_upper = []
    for sequences in aa_seq:
        upper_case = sequences.upper()
        aa_seq_upper.append(upper_case)
    amino_acids = aa_seq_upper[:-1]
    substring = aa_seq_upper[-1]
    results = []
    for sequences in amino_acids:
        aa_count = sequences.count(substring)
        results.append(aa_count)
    return results


def protein_length(*seq: str):
    """

    Calculates the length (number of amino acids) of a protein.
    Takes a string of amino acids, returns the number.
    Amino acids in the string should be indicated as one-letter symbols.

    """
    lengths = []
    for sequences in seq:
        lengths.append(len(sequences))
    return lengths


def count_essential_amino_acids(*seq: str):
    """

    Return list of essential amino acids in protein sequence.
    Takes a string of amino acids, returns only the essential amino acids.
    Amino acids in the string should be indicated as one-letter symbols.

    """
    eaa_list = []

    for sequences in seq:
        eaa_seq = []
        for amino_acid in sequences:
            if amino_acid in ESSENTIAL_AMINO_ACIDS:
                eaa_seq.append(amino_acid)
        eaa_list.append(eaa_seq)

    return eaa_list


def run_aa_tools(*args):
    """

    Main function for amino acid sequences processing.
    Parameters: *args (str) - amino acid sequences and operation.
    Returns: List of results or None if non-amino acid chars found.

    """
    seq = args[:-1]
    operation = args[-1]
    non_aa_chars = set('BJOUXbjoux')
    contains_non_aa = False

    for sequence in seq:
        contains_non_aa = False
        for amino_acid in sequence:
            if amino_acid in non_aa_chars:
                contains_non_aa = True
                break
        if contains_non_aa:
            break
    if contains_non_aa:
        return None

    results = []

    for sequence in seq:
        if operation == "calculate_protein_mass":
            result = calculate_protein_mass(sequence)
            results.append(result)

        if operation == "profile_amino_acid":
            result = profile_amino_acid(sequence)
            results.append(result)

        if operation == "find_amino_acid":
            result = find_amino_acid(seq)
            return result

        if operation == "count_pattern_in_seqs":
            result = count_pattern_in_seqs(seq)
            return result

        if operation == "protein_length":
            result = protein_length(sequence)
            results.append(result)

        if operation == "count_essential_amino_acids":
            result = count_essential_amino_acids(sequence)
            results.append(result)
    return results