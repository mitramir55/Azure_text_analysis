# Azure AI Language Demos

This repository contains a collection of Python scripts demonstrating various Azure AI Language and Speech services, including text analysis, translation, entity recognition, question answering, and audio processing.

## Prerequisites

- Python 3.8+
- Azure subscription
- Azure AI Language, Translator, and Speech resources
- [dotenv](https://pypi.org/project/python-dotenv/) for environment variable management
- Required Azure SDKs (see below)

## Setup

1. **Clone the repository**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment variables:**
   Create a `.env` file in the root directory with the following keys as needed by each script:
   - `AI_SERVICE_ENDPOINT`, `AI_SERVICE_KEY`, `PROJECT`, `DEPLOYMENT`
   - `TRANSLATOR_REGION`, `TRANSLATOR_KEY`
   - `LS_CONVERSATIONS_ENDPOINT`, `LS_CONVERSATIONS_KEY`
   - `QA_PROJECT_NAME`, `QA_DEPLOYMENT_NAME`
   - `PROJECT_ENDPOINT`, `MODEL_DEPLOYMENT`
   - `PROJECT_KEY`, `LOCATION`

   Refer to each script for the specific variables required.

4. **Prepare data folders:**
   - Place text files for analysis in the `reviews/`, `ads/`, and `articles/` folders as needed.

## Scripts Overview

### 1. `audio.py`
Interact with an AI assistant that can answer questions about an audio file (e.g., avocados.mp3) using Azure AI chat completions.

**Usage:**
```bash
python audio.py
```

### 2. `speech.py`
Transcribe spoken commands from an audio file and synthesize spoken responses (e.g., telling the time) using Azure Cognitive Services Speech SDK.

**Usage:**
```bash
python speech.py
```

### 3. `translator.py`
Translate user-input text into a selected language using Azure Translator.

**Usage:**
```bash
python translator.py
```

### 4. `entity-custom.py`
Extract custom entities from text files in the `ads` folder using Azure Text Analytics custom entity recognition.

**Usage:**
```bash
python entity-custom.py
```

### 5. `text-classification.py`
Classify text files in the `articles` folder using a custom classification model from Azure Text Analytics.

**Usage:**
```bash
python text-classification.py
```

### 6. `intent-and-entity-recognition.py`
Recognize user intent and entities (e.g., time, date, location) using Azure Language Service and respond accordingly.

**Usage:**
```bash
python intent-and-entity-recognition.py
```

### 7. `questions-answering-app-deployment.py`
Answer user questions using a deployed Azure Question Answering project.

**Usage:**
```bash
python questions-answering-app-deployment.py
```

### 8. `text-analysis.py`
Analyze text files in the `reviews` folder for language, sentiment, key phrases, entities, and links using Azure Text Analytics.

**Usage:**
```bash
python text-analysis.py
```

## Dependencies

Install the required Python packages:
```bash
pip install azure-ai-textanalytics azure-ai-language-conversations azure-ai-translation-text azure-identity azure-core azure-cognitiveservices-speech python-dotenv
```

## References
- [Azure AI Language Documentation](https://learn.microsoft.com/azure/ai-services/language-service/)
- [Azure Cognitive Services Speech](https://learn.microsoft.com/azure/ai-services/speech-service/)
- [Azure Translator](https://learn.microsoft.com/azure/ai-services/translator/)

---

This repository is based on the [Microsoft Learn AI Language Labs](https://github.com/MicrosoftLearning/mslearn-ai-language/tree/main/Labfiles).