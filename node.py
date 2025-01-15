
class bin_capacity_Node:
    def __init__(self,bin_id,capacity):
        self.bin_id=bin_id
        self.capacity=capacity
        self.left = None
        self.right = None
        self.height = 1

class bin_id_Node:
    def __init__(self,bin_id,capacity):
        self.bin_id=bin_id
        self.capacity=capacity
        self.left = None
        self.right = None
        self.height = 1
        self.objid = []

class object_id_Node:
    def __init__(self,object_id, size, color,bin_id):
        self.object_id=object_id
        self.size=size
        self.color=color
        self.bin_id=bin_id
        self.left = None
        self.right = None
        self.height = 1

class object_Node:
    def __init__(self,object_id, size, color):
        self.object_id=object_id
        self.size=size
        self.color=color
        self.left = None
        self.right = None
        self.height = 1
    