# Ballnet Pose
Detecção de objetos de interesse em uma partida de futebol de robôs na categoria Very Small Size.

Rede neural especializada em detectar objetos de interesse em uma partida de futebol de robôs Very Small Size. 

Consiste em um modelo <em>YOLOv8</em> treinado em uma base de dados extraída de partidas disputadas pela UnBall na IRONCup 2020. Os objetos detectados são: robôs com a camisa da UnBall, tanto a amarela, quanto a azul; e a bola. Os arquivos de saída são gerados no formato ```txt``` com a classe do objeto; as coordenadas do centro de cada caixa delimitadora (bounding box), assim como sua largura e altura; as coordenadas da frente e trás do robô; seguidas do grau de confiança com que foram detectadas.
  ```
  classe x_bbox y_bbox largura_bbox altura_bbox x_frente y_frente conf_frente x_tras y_tras conf_tras
  ```
  
  | Atributo     | Descrição                                                              |
  |--------------|------------------------------------------------------------------------|
  | classe       | Número inteiro que identifica a classe do objeto.                      |
  | x_bbox       | Coordenada x da caixa delimitadora em pixels.                          |
  | y_bbox       | Coordenada y da caixa delimitadora em pixels.                          |
  | largura_bbox | Largura da caixa delimitadora em pixels.                               |
  | altura_bbox  | Altura da caixa delimitadora em pixels.                                |
  | x_frente     | Coordenada x da frente do objeto em pixels.                            |
  | y_frente     | Coordenada y da frente do objeto em pixels.                            |
  | conf_frente  | Grau de confiança na identificação do ponto (x,y) da frente do objeto. |
  | x_tras       | Coordenada x da traseira do objeto em pixels.                          |
  | y_tras       | Coordenada y da traseira do objeto em pixels.                          |
  | conf_tras    | Grau de confiança na identificação do ponto (x,y) da frente do objeto. |


<p align="center">
  <img style="height: 440px" src="https://github.com/user-attachments/assets/f30c9ef4-4675-42f9-8736-ca095a7c00f1" />
</p>
