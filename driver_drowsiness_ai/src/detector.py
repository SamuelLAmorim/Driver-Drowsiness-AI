import config
from ultralytics import YOLO
import cv2

class EyeDetector:
    def __init__(self):
        self.model = YOLO(config.MODEL_PATH)

    def detect(self, frame):
        results = self.model(frame, conf=config.CONF_THRESHOLD, verbose=False)

        eye_closed = False

        for r in results:
            for box in r.boxes:

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cls = int(box.cls)
                conf = float(box.conf)

                label = self.model.names[cls].lower()

                # COR DO BOX
                color = (0,0,255) if "closed" in label else (0,255,0)

                # DESENHA O QUADRADO
                cv2.rectangle(frame, (x1,y1), (x2,y2), color, 2)

                # TEXTO DO BOX
                text = f"{label} {conf:.2f}"
                cv2.putText(frame, text, (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

                # CONTROLE DE ESTADO
                if "closed" in label:
                    eye_closed = True

        return eye_closed