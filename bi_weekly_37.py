import math
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        network_str = 0
        highest_network_str = 0
        best_coords = []
        for i in range(len(towers)):
            network_str = 0
            for x in range(0, 3):
                #print(towers[0])
                temp_x = towers[0][0] - towers[1][0]
                temp_y = towers[0][1] - towers[1][1]
                temp_distance = ((float(temp_x) ** 2) + (float(temp_y) ** 2)) ** 0.5
                if temp_distance <= radius:
                    network_str += (towers[0][2] / (1 + temp_distance))
                    print(temp_x, temp_y, temp_distance, network_str)

                if network_str > highest_network_str:
                    #print(network_str, highest_network_str, towers[i][0], towers[i][1])
                    highest_network_str = network_str
                    best_coords = [towers[i][0], towers[i][1]] 
                towers.append(towers[0])
                towers.remove(towers[len(towers) - 1])
            
        print(highest_network_str)
        return best_coords