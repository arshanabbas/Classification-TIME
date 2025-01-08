from ultralytics import YOLO

model = YOLO("yolo11n-cls.pt")  # load a pretrained model (recommended for training)

results = model.train(data="mnist160", epochs=1, imgsz=64)