from diagrams import Diagram, Edge
from diagrams.k8s.infra import Master, Node
from diagrams import Diagram, Edge
from diagrams.k8s.infra import Master, Node

with Diagram("k8s-cluster", show=False, direction="TB", filename="k8s-cluster", outformat="png",):
  Diagram.DEFAULT_PADDING = 0.5

  master = Master("192.168.1.115")

  node1 = Node("192.168.1.57")
  node2 = Node("192.168.1.59")
  node3 = Node("192.168.1.60")

  master << node1
  master << node2
  master << node3


