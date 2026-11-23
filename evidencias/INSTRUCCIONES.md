# Evidence checklist — do not submit simulated terminal output

Run the project in GitHub Codespaces and save genuine screenshots using these exact names:

| Task | Evidence file | What must be visible |
| --- | --- | --- |
| 1 | `1_folder_structure.png` | Repository structure |
| 2a | `2a_emotion_detection.png` | Initial detector source |
| 2b | `2b_application_creation.png` | Import and a real `emotion_detector("I love this new technology.")` run |
| 3a | `3a_output_formatting.png` | Response formatting source |
| 3b | `3b_formatted_output_test.png` | Real scores for `I am so happy I am doing this` |
| 4a | `4a_packaging.png` | `EmotionDetection/` and `__init__.py` |
| 4b | `4b_packaging_test.png` | Package import and real response for `I hate working long horas` |
| 5a | `5a_unit_testing.png` | `test_emotion_detection.py` source |
| 5b | `5b_unit_testing_result.png` | Actual unittest results |
| 6a | `6a_server.png` | Flask source |
| 6b | `6b_deployment_test.png` | Browser with `I think I am having fun` and real result |
| 7a | `7a_error_handling_function.png` | Detector HTTP 400 handling |
| 7b | `7b_error_handling_server.png` | Flask blank-input handling |
| 7c | `7c_error_handling_interface.png` | Blank input and `Invalid Respuesta de texto! Please try again!` |
| 8a | `8a_server_modified.png` | Final Pylint-ready server source |
| 8b | `8b_static_code_analysis.png` | Real `python3 -m pylint server.py` output and score |

## Copy/paste text submissions

`entregables_codigo/` contains plain-text copies of source code for submissions asking to paste code. Logs and screenshots requiring *execution* are deliberately not prefilled.

## Commands for genuine evidence

```bash
python3 -m pip install -r requirements.txt
python3 -m unittest test_emotion_detection.py -v
python3 -m pylint server.py
python3 server.py
```

For browser testing, use the Codespaces port 5000. For Python interactive evidence:

```python
from EmotionDetection import emotion_detector
emotion_detector("I love this new technology.")
emotion_detector("I am so happy I am doing this")
emotion_detector("I hate working long horas")
```
