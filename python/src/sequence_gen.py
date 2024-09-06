import time

class SequenceGen:

    NUCLEOTIDOS = ['a', 'c', 'g', 't']

    def __init__(self, sequence: str) -> None:
        self.sequence = sequence.replace("\n","").lower()

    @classmethod
    def sequence_from_file(cls, file_path: str):
        with open(file_path) as f:
            sequence = f.read()
            return cls(sequence.replace("\n","").lower())
        
    def measure_execution_time(func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print(f"Execution time for function {func.__name__} is {execution_time:.4f} seconds")
            return result
        return wrapper

    @measure_execution_time 
    def sequence_length(self) -> int:
        return len(self.sequence)
    
    @measure_execution_time
    def nucleotido_counter(self) -> list:
        return [(n, self.sequence.count(n)) for n in self.NUCLEOTIDOS]
    
    @measure_execution_time
    def sub_sequence_counter(self, sub_sequence: str) -> int:
        sub_sequence = sub_sequence.lower()
        start_index = 0
        end_index = len(sub_sequence)
        count = 0

        while end_index <= len(self.sequence):
            if sub_sequence.lower() == self.sequence[start_index:end_index]:
                count += 1
                start_index += 1
                end_index += 1
            else:
                start_index += 1
                end_index += 1

        return count
