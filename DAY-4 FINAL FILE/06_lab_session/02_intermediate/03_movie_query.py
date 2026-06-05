import csv

class MovieQuery:
	"""Loads queries from a CSV file and provides summarized information on request (methods)"""

	criteria = ["year", "genre", "director", "writer", "production_company"]

	def __init__(self, filepath: str):
		self.dataset = self.load_movie_dataset(filepath)

		# Feel free to create more attributes, but you cannot ask for more inputs in __init__

	def load_movie_dataset(self, filepath: str) -> list[dict[str, str]]:
		"""Loads data from given filepath and returns list of dictionaries """
		return []

	def movie_by_criteria(self, criteria_type: str) -> list[str]:
		"""Return all movies names by a given criteria"""
		return []

	def find_movie_by_name(self, movie_name_to_find: str) -> dict[str, str]:
		"""Return dictionary of details for a given movie name (if in dataset)"""
		return {}

	def description(self, criteria_type: str) -> dict[str, float]:
		"""Return dictionary containing the lowest, average, and highest avg_score of a griven criteria_type:
			{"lowest": float, "average": float, "highest": float}
		"""
		return {}

class ConsoleApp:
	"""Class dedicated for console"""

	def __init__(self, dataset):
		self.dataset = dataset

		# Don't change the inputs of __init__
		# But feel free to use different attributes below:


	def start(self) -> None:
		"""Required to implement"""


movie_dataset = MovieQuery(filepath="movies.csv")
console_app = ConsoleApp(movie_dataset)
console_app.start()