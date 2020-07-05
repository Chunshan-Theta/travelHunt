import unittest
from Tblock import PlaceBlock,PLACE_TYPE,TrafficBlock,TRACFFIC_TYPE

class TestPlaceBlock(unittest.TestCase):
    def test_init_place(self):
        ans = {'type': 'place', 'predicted_spend_time': 13, 'place_id': '123456', 'place_pics': ['http://path.to.pic'], 'place_name': 'PLACE name', 'place_main_pic_index': 0}
        place = PlaceBlock(Block_core_type=PLACE_TYPE,place_id="123456",place_pics=["http://path.to.pic"],place_name="PLACE name",predicted_spend_minute=13,place_main_pic_index=0)
        for k,v in ans.items():
            self.assertEqual(v,place[k])
    def test_init_traffic(self):
        ans = {'type': 'traffic', 'traffic_name': 'bus', 'predicted_spend_minute': 12, 'start_location_name': '台北火車站', 'end_location_name': '台南火車站'}
        trafficblock = TrafficBlock( Block_core_type=TRACFFIC_TYPE,traffic_name="bus",predicted_spend_minute=12,start_location_name="台北火車站",end_location_name="台南火車站")
        for k,v in ans.items():
            self.assertEqual(v,trafficblock[k])

if __name__ == '__main__':
    unittest.main()
