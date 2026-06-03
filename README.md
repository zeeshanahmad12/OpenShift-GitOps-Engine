# Python WebApp CI/CD OpenShift

Production-level CI/CD pipeline project.

## Stack
- **App**: Python Flask
- **CI**: GitHub Actions
- **Linting**: pylint, flake8, yamllint, shellcheck
- **SAST**: SonarQube
- **Testing**: pytest + pytest-cov
- **Container Scan**: Trivy
- **Registry**: Quay.io
- **GitOps**: ArgoCD
- **Deploy**: OpenShift (CRC)
- **Monitoring**: Prometheus + Grafana + Loki

## Branch Strategy
Trunk-Based Development

## Pipeline Flow
git push → Lint → SAST → Test → Build → Scan → Push → Deploy
