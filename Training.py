from ultralytics import YOLO

model = YOLO("yolo11n-cls.pt")  # load a pretrained model (recommended for training)

results = model.train(data="D:/Abbas/GitHub/ClassificationData/Output", epochs=300, imgsz=1024)