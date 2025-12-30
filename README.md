simple docker project for beginners

In this project: python app + nginx + monitoring (grafana, prometheus, cAdvisor)

To do: docker-compose up -d

┌─────────────┐
│   Browser   │
│  (User)     │
└─────┬───────┘
      │ HTTP :80
      ▼
┌─────────────┐
│   NGINX     │
│  (web)      │
│             │
│ /           │───▶ Static files
│ /api/*      │───▶ Flask
└─────┬───────┘
      │ internal Docker network
      ▼
┌─────────────┐
│   Flask     │
│  (app)      │
│  :8000      │
│  internal   │
└─────────────┘


┌─────────────────────────────────────────────┐
│           Docker Engine / Host              │
│                                             │
│  ┌───────────┐     metrics      ┌─────────┐ │
│  │ cAdvisor  │◀───────────────▶│ Docker  │ |
│  │ :8080     │                  │ Engine  │ │
│  └─────┬─────┘                  └─────────┘ │
│        │ scrape                             │
│        ▼                                    │
│  ┌───────────┐        query     ┌─────────┐ |
│  │Prometheus │◀──────────────▶ │ Grafana │ |
│  │ :9090     │                  │ :3000   │ │
│  └───────────┘                  └─────────┘ │
└─────────────────────────────────────────────┘
