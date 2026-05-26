# =============================================================================
# PORTFOLIO CONTENT — edit this file to update your portfolio
# =============================================================================

OWNER = {
    "name": "fergan van jaarsveld",
    "title": "data & iot",
    "location": "cape town, za // remote",
    "contact": {
        "email":    "ferganvanj@gmail.com",
        "github":   "github.com/Ferganvj",
        "linkedin": "linkedin.com/in/ferganvj",
    },
}

ABOUT = (
    "iot, ml pipelines and cloud infrastructure in industry 4.0 environments. "
    "bridges ot/it integration gaps to deliver observability platforms and automated "
    "data pipelines that support real-time decisions. hands-on with machine-generated "
    "telemetry at production scale, with grounded awareness of the constraints imposed "
    "by physical systems and operational technology."
)

EXPERIENCE = [
    {
        "role":    "customer success engineer / platform engineer",
        "company": "dataprophet",
        "period":  "2022 — 2026",
        "highlights": [
            "led onboarding and training on internal industrial observability workflows covering grafana dashboards configuration and edge device fleet visibility and platform health monitoring across ec2 web service instances and databases (postgresql) interpreting indicators, data flow behavior and common operational failure modes in production environment.",
            "collaborated with engineering and edge (iot) team to escalate and prioritize critical issues on front- and back-end.",
            "(saltstack, ec2, docker) operated and maintained in-house infrastructure supporting automated deployment workflows and platform reliability.",
            "(iot, edge) troubleshoot ot/it issues between plant-floor devices and cloud-based brokers (data source configuration and device inventory).",
            "(iot) debugged edge gateway services via ssh (log analysis, network diagnostics, service restarts).",
            "(elk, grafana, prometheus) built industrial telemetry dashboards to support process insights and operational observability.",
            "(linux, wireguard, openvpn) diagnosed vpn connectivity issues using cli, configuration files, key management and network diagnostics.",
            "(jira) managed customer support desk.",
            "drove internal process improvements by identifying recurring issues and implementing continuous improvement solutions.",
            "supported change management and continuous improvement initiatives aligned with organisational maturity to industry 4.0 readiness.",
        ],
    },
    {
        "role":    "software engineer intern",
        "company": "dataprophet",
        "period":  "2022 — 2022",
        "highlights": [
            "collaborated with engineers and technical leads participating in meetings and discussions.",
            "(in-house tools, elk stack) built and optimized monitoring dashboards for machine-generated time-series data, improving clarity and operational usability.",
            "contributed to technical documentation and knowledge sharing.",
            "collaborated with cross-functional teams, discussing roadblocks and fostering an environment of continuous learning.",
        ],
    },
]

