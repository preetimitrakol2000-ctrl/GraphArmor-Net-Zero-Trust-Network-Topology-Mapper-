import ctypes
import os
import sys

class GraphBridge:
    def __init__(self, num_nodes: int):
        # Dynamically compile the backend engine
        if not os.path.exists("./libgraph.so") and not os.path.exists("./libgraph.dll"):
            print("[*] Compiling backend C graph infrastructure maps...")
            if sys.platform.startswith("win"):
                os.system("gcc -shared -o libgraph.dll network_graph.c blast_radius.c")
                lib_path = "./libgraph.dll"
            else:
                os.system("gcc -shared -fPIC -o libgraph.so network_graph.c blast_radius.c")
                lib_path = "./libgraph.so"
        else:
            lib_path = "./libgraph.dll" if sys.platform.startswith("win") else "./libgraph.so"

        self.lib = ctypes.CDLL(lib_path)
        self.num_nodes = num_nodes

        # Set up explicit C-to-Python parameter layouts
        self.lib.init_network.restype = ctypes.c_void_p
        self.lib.link_devices.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_float]
        
        self.lib.calculate_blast_radius.argtypes = [
            ctypes.c_void_p, 
            ctypes.c_int, 
            ctypes.POINTER(ctypes.c_int), 
            ctypes.POINTER(ctypes.c_int)
        ]
        self.lib.destroy_network.argtypes = [ctypes.c_void_p]

        # Initialize the network topology graph instance on the C Heap
        self.graph_ptr = self.lib.init_network(self.num_nodes)

    def connect_devices(self, src: int, dest: int, vulnerability: float):
        self.lib.link_devices(self.graph_ptr, src, dest, vulnerability)

    def trace_blast_radius(self, patient_zero: int):
        # Create output arrays using ctypes to match integer arrays in C
        blast_zone_array = (ctypes.c_int * self.num_nodes)()
        zone_size = ctypes.c_int(0)

        self.lib.calculate_blast_radius(
            self.graph_ptr, 
            patient_zero, 
            blast_zone_array, 
            ctypes.byref(zone_size)
        )

        # Cast returned standard items back into high-level Python arrays
        return [blast_zone_array[i] for i in range(zone_size.value)]

    def __del__(self):
        if hasattr(self, 'lib') and self.graph_ptr:
            self.lib.destroy_network(self.graph_ptr)
            print("[+] Network topology heap memory cleared successfully.")
