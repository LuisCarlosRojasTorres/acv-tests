
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

``` mermaid
flowchart TD
    A[Start: Reading ConfigFiles] --> B{ReadVideo}
    B -- -->|Yes| C[OK]
    C --> D[Rethink]
    D --> B
    B ---->|No| E[End]

```
