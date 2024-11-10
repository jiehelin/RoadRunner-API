import grpc
from mathworks.roadrunner import roadrunner_service_pb2
from mathworks.roadrunner import roadrunner_service_pb2_grpc
from mathworks.roadrunner import roadrunner_service_messages_pb2

# 打开与 RoadRunner 服务的连接
with grpc.insecure_channel("localhost:54321") as channel:
    api = roadrunner_service_pb2_grpc.RoadRunnerServiceStub(channel)

    # 创建导入 OpenDRIVE 文件的请求
    importRequest = roadrunner_service_messages_pb2.ImportRequest()
    importRequest.file_path = r"C:\Software\RoadRunner\Assets\opendrive\asda.xodr"
    importRequest.format_name = "OpenDRIVE"
    importRequest.open_drive_settings.import_signals.value = False
    api.Import(importRequest)
