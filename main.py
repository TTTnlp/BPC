import numpy

def read_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # 读取节点数
        num_nodes = int(file.readline().strip())
        
        nodes = []
        for _ in range(num_nodes):
            node_data = file.readline().strip().split()
            node_id = int(node_data[0])
            latitude = float(node_data[1])
            longitude = float(node_data[2])
            nodes.append((node_id, latitude, longitude))
        
        # 读取边数
        num_edges = int(file.readline().strip())
        
        edges = []
        for _ in range(num_edges):
            edge_data = list(map(int, file.readline().strip().split()))
            edges.append(tuple(edge_data))
        
        # 读取用户数
        num_users = int(file.readline().strip())
        
        users = []
        for _ in range(num_users):
            user_data = file.readline().strip().split()
            user_id = int(user_data[0])
            latitude = float(user_data[1])
            longitude = float(user_data[2])
            users.append((user_id, latitude, longitude))

    # print("Nodes:", nodes)
    # print("Edges:", edges)
    # print("Users:", users)
    
    return nodes, edges, users




if __name__ == '__main__':
    read_data('./small_Minsk.txt')
