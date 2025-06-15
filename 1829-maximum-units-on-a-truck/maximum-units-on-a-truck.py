class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort by units per box, descending
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        result = 0
        
        for boxCount, unitsPerBox in boxTypes:
            take = min(truckSize, boxCount)
            result += take * unitsPerBox
            truckSize -= take
            if truckSize == 0:
                break
                
        return result






        