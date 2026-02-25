from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.stream_type: str = "Generic Stream"

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [
            data
            for data in data_batch
            if isinstance(data, str) and criteria in data
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "id": self.stream_id,
            "type": self.stream_type
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        temps: List[float] = [
            float(entry.split(":")[1])
            for entry in data_batch
            if isinstance(entry, str) and entry.startswith("temp:")
        ]
        avg: float = sum(temps) / len(temps) if temps else 0.0

        return (
            f"Sensor analysis: {len(data_batch)} readings processed, "
            f"avg temp: {avg}°C"
        )


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        data_len: int = len(data_batch)
        res: int = 0

        buys: List[int] = [
            int(entry.split(":")[1])
            for entry in data_batch
            if isinstance(entry, str) and entry.startswith("buy:")
        ]

        sells: List[int] = [
            int(entry.split(":")[1])
            for entry in data_batch
            if isinstance(entry, str) and entry.startswith("sell:")
        ]

        res: int = sum(buys) - sum(sells)

        sign: str = "+" if res >= 0 else ""
        return (
            "Transaction analysis: "
            f"{data_len} operations, net flow: {sign}{res} units"
        )


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        data_len: int = len(data_batch)

        errors: int = len([entry for entry in data_batch if entry == "error"])

        return f"Event analysis: {data_len} events, {errors} error detected"


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_streams(self, data_batches: List[List[Any]]) -> None:
        stream_types: List[str] = ["Sensor", "Transaction", "Event"]
        for i in range(len(self.streams)):
            current_stream: DataStream = self.streams[i]

            if i >= len(data_batches):
                break

            current_data: List[Any] = data_batches[i]
            try:
                stream_name: str = (
                    stream_types[i] if i < len(stream_types) else "Unknown"
                )
                if stream_name == 'Sensor':
                    unit = 'readings'
                elif stream_name == 'Transaction':
                    unit = 'operations'
                else:
                    unit = 'events'
                print(f"- {stream_name} data: {len(current_data)} "
                      f"{unit} processed")
            except Exception as e:
                print(f"Stream {current_stream.stream_id} failed: {e}")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    sensor: SensorStream = SensorStream("SENSOR_001")
    stats: Dict[str, Union[str, int, float]] = sensor.get_stats()
    print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
    sensor_data: List[str] = ["temp:22.5", "humidity:65", "pressure:1013"]
    print("Processing sensor batch: "
          "[temp:22.5, humidity:65, pressure:1013]")
    print(sensor.process_batch(sensor_data))

    print("\nInitializing Transaction Stream...")
    trans: TransactionStream = TransactionStream("TRANS_001")
    stats = trans.get_stats()
    print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
    trans_data: List[str] = ["buy:100", "sell:150", "buy:75"]
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(trans.process_batch(trans_data))

    print("\nInitializing Event Stream...")
    event: EventStream = EventStream("EVENT_001")
    stats = event.get_stats()
    print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
    event_data: List[str] = ["login", "error", "logout"]
    print("Processing event batch: [login, error, logout]")
    print(event.process_batch(event_data))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor: StreamProcessor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    new_sensor_data: List[str] = ["temp:20.0", "temp:21.5"]
    new_trans_data: List[str] = ["buy:50", "sell:30", "sell:20", "sell:10"]
    new_event_data: List[str] = ["start", "warning", "stop"]

    data_bratches: List[List[str]] = [
        new_sensor_data, new_trans_data, new_event_data
    ]

    print("\nBatch 1 Results:")
    processor.process_streams(data_bratches)

    print("\nStream filtering active: High-priority data only")

    filtered_sensor = sensor.filter_data(new_sensor_data, "temp")

    filtered_trans = trans.filter_data(new_trans_data, "buy")

    print(
        f"Filtered results: {len(filtered_sensor)} critical sensor alerts, "
        f"{len(filtered_trans)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
