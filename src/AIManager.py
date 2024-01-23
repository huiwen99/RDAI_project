import torch
import albumentations as A
from torchvision.models import resnet101
from albumentations.pytorch.transforms import ToTensorV2

class AIManager():
    def __init__(self, class_labels):
        self.class_labels = class_labels
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.model = resnet101(weights='DEFAULT').to(self.device)
    

    def get_string_pred(self, pred_int):
        string = self.class_labels[str(pred_int)][1]
        if '_' in string:
            str_ls = string.split('_')
            string = ' '.join(str_ls)
        return string
    
    
    def predict(self, img):
        self.model.eval()
        img = self.transforms(img)
        img = torch.unsqueeze(img, 0)
        with torch.no_grad():
            img = img.to(self.device)
            output = self.model(img)
            prediction = output.argmax(dim=1)[0].item()
         
        return self.get_string_pred(prediction)
        
    
    def transforms(self, img):
        t = A.Compose([
                A.Resize(224,224),
                A.ToFloat(max_value=255),
                A.Normalize(),
                ToTensorV2(),  
            ])
        img = t(image=img)["image"]
        return img
