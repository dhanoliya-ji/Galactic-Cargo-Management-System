from bin import Bin
from avl import *
from object import Object, Color
from exceptions import NoBinFoundException
from node import *

class GCMS:
    def __init__(self):
        self.treebyBinCap = AVLTree(comp_bin_capacity, bin_capacity_Node)
        self.treebyBinid = AVLTree(comp_bin_id, bin_id_Node)
        self.treebyObjectcap = AVLTree(comp_object_id, object_Node) 
    
    def add_bin(self, bin_id, capacity):
        binbycap_node = bin_capacity_Node(bin_id, capacity)
        binbyid_id = bin_id_Node(bin_id, capacity)
        self.treebyBinCap.insert(binbycap_node)
        self.treebyBinid.insert(binbyid_id)

    def add_object(self, object_id, size, color):
        if color ==color.RED:
            found_inbin_cap_node = self.treebyBinCap.search_bin(self.treebyBinCap, size,3 )
        if color ==color.BLUE:
            found_inbin_cap_node = self.treebyBinCap.search_bin(self.treebyBinCap, size,1 )
        if color ==color.YELLOW:
            found_inbin_cap_node = self.treebyBinCap.search_bin(self.treebyBinCap, size,2 )
        if color ==color.GREEN:
            found_inbin_cap_node = self.treebyBinCap.search_bin(self.treebyBinCap, size,4)
        if not found_inbin_cap_node:
            raise NoBinFoundException
        found_inbin_id_node = self.treebyBinid.search_bin_by_id(self.treebyBinid.root,found_inbin_cap_node.bin_id)
        found_inbin_id_node.capacity -= size
        new_object_bin_id_node = object_id_Node(object_id, size, color, found_inbin_cap_node.bin_id)
        found_inbin_id_node.objid.append(object_id)
        new_cap_node = bin_capacity_Node(found_inbin_cap_node.bin_id, found_inbin_cap_node.capacity - size)
        self.treebyBinCap.delete1(found_inbin_cap_node)
        self.treebyBinCap.insert(new_cap_node)
        self.treebyObjectcap.insert(new_object_bin_id_node)
        

    def delete_object(self, object_id):
        ob = self.treebyObjectcap.search_object_by_id(self.treebyObjectcap.root, object_id)
        it = self.treebyBinid.search_bin_by_id(self.treebyBinid.root, ob.bin_id)
        cap = it.capacity
        it.objid.remove(object_id)
        it.capacity += ob.size
        new_bin_cap_node = bin_capacity_Node(ob.bin_id, cap + ob.size)
        old_bin_cap_node = self.treebyBinCap.search_bin_by_id_and_capacity(self.treebyBinCap.root, ob.bin_id, cap)
        self.treebyBinCap.delete1(old_bin_cap_node)
        self.treebyBinCap.insert(new_bin_cap_node)
        self.treebyObjectcap.delete2(ob)

    def bin_info(self, bin_id):
        found_inbin_id_node = self.treebyBinid.search_bin_by_id(self.treebyBinid.root,bin_id)
        if found_inbin_id_node is None:
            raise NoBinFoundException
        return (found_inbin_id_node.capacity, found_inbin_id_node.objid)
    def object_info(self, object_id):
        ans = self.treebyObjectcap.search_object_by_id(self.treebyObjectcap.root, object_id)
        return ans.bin_id