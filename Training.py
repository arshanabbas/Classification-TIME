from ultralytics import YOLO

model = YOLO("yolo11n-cls.pt")  # load a pretrained model (recommended for training)

results = model.train(data="C:/Users/arab/Documents/GitHub/ClassificationData/Output", epochs=100, imgsz=1024)