from diagrams import Cluster, Diagram, Node, Edge
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Ing
from diagrams.gcp.network import LoadBalancing
from diagrams.k8s.infra import Node, Master

with Diagram("k8s-nodes", show=False):

    gcp_lb = LoadBalancing("GCP LB")

    with Cluster("Kubernetes"):

        with Cluster("Nodes") as nodes:
            node1= Node("node1")
            node2= Node("node2")
            node3= Node("node3")

        with Cluster("Master"):
            master = Master("master")

    Edge(headport="c", tailport="c", minlen="1", lhead='cluster_Kubernetes') >> nodes
    node1 >> Edge(headport="c", tailport="c", minlen="1", lhead='cluster_MyApp')
