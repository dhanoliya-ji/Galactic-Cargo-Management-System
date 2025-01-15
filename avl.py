class AVLTree:
    def __init__(self, compare_function, node_type):
        self.root = None
        self.size = 0
        self.comparator = compare_function 
        self.node_type = node_type

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2

        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        return x

    def _left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2

        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def insert(self, node):
        self.root = self._insert(self.root, node)

    def _insert(self, current_node, new_node):
        if not current_node:
            self.size += 1
            return new_node
        if self.comparator(new_node, current_node) < 0:
            current_node.left = self._insert(current_node.left, new_node)
        else:
            current_node.right = self._insert(current_node.right, new_node)

        current_node.height = 1 + max(self._height(current_node.left), self._height(current_node.right))

        balance = self._get_balance(current_node)

        if balance > 1 and self.comparator(new_node, current_node.left) < 0:
            return self._right_rotate(current_node)

        if balance < -1 and self.comparator(new_node, current_node.right) > 0:
            return self._left_rotate(current_node)

        if balance > 1 and self.comparator(new_node, current_node.left) > 0:
            current_node.left = self._left_rotate(current_node.left)
            return self._right_rotate(current_node)

        if balance < -1 and self.comparator(new_node, current_node.right) < 0:
            current_node.right = self._right_rotate(current_node.right)
            return self._left_rotate(current_node)

        return current_node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete1(self, node):
        self.root = self._delete1(self.root, node)

    def _delete1(self, current_node, target_node):
        if not current_node:
            return current_node

        if self.comparator(target_node, current_node) < 0:
            current_node.left = self._delete1(current_node.left, target_node)
        elif self.comparator(target_node, current_node) > 0:
            current_node.right = self._delete1(current_node.right, target_node)
        else:
            if current_node.left is None:
                temp = current_node.right
                current_node = None
                self.size -= 1
                return temp
            elif current_node.right is None:
                temp = current_node.left
                current_node = None
                self.size -= 1
                return temp
            temp = self._min_value_node(current_node.right)

            current_node.bin_id = temp.bin_id
            # print("flag 1")
            # print("curr node cap: ", current_node.capacity)
            current_node.capacity = temp.capacity

            current_node.right = self._delete1(current_node.right, temp)

        if current_node is None:
            return current_node

        current_node.height = 1 + max(self._height(current_node.left), self._height(current_node.right))

        balance = self._get_balance(current_node)

        if balance > 1 and self._get_balance(current_node.left) >= 0:
            return self._right_rotate(current_node)

        if balance > 1 and self._get_balance(current_node.left) < 0:
            current_node.left = self._left_rotate(current_node.left)
            return self._right_rotate(current_node)

        if balance < -1 and self._get_balance(current_node.right) <= 0:
            return self._left_rotate(current_node)

        if balance < -1 and self._get_balance(current_node.right) > 0:
            current_node.right = self._right_rotate(current_node.right)
            return self._left_rotate(current_node)

        return current_node
    
    def delete2(self, node):
        self.root = self._delete2(self.root, node)
    def _delete2(self, current_node, target_node):
        if not current_node:
            return current_node
        if self.comparator(target_node, current_node) < 0:
            current_node.left = self._delete2(current_node.left, target_node)
        elif self.comparator(target_node, current_node) > 0:
            current_node.right = self._delete2(current_node.right, target_node)
        else:
            if current_node.left is None:
                temp = current_node.right
                current_node = None
                self.size -= 1
                return temp
            elif current_node.right is None:
                temp = current_node.left
                current_node = None
                self.size -= 1
                return temp
            temp = self._min_value_node(current_node.right)
            current_node.bin_id = temp.bin_id
            current_node.object_id = temp.object_id
            current_node.right = self._delete2(current_node.right, temp)
        if current_node is None:
            return current_node
        current_node.height = 1 + max(self._height(current_node.left), self._height(current_node.right))
        balance = self._get_balance(current_node)
        if balance > 1 and self._get_balance(current_node.left) >= 0:
            return self._right_rotate(current_node)
        if balance > 1 and self._get_balance(current_node.left) < 0:
            current_node.left = self._left_rotate(current_node.left)
            return self._right_rotate(current_node)
        if balance < -1 and self._get_balance(current_node.right) <= 0:
            return self._left_rotate(current_node)
        if balance < -1 and self._get_balance(current_node.right) > 0:
            current_node.right = self._right_rotate(current_node.right)
            return self._left_rotate(current_node)
        return current_node

    def search_bin_by_id(self, root, bin_id):
        if root is None or root.bin_id == bin_id:
            return root
        if bin_id < root.bin_id:
            return self.search_bin_by_id(root.left, bin_id)
        return self.search_bin_by_id(root.right, bin_id)
    
    def search_bin_by_id_and_capacity(self, node, bin_id, capacity):
        if node is None:
            return None
        if node.bin_id == bin_id and node.capacity == capacity:
            return node
        elif bin_id < node.bin_id:
            return self.search_bin_by_id_and_capacity(node.left, bin_id, capacity)
        else:
            return self.search_bin_by_id_and_capacity(node.right, bin_id, capacity)
        
    def search_object_by_id(self,node, object_id):
        def find_object(node, object_id):
            if node is None:
                return None
            
            if node.object_id == object_id:
                return node
            elif object_id < node.object_id:
                return find_object(node.left, object_id)
            else:
                return find_object(node.right, object_id)
        return find_object(node, object_id)
    
    def search_bin(self, tree, cargo_size, cargo_color):
        def find_bin(node, best_fit=None):
            if node is None:
                return best_fit
            if cargo_color == 1:
                if node.capacity >= cargo_size:
                    if best_fit is None or node.capacity < best_fit.capacity or (node.capacity == best_fit.capacity and node.bin_id < best_fit.bin_id):
                        best_fit = node
                best_fit = find_bin(node.left, best_fit)
                best_fit = find_bin(node.right, best_fit)
            elif cargo_color == 2:
                if node.capacity >= cargo_size:
                    if best_fit is None or node.capacity < best_fit.capacity or (node.capacity == best_fit.capacity and node.bin_id > best_fit.bin_id):
                        best_fit = node
                best_fit = find_bin(node.left, best_fit)
                best_fit = find_bin(node.right, best_fit)
            elif cargo_color == 3:
                if node.capacity >= cargo_size:
                    if best_fit is None or node.capacity > best_fit.capacity or (node.capacity == best_fit.capacity and node.bin_id < best_fit.bin_id):
                        best_fit = node
                best_fit = find_bin(node.left, best_fit)
                best_fit = find_bin(node.right, best_fit)
            elif cargo_color == 4:
                if node.capacity >= cargo_size:
                    if best_fit is None or node.capacity > best_fit.capacity or (node.capacity == best_fit.capacity and node.bin_id > best_fit.bin_id):
                        best_fit = node
                best_fit = find_bin(node.left, best_fit)
                best_fit = find_bin(node.right, best_fit)
            return best_fit
        return find_bin(tree.root)

    def find_max_node(self, node):
        current = node
        while current.right:
            current = current.right
        return current

    
    def inorder_traversal(self, node):
        result = []
        self._inorder_traversal(node, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append((node.bin_id, node.capacity))
            self._inorder_traversal(node.right, result)

    def get_size(self):
        return self.size

def comp_bin_capacity(bin1, bin2):
    if bin1.capacity != bin2.capacity:
        return bin1.capacity - bin2.capacity
    else:
        return bin1.bin_id - bin2.bin_id
    
def comp_bin_id(bin1, bin2):
    return bin1.bin_id - bin2.bin_id

def comp_object_id(object1, object2):
    return object1.object_id - object2.object_id




