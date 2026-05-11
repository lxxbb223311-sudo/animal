import requests

class AmapAPI:
    def __init__(self, api_key):
        self.api_key = "25420c5d592565ab8c90710db4c6c2d6"
        self.base_url = "https://restapi.amap.com/v3"

    # 1. IP 定位（无 GPS 时 fallback）
    def get_location_by_ip(self):
        url = f"{self.base_url}/ip?key={self.api_key}"
        try:
            res = requests.get(url, timeout=5)
            res.raise_for_status()
            data = res.json()
            if data.get("status") == "1":
                return {
                    "lat": float(data["lat"]),
                    "lng": float(data["lng"]),
                    "address": data["address"]
                }
            else:
                return None
        except Exception as e:
            print(f"IP 定位失败：{e}")
            return None

    # 2. 轨迹查询（模拟，实际需结合后端存储）
    def get_history_trajectory(self, user_id):
        # 实际项目中，轨迹数据应存储在后端，这里模拟返回
        return [
            {"lat": 39.908823, "lng": 116.397470, "time": "2024-05-20 10:00:00"},
            {"lat": 39.909823, "lng": 116.398470, "time": "2024-05-20 10:01:00"},
            {"lat": 39.910823, "lng": 116.399470, "time": "2024-05-20 10:02:00"},
        ]

    # 3. 紧急救援（模拟发送救援请求到后端）
    def send_rescue_request(self, lat, lng, user_id):
        # 实际项目中，这里应 POST 数据到你的后端服务器
        print(f"紧急救援请求已发送：纬度 {lat}，经度 {lng}，用户 ID {user_id}")
        return True