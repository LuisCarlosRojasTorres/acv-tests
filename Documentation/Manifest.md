
## Flowchart generico para App V1.0.0
- Assumindo:
  - Source é um video.
  - O Tipo de exercicio foi escolhido pelo usuário.
- Application Data:
  - `appsettings.json`
    - `MediaPipeFrameRate`: A cada quantos frames do source o MediaPipe vai calcular os landmarks
      - Assumindo source a 30fps um MediaPipeFrameRate:5 é um bom inicio
  - `<ExerciseName>Data.json`
    - Arquivo com valores minimos e maximos de ângulo e deslocamento dos pontos de interés para um exercicio determinado. 

## FSM

- The main application is a loop which iterates through each frame.

``` mermaid
stateDiagram-v2
[*] --> Get_Frame
Get_Frame --> [*] : Other frames

Get_Frame --> Get_Landmarks : Each x frames 
  Get_Landmarks --> [*] : Failed

  Get_Landmarks --> Get_Points_and_Angles : Success
    Get_Points_and_Angles --> Analyse_Results : Success
    Analyse_Results --> Show_Frame 
    Show_Frame --> [*]

  Get_Points_and_Angles --> [*] : Failed  
```