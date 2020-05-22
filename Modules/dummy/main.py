import os

class Dummy:
    model = None
    result = None
    path = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        # TODO
        #   - 분석에 필요한 모델이 별도의 초기화나 load가 필요한 경우 이곳에서 초기화를 진행합니다.
        #   - self.model_name을 분석 모델의 이름으로 수정해야 하며 이 변수는 전체 결과에서 구분자 역할을 합니다.
        #     (전체 결과 예시 : [{'name': 'Dummy', 'result': []}, {'name': 'Dummy2', 'result': []}]})
        self.model_name = "Dummy"

    def analysis_from_json(self, od_result):
        '''
        TODO
            - 이미지 경로와 Object detection(e.g. ssd-mobilenet-v2) 결과를 포함한 json data(od_result)를 입력으로 받아 분석하는 함수입니다.
            - input이 되는 json data의 형태는 다음과 같습니다.
            {
                "image_path": "/home/user/image/image.jpg",
				"cam_id": 0,
				"frame_num": 0,
				"results": [
                    {
                        "module_name": "ssd-mobilenet-v2",
                        "detection_result": [
                            {   # ===== When the label of the detection result is one ===== #
                                "labels": [
                                    { "description": "person", "score": 0.865448932 },
                                ],
                                "position": {
                                    "x": 100,               -> float
                                    "y": 100,               -> float
                                    "w": 100,               -> float
                                    "h": 100,               -> float
                                }
                            },
                            {   # ===== When the label of the detection result is multiple ===== #
                                "labels": [
                                    { "description": "dog", "score": 0.865448932 },
                                    { "description": "cat", "score": 0.105616512 },
                                    .....
                                ],
                                "position": {
                                    "x": 100,               -> float
                                    "y": 100,               -> float
                                    "w": 100,               -> float
                                    "h": 100,               -> float
                                }
                            },
                        ]
                    }
                ]
            }
        '''
        result = []
        import time
        time.sleep(2)

        self.result = result

        return self.result