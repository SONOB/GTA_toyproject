coco128을 사용해 만든 자동조준 입니다.

$pip install torch

$pip install numpy

$pip install opencv-python

$pip install pyautogui

$pip install pillow

위 5개를 pip install해주시고 KBcmd.py파일과 best.pt파일을 같은 폴더상에 놔주고 실행시키면 됩니다.

coco128을 사용했기 떄문에 다른물건들도 인식할것인데 본 코드에서는 'person'만 따라가게 설정했기 때문에 화면상 'person'으로 인식되는 물체만 따라갈 것입니다.

총을 쏘는 키를 'K'키로 지정했기 때문에 발사버튼의 서브키로 'K'를 설정해주시고 마우스를 인게임이 아닌 'WINDOW'로 지정해주셔야 움직일 겁니다.
