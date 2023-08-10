from yolotr.models import Darknet
from yolotr.utils.datasets import *
from yolotr.utils.utils import *
import torch
import os 

current_path = os.path.dirname(__file__)

class  TrafficDetector:
    def __init__(self,
                 img_size=640, 
                 cfg_file="yolov4-tiny.cfg", 
                 weights_file="yolov4-tiny.pt", 
                 names_file="coco.names"):
        self.img_size = img_size
        self.cfg = os.path.join(current_path, F"cfg/{cfg_file}")
        self.weights = os.path.join(current_path, F"cfg/{weights_file}")
        self.names = os.path.join(current_path, F"cfg/{names_file}")
        # 构建模型
        self.model = Darknet(self.cfg, self.img_size)
        # 加载预训练模型
        self.model.load_state_dict(torch.load(self.weights)['model'])
        self.CUDA = torch.cuda.is_available()
        if self.CUDA:
            self.model.cuda()
        # 因为模型中使用了BatchNorm，Dropout等操作，预测的时候需要调用eval屏蔽
        self.model.eval()
        # ------------ 识别类型名
        # 加载类别
        self.names = load_classes(self.names)
    
    def detect(self, img0):
        img = self.format_img(img0)
        if self.CUDA:
            img = img.cuda()
        # 计算侦测结果
        pred = self.model(img, augment=False)[0]
        pred = pred.cpu()
        # 进行最大化抑制
        pred = non_max_suppression(pred, 0.3, 0.2, merge=False, classes=None, agnostic=False)
        # 解析识别结果
        for det in pred:
            if det is not None and len(det):
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img0.shape).round()
        if pred[0] is not None: 
            return pred[0].cpu().detach().numpy()  # 总长6：目标位置与大小（0:3），目标概率(4)，目标类别[5]
        else:
            return None
        
    def detect_mark(self, img0):
        # 侦测
        pred = self.detect(img0)
        # 标注
        if pred is not None:
            # 循环标注
            for result in pred:
                x1, y1, x2, y2 = result[0:4]
                prob = result[4]
                clss = int( result[5])
                cls_name = self.get_name(clss)
                # print([x1, y1, x2, y2], prob, clss, cls_name)
                # 备注：这里可以做一个概率阈值过滤（登录成功，可以考虑使用计数规则）
                # 标注
                img0 = cv2.rectangle(img0, rec=(x1, y1, x2 - x1, y2 - y1), color=(0, 0, 255), thickness=2)
            
        return img0, pred

    def get_name(self, idx):
        return self.names[idx]

    def format_img(self, img0):
        img = letterbox(img0, new_shape=self.img_size)[0]
        img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB
        img = np.ascontiguousarray(img)
        img = torch.from_numpy(img)
        img = img.float()
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)
        return img
    
    def load_image(self, img_file):
        img0 = cv2.imread(img_file)  # BGR
        return img0