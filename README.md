# Vishal Patel

Backend and machine learning engineer. MS Computer Science, LIU Brooklyn, 2026. GPA 3.9. Brooklyn, NY.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vishal1410)
[![Email](https://img.shields.io/badge/vp1412003@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:vp1412003@gmail.com)

> Open to full-time backend and machine learning engineering roles. On F1 OPT and authorized to work in the US now.

I build backend services and the machine learning systems behind them, from the API layer down to the Terraform that provisions it. Two of the projects below are deployed and running; the rest are public and reproducible from their READMEs.

## Live

### [glowread](https://github.com/ishal1410/glowread)
`Next.js 16` `React 19` `TypeScript` `Tailwind v4` `Perfect Corp API` `Vitest`
Live at [glowread.vercel.app](https://glowread.vercel.app)

Upload a selfie and get scores across 11 skin concerns, an AM/PM routine, and real products matched to it. The planning is deterministic code and the LLM only rewrites the wording, so the output schema cannot break and every recommendation stays explainable and testable. 120 Vitest tests cover that logic. Face detection runs locally and rejects a photo with no face before the app spends a paid API unit. Narration is fetched after the results are already on screen, because provider latency measured anywhere from 2.7s to 34.1s on back-to-back calls.

### [jdecode](https://github.com/ishal1410/jdecode)
`Next.js 16` `FastAPI` `Python` `PyMuPDF` `Vercel + Render`
Live at [jdecode.vercel.app](https://jdecode.vercel.app)

Paste a job posting and get a ranked list of the keywords your resume is missing, with a match score once you upload it. Keywords are graded from critical down to nice to have, synonyms are resolved so "ML" and "Machine Learning" count once, and a red flag pass catches vague pay and impossible requirements. It runs on your own API key across six providers, four of which have free tiers, so it costs nothing to host and stores no keys on the server.

## Backend and infrastructure

### [ml-serving-platform](https://github.com/ishal1410/ml-serving-platform)
`FastAPI` `PyTorch` `AWS S3` `Docker` `Terraform` `Prometheus` `Grafana` `GitHub Actions`

An EfficientNet-B0 image classifier served behind a FastAPI application. Model weights load from S3 at runtime rather than baking into the image, Prometheus scrapes request metrics into a Grafana dashboard, Terraform provisions the AWS side, and GitHub Actions runs the pytest suite on every push.

### [realtime-chat-app](https://github.com/ishal1410/realtime-chat-app)
`Node.js` `TypeScript` `Apollo Server v5` `GraphQL` `Redis` `Kafka` `PostgreSQL` `Kubernetes`

A chat backend split across WebSockets for delivery and GraphQL for history. Redis Pub/Sub fans messages out so any server instance can broadcast to clients connected to any other, Kafka carries async events to decoupled consumers, DataLoader batches the GraphQL resolvers, and auth is JWT with bcrypt. Kubernetes manifests and a Jest suite are in the repo.

## Machine learning and research

### [deepfake-detection-faceforensics](https://github.com/ishal1410/deepfake-detection-faceforensics)
`TensorFlow` `EfficientNet-B0` `MTCNN` `dlib` `scikit-learn` `Grad-CAM`

Detecting manipulated video on FaceForensics++. An EfficientNet-B0 with a spatial attention module reached 89.33% accuracy at 0.9611 AUC on its own, and the best ensemble configuration reached 95.33%. Tested cross-dataset on Celeb-DF v2 it drops to 75.00%, which is the more useful number: it shows how much of the performance was dataset-specific. Grad-CAM overlays on the failed Celeb-DF cases show where the model looked when it got them wrong. Group project for AI 688 with Saunil Patel.

### [neural-decoding-bci](https://github.com/ishal1410/neural-decoding-bci)
`Python` `Ridge Regression` `scikit-learn`

What actually breaks a brain-computer interface decoder in the real world. Using intracortical recordings from an ALS patient with 256 implanted electrodes (Card et al., NEJM 2024), I compared two failure modes: electrodes dying, and the neural signal drifting over months. Drift wins by a wide margin. Sensor dropout degrades the decoder but Ridge regularization recovers some of it, while a decoder trained on the August 2023 session is unusable by April 2025 no matter how much extra training data you give it. Graduate coursework for AI 689.

## Tools

### [catalogpilot](https://github.com/ishal1410/catalogpilot)
`Python` `Google ADK` `Gemini` `DataHub`

Ask a data catalog a question in plain English and get an answer traced through real lineage, ownership, and governance metadata, with every asset named by its URN so you can go verify it. Two design decisions carry it. The agent holds one write tool out of the twelve DataHub exposes, because catalog text is untrusted input reaching a model that has write access, so a prompt injection tops out at an unwanted document instead of stripped governance metadata. And write-back is checked against the tool calls that actually happened, so a model that says it saved a document without calling `save_document` is reported as a failure.

### [linkedin-job-scanner](https://github.com/ishal1410/linkedin-job-scanner)
`JavaScript` `Node.js` · 8 stars · zero dependencies

Pulls fresh LinkedIn job postings into a spreadsheet from the same public listings a logged-out visitor sees. Most tools in this space want your password or session cookie, which is exactly the automation LinkedIn restricts accounts for. This one stays logged out, so your account is never part of the transaction. Configure your target roles once, then one command does the checking.

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
