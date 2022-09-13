class Node:
	def __init__(self, x, y) -> None:
		self.x = x
		self.y = y

	def __str__(self) -> str:
		text = f"({self.x}, {self.y})"
		return text


if __name__ == "__main__":
	node_00 = Node(1, 2)
	print(node_00)
