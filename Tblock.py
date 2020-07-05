from typing import Optional

import pymongo
PLACE_TYPE = "place"
TRACFFIC_TYPE = "traffic"
class Block_core(dict):

    def __init__(self, Block_core_type):
        self.traffic_label = TRACFFIC_TYPE
        self.place_label = PLACE_TYPE
        self.__setitem__("type", Block_core_type)
    def type(self):
        return self.__getitem__("type")

    def is_place(self) -> bool:
        if self.__getitem__("type") != self.place_label:
            return False
        return True

    def is_traffic(self) -> bool:
        if self.__getitem__("type") != self.traffic_label:
            return False
        return True

class PlaceBlock(Block_core):
    def __init__(self,Block_core_type:str,place_id:str,place_pics:[str],place_name:str,predicted_spend_minute:Optional[int] = None,place_main_pic_index:int=0):
        super().__init__(Block_core_type)
        self.__setitem__("predicted_spend_time", predicted_spend_minute)
        self.__setitem__("place_id", place_id)
        self.__setitem__("place_pics", place_pics)
        self.__setitem__("place_name", place_name)

        ##
        self.__setitem__("place_main_pic_index", place_main_pic_index)



    def check_place(self) -> tuple:
        if not self.is_place():
            return False, "type"

        if self.__getitem__("place_id") is None:
            return False, "place_id"

        if self.__getitem__("place_pics") is None:
            return False, "place_pics"

        if self.__getitem__("place_name") is None:
            return False, "place_name"
        return True, None

class TrafficBlock(Block_core):
    def __init__(self, Block_core_type,traffic_name,predicted_spend_minute,start_location_name,end_location_name):
        super().__init__(Block_core_type)
        self.__setitem__("traffic_name", traffic_name)
        self.__setitem__("predicted_spend_minute", predicted_spend_minute)
        self.__setitem__("start_location_name", start_location_name)
        self.__setitem__("end_location_name", end_location_name)


    def check_traffic(self) -> tuple:
            if not self.is_traffic():
                return False, "type"
            if self.__getitem__("traffic_name") is None:
                return False, "traffic_name"
            if self.__getitem__("predicted_spend_minute") is None:
                return False, "predicted_spend_minute"
            return True, None
