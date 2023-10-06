import SeqSculpt_internal_fuction.aamigo_v_2
import SeqSculpt_internal_fuction.dna_rna_tools

AA_MASS_DICT = {'A': 89, 'R': 174, 'N': 132, 'D': 133, 'C': 121, 'Q': 146, 'E': 147, 'Z': 147,
                            'G': 75, 'H': 155, 'I': 131, 'L': 131, 'K': 146, 'M': 149, 'F': 165, 'P': 115, 'S': 105,
                            'T': 119, 'W': 204, 'Y': 181, 'V': 117}

AA_BIOCHEMISTRY = {'hydrophobic': ['G', 'A', 'V', 'L', 'I', 'P', 'F', 'M', 'W'], 'polar': ['S', 'T', 'C', 'N', 'Q', 'Y'],
         '- charged': ['E', 'D'], '+ charged': ['K', 'H', 'R']}

PROFILE = {'hydrophobic': 0.0, 'polar': 0.0, '- charged': 0.0, '+ charged': 0.0}

ESSENTIAL_AMINO_ACIDS = ['H', 'I', 'K', 'L', 'M', 'F', 'T', 'W', 'V', 'h', 'i', 'k', 'l', 'm', 'f', 't', 'w', 'v']

COMPLEMENT_DICT = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'U': 'A','a': 't', 't': 'a', 'c': 'g', 'g': 'c', 'u': 'a' }


def filter_fastq(seqs, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0):
    """

    Herforms filtration based on a specified GC composition interval (in percent), 
    sequence length and average read quality threshold for filtering.

    """
    filtered_seqs = {}
    
    gc_lower_bound, gc_upper_bound = gc_bounds
    length_lower_bound, length_upper_bound = length_bounds
    
    for seq_name, (sequence, quality) in seqs.items():
        gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
        seq_quality = 0
        for char in quality:
            char_quality = ord(char) - 33
            seq_quality += char_quality
        mean_quality = seq_quality / len(quality)

        if (
            gc_lower_bound <= gc_content <= gc_upper_bound and
            length_lower_bound <= len(sequence) <= length_upper_bound and
            mean_quality >= quality_threshold
        ):
            filtered_seqs[seq_name] = (sequence, quality)
    
    return filtered_seqs


def run_dna_rna_tools(sequence, procedure):
    """

    Main function for dna sequences processing.
    Parameters: sequence (str) - dna sequences and procedure.
    
    """
    procedures = {
        "transcribe": transcribe,
        "reverse": reverse,
        "complement": complement,
        "reverse_complement": reverse_complement
	}

    if 'T' in sequence.upper() and 'U' in sequence.upper():
        raise ValueError('Please, enter RNA or DNA')
    
    if procedure not in procedures:
        return "Error. Available procedures: transcribe, reverse, complement, reverse_complement."
    result = procedures[procedure](sequence)
    return result


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
