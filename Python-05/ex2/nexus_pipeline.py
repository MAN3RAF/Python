from typing import Protocol, Any, List, Dict, Union
from abc import ABC, abstractmethod
from collections import defaultdict


class ProcessingStage(Protocol):
	def process(self, data: Any) -> Any:
		pass


class InputStage:
	def process(self, data: Any) -> Any:
		if data is None:
			raise ValueError("No data provided to Inout stage")
		else:
			return data


class TransformStage:
	def process(self, data: Any) -> Any:
		print("Transform: Enriched with metadata and validation")

		if isinstance(data, dict):
			if "value" in data:
				tmp = data["value"]
			else:
				tmp = 0.0
			res = {"type": "JSON", "temp": tmp}
			return res

		if isinstance(data, str):
			if "," in data:
				print("Transform: Parsed and structured data")

				splited = data.split(",")

				if len(splited) >= 2:

					res = {"type": "CSV", "first": splited[0], "second": splited[1]}
					return res
				else:
					raise("Invalid data format")
			else:
				raise("Invalid data format")


		if isinstance(data, list):
			print("Transform: Aggregated and filtered")
			valid_data = [x for x in data if -50 <= x <= 100]

			if valid_data:
				avg = sum(valid_data) / len(valid_data)
			else:
				avg = 0.0

			return{
				"type": "stream",
				"len": len(valid_data),
				"avg": avg
			}


class OutputStage:
	def process(self, data: Any) -> Any:
		if isinstance(data, dict):
			if data['type'] == "JSON":
				temp = data['temp']
				if 0 <= temp <= 50:
					return f"Processed temperature reading: {temp}°C (Normal range)"
				else:
					return f"Output: Processed temperature reading: {temp}°C (Not normal range)"
			if data['type'] == "CSV":
				return f"{data['first']} activity logged: 1 {data['second']} processed"
			if data['type'] == "stream":
				return f"Stream summary: {data['len']} readings, avg: {data['avg']:.1f}°C"
		return f"Non processed data: {data}"

class ProcessingPipeline(ABC):
	def __init__(self, pipeline_id):
		self.pipeline_id = pipeline_id
		self.stages = []

	def add_stage(self, stage):
		self.stages.append(stage)

	@abstractmethod
	def process(self, data: Any) -> Any:
		pass


class JSONAdapter(ProcessingPipeline):
	def __init__(self, pipeline_id):
		super().__init__(pipeline_id)
	
	def process(self, data: Any) -> Union[str, Any]:
		res = data
		for s in data.stages:
			res = s.process(res)
		return res


class CSVAdapter(ProcessingPipeline):
	def __init__(self, pipeline_id):
		super().__init__(pipeline_id)
	
	def process(self, data: Any) -> Union[str, Any]:
		res = data
		for s in data.stages:
			res = s.process(res)
		return res


class StreamAdapter(ProcessingPipeline):
	def __init__(self, pipeline_id):
		super().__init__(pipeline_id)
	
	def process(self, data: Any) -> Union[str, Any]:
		res = data
		for s in data.stages:
			res = s.process(res)
		return res


class NexusManager:
	def __init__(self) -> None:
		print("Initializing Nexus Manager...")
		print("Pipeline capacity: 1000 streams/second")
		self.pipelines = []
	
	def add_pipeline(self, pipeline: Any) -> Any:
		self.pipelines.append(pipeline)
	
	def process_data(self,pipeline_id, data: Any) -> Any:
		if pipeline_id in self.pipelines:
			return self.pipelines[pipeline_id].process(data)
		else:
			print(f"Error: Pipeline {pipeline_id} not found")
			return None


def main() -> None:
	print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")


main()
