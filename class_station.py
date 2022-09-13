from class_node import Node


class Station(Node):
	def __init__(self, x, y, color) -> None:
		super().__init__(x, y)
		self.color = color

	def __str__(self) -> str:
		text = f"{super().__str__()} - {self.color} station"
		return text

if __name__ == "__main__":
	station_00 = Station(1, 2, "U1")
	print(station_00)
