# Final project

## oaqjp-final-project-emb-ai

**Emotion Detection Web Application using IBM Watson NLP and Flask**

This educational project detects five emotions (anger, disgust, fear, joy, sadness) and returns the dominant emotion. It exposes the Python package `EmotionDetection` and a Flask web interface.

### Project structure

- `EmotionDetection/emotion_detection.py`: Watson NLP request, result formatting and HTTP 400 handling.
- `EmotionDetection/__init__.py`: package export of `emotion_detector`.
- `server.py`: Flask routes `/` and `/emotionDetector`.
- `templates/index.html`: web interface.
- `static/mywebscript.js`: browser interaction with the Flask route.
- `test_emotion_detection.py`: six deterministic unit tests with mock Watson responses (five emotions + HTTP 400).
- `requirements.txt`: Python dependencies.
- `entregables_codigo/`: source-code snapshots for course submission.
- `evidencias/`: checklist of screenshots/results to capture from **your real execution**.

### Run in GitHub Codespaces

From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 server.py
```

Open port `5000` in the Codespaces **Ports** tab. Test the phrase `I think I am having fun`. The result depends on the Watson NLP laboratory endpoint availability.

### Test the Python package

```bash
python3
>>> from EmotionDetection import emotion_detector
>>> emotion_detector("I am so happy I am doing this")
>>> emotion_detector("I hate working long horas")
```

The model is primarily intended for English text, so predicted emotion labels and scores depend on the actual Watson NLP response. Never replace genuine output with fabricated values.

### Unit tests

```bash
python3 -m unittest test_emotion_detection.py -v
```

The bundled unit tests **mock** Watson responses to test Python code reliably. They do not prove live access to the IBM endpoint; live model behavior must be separately checked via the interpreter or Flask UI.

### Static code analysis

```bash
python3 -m pylint server.py
```

Review Pylint's actual score and resolve any environment-specific warnings. Do not submit an invented score.

### Handling invalid input

Empty text yields this required exact text:

`Invalid Respuesta de texto! Please try again!`

A Watson NLP HTTP 400 response results in a Python dictionary of five `None` scores and `dominant_emotion: None`, and the Flask endpoint returns the invalid input message.

### Evidence for evaluation

See `evidencias/INSTRUCCIONES.md`. Real screenshot files and terminal logs are **not** included because they must be produced from your own running Codespaces environment.

### GitHub submission

Publish this project as a **public fork** named `oaqjp-final-project-emb-ai` in your GitHub account. The repository files provided here do **not** establish that GitHub's fork relationship has been created. Verify the fork and commit the files in your own repository.
