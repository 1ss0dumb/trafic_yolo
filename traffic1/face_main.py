from yolo.detector import YOLOv4Detector
import cv2
if __name__ == "__main__":
    detector = YOLOv4Detector(weights="last.pt")
    img = detector.load_image("imgs/IMG_3100.JPG")
    # img = detector.load_image("1.jpg")
    # result = detector.detect(img)[0][0] # [0][0]  # 总长6：目标位置与大小（0:3），目标概率(4)，目标类别[5]
    # print(result)
    # rect = result[0:4].detach().numpy()
    # prob = result[4].detach().item()
    # clss = int( result[5].detach().item())
    # cls_name = detector.get_name(clss)
    # print("侦测结果: ", rect, "，概率：", prob, ",类别:", clss, "类别名：", cls_name)
    img,cls = detector.detect_mark(img)
    img = cv2.resize(img,(300,300))
    cv2.imshow("img",img)
    cv2.waitKey(0)