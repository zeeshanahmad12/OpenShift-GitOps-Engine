# 🚀 OpenShift-GitOps-Engine

> **Production-Level CI/CD Pipeline** | Python Flask → GitHub Actions → ArgoCD → OpenShift

[![CI Pipeline](https://github.com/zeeshanahmad12/OpenShift-GitOps-Engine/actions/workflows/ci.yml/badge.svg)](https://github.com/zeeshanahmad12/OpenShift-GitOps-Engine/actions/workflows/ci.yml)
[![CD Pipeline](https://github.com/zeeshanahmad12/OpenShift-GitOps-Engine/actions/workflows/cd.yml/badge.svg)](https://github.com/zeeshanahmad12/OpenShift-GitOps-Engine/actions/workflows/cd.yml)

---

## 📌 Project Overview

**OpenShift-GitOps-Engine** ek production-grade CI/CD pipeline project hai jo demonstrate karta hai ke ek real company mein code commit hone se lekar production deployment tak ka poora automated workflow kaise kaam karta hai.

Yeh project **Platform Engineer / DevOps Engineer** roles ke liye CV proof ka kaam karta hai — sirf theory nahi, **working pipeline** hai.

---

## 🎯 Project Purpose

| Maqsad | Detail |
|--------|--------|
| 🔧 CI/CD Automation | Git push hote hi automatic lint, test, build, scan, deploy |
| 🛡️ Security Scanning | SAST (SonarQube) + Container Scan (Trivy) |
| 🔄 GitOps Pattern | ArgoCD Git repo monitor karta hai — manual deploy nahi |
| 📦 Containerization | Production-grade Docker image with non-root user |
| 🌐 OpenShift Deploy | CRC (local) OpenShift cluster pe live deployment |
| 📊 Monitoring | Prometheus + Grafana + Loki + Alertmanager |

---

## 🏗️ Project Structure

```
OpenShift-GitOps-Engine/
│
├── 📁 .github/workflows/
│   ├── ci.yml              # CI Pipeline (lint→test→build→scan→push)
│   └── cd.yml              # CD Pipeline (manifest update→deploy)
│
├── 📁 app/
│   ├── __init__.py
│   ├── main.py             # Flask app entry point
│   ├── routes.py           # API endpoints (/, /health, /api/info)
│   └── config.py           # Dev/Staging/Prod configuration
│
├── 📁 tests/
│   ├── test_unit.py        # Unit tests (pytest)
│   ├── test_integration.py # Integration tests
│   └── test_smoke.py       # Smoke tests (post-deploy health check)
│
├── 📁 docker/
│   ├── Dockerfile          # Production-grade (non-root user)
│   └── .dockerignore
│
├── 📁 k8s/
│   ├── base/               # Base Kubernetes manifests
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   ├── route.yaml      # OpenShift Route
│   │   └── kustomization.yaml
│   └── overlays/
│       ├── dev/            # 1 replica
│       ├── staging/        # 2 replicas
│       └── prod/           # 3 replicas
│
├── 📁 argo/
│   ├── application-staging.yaml  # ArgoCD staging app
│   ├── application-prod.yaml     # ArgoCD prod app
│   └── rollout.yaml              # Canary deployment (10%→50%→100%)
│
├── 📁 monitoring/
│   ├── prometheus-rules.yaml     # Alert rules (CPU, CrashLoop)
│   ├── grafana-dashboard.json    # Dashboard config
│   └── loki-config.yaml          # Log aggregation
│
├── 📁 scripts/
│   ├── update-manifest.sh  # Image tag update (GitOps trigger)
│   ├── smoke-test.sh       # Health check after deploy
│   └── rollback.sh         # Emergency rollback
│
├── 📁 sonarqube/
│   └── sonar-project.properties  # SAST config
│
├── 📁 .linting/
│   ├── .pylintrc           # Python lint rules
│   ├── .flake8             # Flake8 rules
│   ├── .yamllint           # YAML lint rules
│   └── .shellcheckrc       # Bash script rules
│
├── requirements.txt        # Flask, Gunicorn
├── requirements-dev.txt    # pytest, pylint, flake8
└── pytest.ini              # Test configuration
```

---

## 🔄 Pipeline Flow

```
Developer → git push → main branch
                ↓
    ┌─────── CI Pipeline ────────┐
    │                            │
    │  1️⃣  Linting               │
    │     pylint + flake8        │
    │     yamllint + shellcheck  │
    │           ↓                │
    │  2️⃣  SAST Scan             │
    │     SonarQube              │
    │           ↓                │
    │  3️⃣  Unit + Integration    │
    │     pytest (min 80% cov)   │
    │           ↓                │
    │  4️⃣  Docker Build          │
    │     python:3.11-slim       │
    │           ↓                │
    │  5️⃣  Trivy Scan            │
    │     CVE + SCA check        │
    │           ↓                │
    │  6️⃣  Push to Quay.io       │
    │     Tag: Git SHA           │
    └────────────────────────────┘
                ↓
    ┌─────── CD Pipeline ────────┐
    │                            │
    │  7️⃣  Manifest Update       │
    │     k8s/base/deployment    │
    │     Git commit + push      │
    │           ↓                │
    │  8️⃣  ArgoCD Sync           │
    │     Git detect → Deploy    │
    │     Staging first          │
    │           ↓                │
    │  9️⃣  Smoke Test            │
    │     /health → 200 OK       │
    │           ↓                │
    │  🔟  Production Gate       │
    │     Manual approval        │
    │           ↓                │
    │  1️⃣1️⃣ Canary Rollout      │
    │     10% → 50% → 100%       │
    └────────────────────────────┘
                ↓
    ┌─────── Monitoring ─────────┐
    │  Prometheus + Grafana      │
    │  Loki (logs)               │
    │  Alertmanager (alerts)     │
    └────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Category | Tool | Purpose |
|----------|------|---------|
| **App** | Python Flask | Web application |
| **Branch Strategy** | Trunk-Based Development | Fast merges, daily integration |
| **CI Tool** | GitHub Actions | Pipeline orchestration |
| **Linting** | pylint, flake8 | Python code quality |
| **YAML Lint** | yamllint | K8s manifest validation |
| **Shell Lint** | shellcheck | Bash script validation |
| **SAST** | SonarQube | Security vulnerability scan |
| **Testing** | pytest + pytest-cov | Unit + Integration tests |
| **Container** | Docker | Image build |
| **Image Scan** | Trivy | CVE + SCA scanning |
| **Registry** | Quay.io | Container image storage |
| **GitOps** | ArgoCD | Automated deployment |
| **Rollout** | Argo Rollouts | Canary/Blue-Green deploy |
| **Platform** | OpenShift (CRC) | Kubernetes platform |
| **Templating** | Kustomize | Multi-env manifest management |
| **Metrics** | Prometheus | Infrastructure monitoring |
| **Dashboard** | Grafana | Visual monitoring |
| **Logs** | Loki | Log aggregation |
| **Alerts** | Alertmanager | Notification system |

---

## 🌍 Multi-Environment Strategy

| Environment | Namespace | Replicas | Purpose |
|-------------|-----------|----------|---------|
| Dev | python-webapp-dev | 1 | Developer testing |
| Staging | python-webapp-staging | 2 | Pre-production validation |
| Production | python-webapp-prod | 3 | Live traffic |

---

## 🚀 Quick Start

### Prerequisites
```bash
# Required
- OpenShift CRC (local cluster)
- GitHub Account
- Quay.io Account
- ArgoCD installed on OpenShift
```

### Setup Steps
```bash
# 1. Clone repo
git clone https://github.com/zeeshanahmad12/OpenShift-GitOps-Engine

# 2. GitHub Secrets add karo
# QUAY_USERNAME, QUAY_PASSWORD, SONAR_TOKEN, SONAR_HOST_URL

# 3. ArgoCD install karo
ansible-playbook -i inventory.ini site.yml

# 4. App register karo
oc apply -f argo/application-staging.yaml

# 5. git push karo — pipeline automatically chalegi!
git push origin main
```

---

## 📊 API Endpoints

| Endpoint | Method | Response |
|----------|--------|---------|
| `/` | GET | `{"message": "Python WebApp CI/CD Pipeline", "status": "running"}` |
| `/health` | GET | `{"status": "healthy"}` |
| `/api/info` | GET | App version and environment info |

---

## 🔐 Security Features

- ✅ Non-root Docker user (`appuser`)
- ✅ Trivy CVE scanning (CRITICAL + HIGH)
- ✅ SonarQube SAST analysis
- ✅ Git SHA image tagging (never `latest`)
- ✅ GitHub Secrets for credentials
- ✅ OpenShift TLS route (edge termination)

---

## 📈 Monitoring & Alerts

```yaml
Alerts configured:
  - HighCPUUsage: CPU > 85% for 5 minutes
  - PodCrashLooping: Restarts > 3 in 5 minutes
```

---

## 👨‍💻 Author

**Zeeshan Ahmad**
- 🔗 LinkedIn: [linkedin.com/in/zeeshan-khattak](https://linkedin.com/in/zeeshan-khattak)
- 🐙 GitHub: [github.com/zeeshanahmad12](https://github.com/zeeshanahmad12)
- 🎓 Certifications: RHCSA, RHCE, AWS

---

## 📄 License

MIT License — Free to use for learning and portfolio purposes.
