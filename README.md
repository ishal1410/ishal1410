<p align="center">
  <img src="./assets/hero.svg" width="100%" alt="Vishal Patel, backend and ML engineer. Production services and the ML systems behind them, from the API layer down to the infrastructure they run on.">
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/vishal1410"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:vp1412003@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://depositcheck-liart.vercel.app"><img src="https://img.shields.io/badge/SerpApi%20Best%20AI%20Use%20Case-Winner%202026-D29922?style=for-the-badge" alt="Winner, SerpApi Best AI Use Case 2026"></a>
</p>

I build backend services and the machine learning systems behind them, from the API layer down to the infrastructure they run on. Most of what is here started as a question I could not answer by reading, so I built the thing and measured it.

<img src="./assets/stats.svg" width="100%" alt="Public code on this account: 14 repositories, 9 stars, and the share of each language across them, notebook bytes excluded.">

<img src="./assets/section-recent.svg" width="100%" alt="Section 01, Recent">

### [depositcheck](https://github.com/ishal1410/depositcheck) · [live](https://depositcheck-liart.vercel.app)

**Winner, SerpApi "Best AI Use Case" — DevNetwork API+Cloud+AI Hackathon 2026**

![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![SerpApi](https://img.shields.io/badge/SerpApi%20google__lens-4285F4?style=flat-square&logo=google&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel%20Blob-000000?style=flat-square&logo=vercel&logoColor=white)
![177 tests](https://img.shields.io/badge/tests-177-3FB950?style=flat-square)

Upload one photo from a rental listing, type the address you were given, and find out whether those photos already belong to a different property. Rental scams work by theft rather than invention, and the photos are the part the scammer cannot change.

The design decision worth reading is that there is no green "safe" verdict. A listing built from AI-generated photos returns zero reverse-image matches, which is the same signal as an honest landlord who photographed the flat themselves. An accusation therefore requires positive evidence, a competing street address actually found and named by two independent sites, because on its first real production request the tool accused a real landlord off a truncated API response. That rule is written down in [ADR-0001](https://github.com/ishal1410/depositcheck/blob/master/docs/adr/0001-accuse-only-on-positive-evidence.md) and the truncated response is checked in as a regression fixture.

### [ninetyninety](https://github.com/ishal1410/ninetyninety) · [live](https://ishal1410.github.io/ninetyninety/)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Strands Agents](https://img.shields.io/badge/Strands%20Agents-232F3E?style=flat-square)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

A volunteer treasurer's bank export becomes a drafted IRS Form 990-EZ, with every line citing the transactions behind it and the rule that put them there. Two agents classify each row without seeing each other's reasoning, and a referee runs only where they disagree, so disagreements surface on screen instead of being resolved silently.

The arithmetic that fills the form was checked against 3,632 real Form 990-EZ returns from the IRS e-file corpus by rebuilding each return's stated totals from its own line items: 3,632 of 3,632 on total revenue, 99.97% on total expenses. The three mismatches are two real filings whose own totals disagree with their own components, listed in [`results/validation.json`](https://github.com/ishal1410/ninetyninety/blob/master/results/validation.json). Python computes every total; the model never adds.

### Open source

Two pull requests open against [datahub-project/datahub](https://github.com/datahub-project/datahub): a [Vite alias resolution fix](https://github.com/datahub-project/datahub/pull/19336) for builds run from outside the project root, and [column descriptions on hover](https://github.com/datahub-project/datahub/pull/19359) in the lineage graph.

<img src="./assets/section-live.svg" width="100%" alt="Section 02, Live">

### [glowread](https://github.com/ishal1410/glowread) · [glowread.vercel.app](https://glowread.vercel.app)

![Next.js](https://img.shields.io/badge/Next.js%2016-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![React](https://img.shields.io/badge/React%2019-61DAFB?style=flat-square&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Vitest](https://img.shields.io/badge/Vitest-6E9F18?style=flat-square&logo=vitest&logoColor=white)

Selfie in, scores across 11 skin concerns and a matched AM/PM routine out. The planner is deterministic code and the LLM only rewrites wording, so the output schema cannot break and 120 Vitest tests cover the planning logic directly.

### [jdecode](https://github.com/ishal1410/jdecode) · [jdecode.vercel.app](https://jdecode.vercel.app)

![Next.js](https://img.shields.io/badge/Next.js%2016-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

Paste a job posting, get the keywords your resume is missing ranked from critical down to nice to have. It runs on your own key across six providers, four of them free, and the key is passed per request and never stored, so hosting it costs nothing.

<img src="./assets/section-backend.svg" width="100%" alt="Section 03, Backend and infrastructure">

### [ml-serving-platform](https://github.com/ishal1410/ml-serving-platform)

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-844FBA?style=flat-square&logo=terraform&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)

EfficientNet-B0 served behind FastAPI, with model weights pulled from S3 at runtime rather than baked into the image, so the container stays small and the model can be swapped without a rebuild. Terraform provisions the AWS side and the compose stack brings up Prometheus and Grafana alongside the API.

### [realtime-chat-app](https://github.com/ishal1410/realtime-chat-app)

![Node.js](https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white)
![GraphQL](https://img.shields.io/badge/GraphQL-E10098?style=flat-square&logo=graphql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-FF4438?style=flat-square&logo=redis&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)

WebSockets for delivery, GraphQL for history. Redis Pub/Sub fans messages across instances so any server can reach a client connected to any other, and Kafka carries async events to decoupled consumers. Auth is JWT with bcryptjs, DataLoader batches the resolvers, and the repo ships GitHub Actions CI alongside Kubernetes manifests for the app, Postgres, and Redis.

<img src="./assets/section-research.svg" width="100%" alt="Section 04, Machine learning and research">

### [deepfake-detection-faceforensics](https://github.com/ishal1410/deepfake-detection-faceforensics)

![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/EfficientNet--B0-D00000?style=flat-square&logo=keras&logoColor=white)
![OpenCV](https://img.shields.io/badge/MTCNN%20%2B%20Grad--CAM-5C3EE8?style=flat-square&logo=opencv&logoColor=white)

EfficientNet-B0 with spatial attention reached 89.33% at 0.9611 AUC on FaceForensics++, and the best ensemble reached 95.33%. Tested cross-dataset on Celeb-DF v2 it falls to 75.00%, which says more about how well it generalizes than the headline figure does.

### [neural-decoding-bci](https://github.com/ishal1410/neural-decoding-bci)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)

Which failure mode actually breaks a brain-computer interface: electrodes dying, or the neural signal drifting over months? On 256-electrode intracortical recordings from an ALS patient (Card et al., NEJM 2024), drift is by far the more damaging of the two.

<img src="./assets/section-tools.svg" width="100%" alt="Section 05, Tools">

### [catalogpilot](https://github.com/ishal1410/catalogpilot)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Google ADK](https://img.shields.io/badge/Google%20ADK-4285F4?style=flat-square&logo=google&logoColor=white)
![DataHub](https://img.shields.io/badge/DataHub-1890FF?style=flat-square)

Ask a data catalog a question in plain English, get an answer traced through real lineage and ownership with every asset named by its URN. The agent holds one write tool out of the twelve DataHub exposes, because catalog text is untrusted input reaching a model that has write access.

### [linkedin-job-scanner](https://github.com/ishal1410/linkedin-job-scanner)

![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Node.js](https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white)
![zero dependencies](https://img.shields.io/badge/dependencies-0-3FB950?style=flat-square)
[![Stars](https://img.shields.io/github/stars/ishal1410/linkedin-job-scanner?style=flat-square&color=D29922)](https://github.com/ishal1410/linkedin-job-scanner/stargazers)

Pulls fresh job postings into a spreadsheet from the same public listings a logged-out visitor sees. Most tools in this space want your session cookie, which is exactly the automation LinkedIn restricts accounts for.

<details>
<summary><b>Other projects</b></summary>

<br>

| Project | Stack | What it does |
|---|---|---|
| [weather-forecast-project](https://github.com/ishal1410/weather-forecast-project) | LSTM · ARIMA · Streamlit | Ensemble weather forecasting dashboard, best RMSE 2.61°C |
| [slippage-impact-model](https://github.com/ishal1410/slippage-impact-model) | Python · NumPy · SciPy | Nonlinear market impact from live order book data, with Lagrange-optimized trade scheduling |
| [music-recommender](https://github.com/ishal1410/music-recommender) | Python · Flask | Collaborative filtering over a user similarity graph, walked to surface unheard tracks |

</details>

<img src="./assets/section-stack.svg" width="100%" alt="Section 06, Stack">

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![SQL](https://img.shields.io/badge/SQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

**Backend**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-5FA04E?style=for-the-badge&logo=nodedotjs&logoColor=white)
![GraphQL](https://img.shields.io/badge/GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![Socket.io](https://img.shields.io/badge/WebSockets-010101?style=for-the-badge&logo=socketdotio&logoColor=white)

**Machine learning**

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

**Infrastructure**

![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-844FBA?style=for-the-badge&logo=terraform&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-FF4438?style=for-the-badge&logo=redis&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

---

<p align="center">
  <a href="mailto:vp1412003@gmail.com">vp1412003@gmail.com</a> · <a href="https://www.linkedin.com/in/vishal1410">linkedin.com/in/vishal1410</a>
</p>
