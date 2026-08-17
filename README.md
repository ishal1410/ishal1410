# Vishal Patel

Backend and machine learning engineer. MS Computer Science, LIU Brooklyn, 2026. GPA 3.9. Brooklyn, NY.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vishal1410)
[![Email](https://img.shields.io/badge/vp1412003@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:vp1412003@gmail.com)

> Open to full-time backend and machine learning engineering roles. On F1 OPT and authorized to work in the US now.

I build backend services and the machine learning systems behind them, from the API layer down to the Terraform that provisions it.

## Live

### [glowread](https://github.com/ishal1410/glowread) · [glowread.vercel.app](https://glowread.vercel.app)
`Next.js 16` `React 19` `TypeScript` `Perfect Corp API` `Vitest`

Selfie in, scores across 11 skin concerns and a matched AM/PM routine out. The planner is deterministic code and the LLM only rewrites wording, so the output schema cannot break and 120 Vitest tests can cover the logic that matters.

### [jdecode](https://github.com/ishal1410/jdecode) · [jdecode.vercel.app](https://jdecode.vercel.app)
`Next.js 16` `FastAPI` `Python` `PyMuPDF`

Paste a job posting, get the keywords your resume is missing ranked from critical down to nice to have. Runs on your own key across six providers, four of them free, so it costs nothing to host and stores no keys server side.

## Backend and infrastructure

### [ml-serving-platform](https://github.com/ishal1410/ml-serving-platform)
`FastAPI` `PyTorch` `AWS S3` `Docker` `Terraform` `Prometheus` `Grafana`

EfficientNet-B0 served behind FastAPI, with model weights pulled from S3 at runtime instead of baked into the image. Prometheus feeds a Grafana dashboard, Terraform provisions the AWS side, and GitHub Actions runs pytest on every push.

### [realtime-chat-app](https://github.com/ishal1410/realtime-chat-app)
`Node.js` `TypeScript` `Apollo Server v5` `GraphQL` `Redis` `Kafka` `PostgreSQL` `Kubernetes`

WebSockets for delivery, GraphQL for history. Redis Pub/Sub fans messages across instances so any server can reach a client connected to any other, Kafka carries async events to decoupled consumers, and auth is JWT with bcrypt.

## Machine learning and research

### [deepfake-detection-faceforensics](https://github.com/ishal1410/deepfake-detection-faceforensics)
`TensorFlow` `EfficientNet-B0` `MTCNN` `dlib` `Grad-CAM`

EfficientNet-B0 with spatial attention reached 89.33% at 0.9611 AUC on FaceForensics++, and the best ensemble reached 95.33%. Tested cross-dataset on Celeb-DF v2 it falls to 75.00%, which is the more useful number to report. Group project for AI 688 with Saunil Patel.

### [neural-decoding-bci](https://github.com/ishal1410/neural-decoding-bci)
`Python` `Ridge Regression` `scikit-learn`

Which failure mode actually breaks a brain-computer interface: electrodes dying, or the neural signal drifting over months? On 256-electrode intracortical recordings from an ALS patient (Card et al., NEJM 2024), drift wins by a wide margin. Graduate coursework for AI 689.

## Tools

### [catalogpilot](https://github.com/ishal1410/catalogpilot)
`Python` `Google ADK` `Gemini` `DataHub`

Ask a data catalog a question in plain English, get an answer traced through real lineage and ownership with every asset named by its URN. The agent holds one write tool out of the twelve DataHub exposes, because catalog text is untrusted input reaching a model that has write access.

### [linkedin-job-scanner](https://github.com/ishal1410/linkedin-job-scanner)
`JavaScript` `Node.js` · 8 stars · zero dependencies

Pulls fresh job postings into a spreadsheet from the same public listings a logged-out visitor sees. Most tools in this space want your session cookie, which is exactly the automation LinkedIn restricts accounts for.

<details>
<summary>Other projects</summary>

| Project | Stack | What it does |
|---|---|---|
| [weather-forecast-project](https://github.com/ishal1410/weather-forecast-project) | LSTM · ARIMA · Streamlit | Ensemble weather forecasting dashboard, best RMSE 2.61°C |
| [slippage-impact-model](https://github.com/ishal1410/slippage-impact-model) | Python · NumPy · SciPy | Nonlinear market impact from live order book data, with Lagrange-optimized trade scheduling |
| [ofi-feature-construction](https://github.com/ishal1410/ofi-feature-construction) | Python · pandas | Order flow imbalance features from limit order book data, including cross-asset OFI |
| [music-recommender](https://github.com/ishal1410/music-recommender) | Python · Flask | Collaborative filtering over a user similarity graph, walked to surface unheard tracks |

</details>

## Stack

Languages: Python, TypeScript, JavaScript, Java, C++, SQL

Backend: FastAPI, Node.js, GraphQL, REST, WebSockets, JWT, Next.js

Machine learning: PyTorch, TensorFlow, scikit-learn, OpenCV, EfficientNet, LSTM

Infrastructure: AWS, Docker, Kubernetes, Terraform, Redis, Kafka, PostgreSQL, Prometheus, Grafana

## Contact

[vp1412003@gmail.com](mailto:vp1412003@gmail.com) · [linkedin.com/in/vishal1410](https://www.linkedin.com/in/vishal1410)