PROJECTS = [
    {
        "name":        "deepfake-detection-system",
        "description": "modern deepfake detection project",
        "tech":        ["python", "deep learning", "traditional ml", "federated learning", "jupyter"],
        "detail": (
            "modular deepfake detection system built in python that combines three distinct approaches "
            "to classifying real versus ai-generated face images. the deep learning backbone supports three "
            "pretrained architectures — efficientnet-b4, xception, and vision transformer (vit-b/16). "
            "all fine-tuned for binary deepfake classification using the timm library. a traditional machine "
            "learning pipeline is also included, where raw face images are compressed via pca before being fed "
            "into classical classifiers such as lda, logistic regression and gaussian naive bayes. the "
            "project uniquely incorporates federated learning through the flower framework, simulating distributed "
            "training across multiple clients using either fedavg or fedprox strategies which is useful for "
            "privacy-sensitive settings where data cannot be centralized. all hyperparameters are managed "
            "through yaml config files and a model registry pattern (@register_model) makes adding new architectures "
            "a three-step process. the system supports three major deepfake datasets: celeb-df v2, faceforensics++ and dfdc "
            "with included download and preprocessing scripts that extract face crops and write csv manifests. "
            "a gradio-based web demo lets users upload any photo and receive a fake-probability score in the browser "
            "with no additional code. four jupyter notebooks walk through each major component: data exploration, "
            "traditional ml with pca, deep learning and federated training making the project equally useful as a "
            "research baseline or a learning resource."
        ),
    },
    {
        "name":        "home_monitoring",
        "description": "real-time pipeline monitoring system",
        "tech":        ["python", "kafka", "grafana", "postgres"],
        "detail": (
            "collecting system, network, and gpu metrics from a linux/wsl2 machine and streams them through "
            "a full iot-style pipeline into grafana dashboards. raw metrics travel two paths: a custom 5-stage "
            "python pipeline (scrape → process → mqtt → kafka → postgresql) that computes metrics and fires "
            "threshold-based alerts and a direct prometheus path for raw time-series data and gpu stats. "
            "everything runs in docker with 12 containerized services: mosquitto, kafka, postgresql, prometheus, "
            "alertmanager, grafana and custom python agents that are all wired together with health checks and "
            "automatic restarts. security is enforced throughout: no hardcoded credentials, non-root containers, "
            "per-role mqtt users, and secret scanning on every commit."
        ),
    },
    {
        "name":        "muliti-robot-path-finding",
        "description": "conflict based search for finding optimal robot paths",
        "tech":        ["python", "graph theory", "heuristic search", "conflict based search"],
        "detail": (
            "v1 - multi-robot path planning problem is the problem of finding optimal (or close to optimal) "
            "paths for n robots simultaneously without collisions where each robot has a designated start and goal state. "
            "v2 - more structured and visually interpretable system, focusing on clarity, visualization and "
            "improved architecture."
        ),
    },
    {
        "name":        "ml_api",
        "description": "fastapi ml inference service",
        "tech":        ["python", "fastapi", "docker", "scikit-learn"],
        "detail": (
            "production-ready ml model serving api with async inference, "
            "model versioning, health checks, and prometheus metrics. "
            "fully containerised for repeatable deployments."
        ),
    },
    {
        "name":        "terminal-kit",
        "description": "a shell that feels good",
        "tech":        ["shell"],
        "detail": (
            "turning any developer terminal into a pro workspace in under 60 seconds."
        ),
    },
    {
        "name":        "female-health-risk-model",
        "description": "a reproducible python pipeline for analyzing miscarriage risk and "
                        "menstrual irregularity in women aged 24–32 using nhanes public health data.",
        "tech":        ["python", "logistic regression", "random forest", "xgboost"],
        "detail": (
            "investigates the relationship between hormonal, metabolic and lifestyle variables "
            "including testosterone, thyroid function, bmi, insulin resistance and reproductive history "
            "including adverse reproductive outcomes using three nhanes survey cycles "
            "(2015–2016, 2017–2020, 2021–2023)."
        ),
    },
    {
        "name":        "ai-assistant",
        "description": "a dual-purpose engineering toolkit combining a locally-hosted llm coding "
                        "assistant with a real-time log processing and anomaly detection pipeline.",
        "tech":        ["python", "llm", "log processing", "anomaly detection"],
        "detail": (
            "coder-assistant model served via ollama, built on qwen2.5-coder:14b at temperature 0.2. "
            "the model is configured with a strict engineering persona as it operates as a senior software "
            "engineer and systems architect. its behavior: "
            "> restates problems in technical terms before answering. "
            "> outputs structured responses: plan → patch → risk check. "
            "> produces targeted before/after patches instead of full-file rewrites. "
            "> enforces refactoring rules: remove duplicates, remove artifacts, improve modularization. "
            "> persists architectural decisions and trade-offs in memory/project_memory.md."
        ),
    },
]

SKILLS = {
    "languages":        ["python", "postgresql", "bash"],
    "data":             ["pandas", "numpy"],
    "infrastructure":   ["linux", "docker", "ci/cd", "saltstack"],
    "observability":    ["grafana", "prometheus", "elk stack"],
    "machine learning": ["pytorch", "scikit-learn"],
}
