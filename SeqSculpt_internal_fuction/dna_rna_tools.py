COMPLEMENT_DICT = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'U': 'A','a': 't', 't': 'a', 'c': 'g', 'g': 'c', 'u': 'a' }


def transcribe(sequence):
    sequence = sequence.replace('T', 'U').replace('t', 'u')
    return sequence
    """

    Makes an RNA copy of a gene's DNA sequence.

    """

def reverse(sequence):
    return sequence[::-1]
    """

    Converts a DNA sequence into its reverse.

    """

def complement(sequence):
    """

    Converts a DNA sequence into its complement.

    """
    complemented_sequence = ''
    for base in sequence:
        complemented_base = COMPLEMENT_DICT[base]
        complemented_sequence += complemented_base
    return complemented_sequence
	
    
def reverse_complement(sequence):
    """

    Converts a DNA sequence into its reverse-complement counterpart.

    """
    return reverse(complement(sequence))
	

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

def main():
    sequence = input("Enter DNA or RNA sequence: ")
    procedure = input("Enter the name of the procedure (transcribe, reverse, complement, reverse_complement): ")
    result = run_dna_rna_tools(sequence, procedure)
    print("Result:", result)

if __name__ == "__main__":
    main()