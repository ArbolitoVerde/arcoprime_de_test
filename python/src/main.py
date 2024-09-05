from sequence_gen import SequenceGen

FILE_PATH = './python/data/sequence_dna'
SUB_SEQUENCE = 'TGCCAG'

def statistics_gen_sequence():
    sequence = SequenceGen.sequence_from_file(FILE_PATH)

    sequence_len = sequence.sequence_length()
    print(f"The sequence length has {sequence_len} nucleotides \n")

    nucleotido_count = sequence.nucleotido_counter()
    print(f"The sequence has the following resume by nucleotide {nucleotido_count} \n")

    sub_sequence_count = sequence.sub_sequence_counter(SUB_SEQUENCE)
    print(f"The sequence contains the subsequence {SUB_SEQUENCE} {sub_sequence_count} times\n")

if __name__ == "__main__":
    statistics_gen_sequence()