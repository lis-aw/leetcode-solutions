class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        print(boxTypes)
        result = 0
        for boxes, unitInBox in boxTypes:
            print(boxes, unitInBox)
            if truckSize > boxes:
                result += boxes * unitInBox
                truckSize-=boxes
            else:
                result += truckSize * unitInBox
                return (result)
        return result






        