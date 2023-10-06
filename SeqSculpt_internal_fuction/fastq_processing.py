def filter_fastq(seqs, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0):
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