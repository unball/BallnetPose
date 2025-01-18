# Ballnet Pose
Detecção de objetos de interesse em uma partida de futebol de robôs na categoria Very Small Size.

Rede neural especializada em detectar objetos de interesse em uma partida de futebol de robôs Very Small Size. 
<p align="center">
  <img style="height: 440px" src="https://github.com/user-attachments/assets/f30c9ef4-4675-42f9-8736-ca095a7c00f1" />
</p>

## Descrição
Consiste em um modelo <em>YOLOv8</em> treinado em uma base de dados extraída de partidas disputadas pela UnBall na IRONCup 2020. Os objetos detectados são: robôs com a camisa da UnBall, tanto a amarela, quanto a azul; e a bola.

## Identificadores

ID | Objeto | Imagem 
---|------- | -------
0 | Robô 0 | ![camisa0-azul](https://github.com/user-attachments/assets/d7e45729-95d6-4f5a-b60e-82f29af17df4)
1 | Robô 1 | ![camisa1-azul](https://github.com/user-attachments/assets/91646781-aab8-4a39-88e7-6ed09b574481)
2 | Robô 2 | ![camisa2-azul](https://github.com/user-attachments/assets/ad5225b5-8056-46f1-8db7-448b0239ad8c)
3 | Bola | ![ball](https://github.com/user-attachments/assets/b317aa1b-16a8-4f4e-9999-c9076cad2f64)



  
## Ambiente de execução
Pacote | Versão
-------| -------
python | 3.12.3
torch | 2.5.1
torchvision | 0.20.1
ultralytics | 8.3.61
> 🚨 Recomenda-se a utilização de uma GPU - _Graphics Processing Unit_ -  para executar o script.

## Exemplo
### Script
```
from detect import *

detector = BallnetPose()
path = "imgs"
locations = detector.detect(path)
```

### Saída esperada
```
[
  Detection(
    robots=[
      Robot(id=1.0, center_x=99.5, center_y=600.5, orientation=49.86451443776053),
      Robot(id=2.0, center_x=559.5, center_y=419.0, orientation=45.76389846093002),
      Robot(id=0.0, center_x=60.0, center_y=603.0, orientation=50.19442890773479)
    ],
    ball=Ball(center_x=192.0, center_y=393.0)
  ),
  Detection(
    robots=[
      Robot(id=1.0, center_x=471.5, center_y=441.0, orientation=49.93921554212619),
      Robot(id=2.0, center_x=113.0, center_y=246.5, orientation=51.34019174590992),
      Robot(id=0.0, center_x=379.0, center_y=444.5, orientation=49.89909245378777)
    ],
    ball=Ball(center_x=436.5, center_y=468.0)
  )
]
```

 O resultado esperado é uma lista de objetos **Detection** (tupla nomeada) composta por objetos **Robot** e **Ball**. Os objetos **Robot** possuem as propriedades: ```id```, ```center_x```, ```center_y```, ```orientation```; já os objetos **Ball** possuem apenas ```center_x``` e ```center_y```.
