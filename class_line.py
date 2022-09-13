class Line:
	
	line = []

	def __init__(self, color) -> None:
		self.color = color

	def add_node(self, node):
		self.line.append(node)

	def __str__(self) -> str:
		text = f"{self.color}:"
		for node in self.line:
			text += f"\n{node.__str__()}"
		return text


if __name__ == "__main__":
	from class_node import Node
	from class_station import Station
	station_00 = Station(0, 0, "U1")
	station_01 = Node(1, 0)
	station_02 = Station(1, 1, "U1")
	station_03 = Node(1, 2)
	station_04 = Station(2, 2, "U1")
	line_00 = Line("U1")
	line_00.add_node(station_00)
	line_00.add_node(station_01)
	line_00.add_node(station_02)
	line_00.add_node(station_03)
	line_00.add_node(station_04)
	print(line_00)
