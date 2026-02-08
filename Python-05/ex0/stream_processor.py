from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataProcessor(ABC):
    
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        data_len: int = len(data)
        total: float = sum(data)
        avg: float = total / data_len

        result: str = f"Processed {data_len} numeric values, sum={total}, avg={avg}"
        return result

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list) or not data:
            return False
        for i in data:
            if type(i) != int and type(i) != float:
                return False
        return True


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:

        data_len: int = len(data)
        data_words: int = len(data.split())
        result: str = f"Processed text: {data_len} characters, {data_words} words"

        return result

    def validate(self, data: Any) -> bool:

        if not data or not isinstance(data, str):
            return False
        else:
            return True

class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:

        result: str = ""
        if data.startswith("ERROR"):
            result = "[ALERT] ERROR level detected: Connection timeout"
        elif data.startswith("INFO"):
            result = "[INFO] INFO level detected: System ready"
        elif data.startswith("SECCESS"):
            result = "[SUCCESS] Success operation: Connection started"
        return result

    def validate(self, data: Any) -> bool:
        if not data or not isinstance(data, str):
            return False
        if (not data.startswith("ERROR") and not data.startswith("INFO") and not data.startswith("SUCCESS")): 
            return False
        return True


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")

    number: NumericProcessor = NumericProcessor()                                                                                                                                                                                                                                                                                                                                                                            
    nbr_data: List[int] = [1, 2, 3, 4, 5]

    print(f"Processing data: {nbr_data}")
    if number.validate(nbr_data):
        print("Validation: Numeric data verified")
        print(f"{number.format_output(number.process(nbr_data))}")
    else:
        print(f"ERROR: Data '{nbr_data}' is invalid")

    print("\nInitializing Text Processor...")
    
    text: TextProcessor = TextProcessor()
    txt_data: str = "Hello Nexus World"

    print(f'Processing data: "{txt_data}"')

    if text.validate(txt_data):
        print("Validation: Text data verified")
        print(f"{text.format_output(text.process(txt_data))}")

    else:
        print(f"ERROR: Data '{txt_data}' is invalid")

    print("\nInitializing Log Processor...")
    log: LogProcessor = LogProcessor()

    log_data: str = "ERROR: Connection timeout"

    print(f'Processing data: "{log_data}"')

    if log.validate(log_data):
        print("Validation: Log entry verified")
        print(f"{log.format_output(log.process(log_data))}")
    else:
        print(f"ERROR: Data '{log_data}' is invalid")

    print("\n=== Polymorphic Processing Demo ===")

    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [NumericProcessor(), TextProcessor(), LogProcessor()]
    inputs: List[Union[List[int], str]] = [[1, 2, 3], "Hello Nexus", "INFO: System ready"]

    for i in range(len(processors)):
        process: DataProcessor = processors[i]
        input: Union[List[int], str] = inputs[i]

        try:
            if process.validate(input):
                print(f"Result {i+1}: {process.process(input)}")
            else:
                print(f"Result {i+1}: ERROR (Invalid Data)")
        except Exception as e:
            print(f"Result {i+1}: Failed due to an unexpected error: {e}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()

