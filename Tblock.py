import pymongo


class TBlock(dict):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.traffic_label = "traffic"
        self.place_label = "place"
        self.__setitem__("type", None)
        self.__setitem__("traffic_name", None)
        self.__setitem__("predicted_spend_time", None)
        self.__setitem__("place_id", None)
        self.__setitem__("place_pic", None)
        self.__setitem__("place_name", None)

    def is_place(self) -> bool:
        if self.__getitem__("type") != self.place_label:
            return False
        return True

    def is_traffic(self) -> bool:
        if self.__getitem__("type") != self.traffic_label:
            return False
        return True

    def check_place(self) -> tuple:
        if self.__getitem__("type") != self.place_label:
            return False, "type"

        if self.__getitem__("place_id") is None:
            return False, "place_id"

        if self.__getitem__("place_pic") is None:
            return False, "place_pic"

        if self.__getitem__("place_name") is None:
            return False, "place_name"
        return True, None

    def check_traffic(self) -> tuple:
        if self.__getitem__("type") != self.traffic_label:
            return False, "type"
        if self.__getitem__("traffic_name") is None:
            return False, "traffic_name"
        if self.__getitem__("predicted_spend_time") is None:
            return False, "predicted_spend_time"
        return True, None
