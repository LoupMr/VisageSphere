# 📘 Technical Design Document — VisageSphere

> **Project Type:** Local AI Research & Educational Project  
> **Description:** AI-powered face recognition and real-time web data search engine  
> **Stage:** Local-only development and experimentation

---

## 🔍 1. Project Context & Local Constraints

### 1.1 Usage Scale
- Personal project with small-scale usage for learning/testing.

### 1.2 Budget
- Zero-cost development using only open-source technologies.

### 1.3 Environment
- 100% local development on a single machine (no Docker/NAS yet).
- Uses development servers (e.g., `uvicorn`, `flutter run`).

### 1.4 Data Handling
- **Temporary only**: No data storage beyond login credentials.
- Face data is discarded after immediate processing.

### 1.5 Data Sources
- Real-time scraping of publicly available internet data:
  - Social media
  - Public websites
  - OSINT sources

---

## 🧰 2. Recommended Local Development Stack

### 2.1 Frontend (User Interface)
| Technology  | Pros                                 | Cons                          |
|-------------|--------------------------------------|-------------------------------|
| **Flutter** | One codebase for mobile & web        | Slight learning curve         |

✅ **Chosen:** Flutter — Clean cross-platform UI

---

### 2.2 Backend API
| Technology           | Pros                                  | Cons                      |
|----------------------|---------------------------------------|---------------------------|
| **Python + FastAPI** | High performance, great with AI       | None significant locally  |
| Django               | Built-in tools                        | Overhead for small scale  |

✅ **Chosen:** FastAPI — Fast and perfect for ML integrations

---

### 2.3 Face Recognition (AI)
| Technology            | Pros                                  | Cons                           |
|-----------------------|----------------------------------------|--------------------------------|
| **OpenCV + DeepFace** | Accurate, local, open-source           | Setup complexity               |
| FaceNet               | High accuracy                          | Needs more compute resources   |

✅ **Chosen:** OpenCV + DeepFace — Balanced local solution

---

### 2.4 Local Data Storage
| Technology | Pros                         | Cons                         |
|------------|------------------------------|------------------------------|
| SQLite     | Lightweight, no server needed| Not ideal for large systems  |

✅ **Chosen:** SQLite — Simple storage for auth data only

---

### 2.5 Web Crawling & Data Retrieval
- Real-time crawling using:
  - **Scrapy** + **Beautiful Soup**
  - Search engine result parsing (DuckDuckGo, Bing)

---

## 🧱 3. Local Architecture Overview


```
Local Dev Environment
├── Frontend (Flutter App)
│       │
│ REST API requests
│       ▼
└── Backend (FastAPI Server)
├── Face Recognition (DeepFace + OpenCV)
├── Web Crawler (Scrapy, BS4)
└── SQLite DB (Auth only)
```

---

## 🧪 4. Local Development Workflow

1. Run **FastAPI** backend locally:
   ```bash
   uvicorn main:app --reload
    ```

2. Run **Flutter** frontend app:

   ```bash
   flutter run
   ```

3. Image or video input is sent to the backend via HTTP.

4. Backend runs recognition and discards data post-processing.

5. A real-time web crawl finds matching public profiles or mentions.

---

## 🔐 5. Security & Authentication

* Auth data stored in **SQLite** (hashed passwords or OAuth tokens).
* JWT or session-based login system.
* HTTPS not required locally but planned for production stage.

---

## ⚖️ 6. Legal & Privacy Considerations

* No persistent face/image data stored.
* Data processed temporarily and deleted after search.
* Crawlers respect `robots.txt` and website ToS.
* This project is for **educational/research** use only.

---

## 🚧 7. Project Milestones

| Phase | Activity                               | Deliverable                     |
| ----- | -------------------------------------- | ------------------------------- |
| 1     | FastAPI backend setup with SQLite auth | API ready                       |
| 2     | Add OpenCV + DeepFace processing       | Face recognition working        |
| 3     | Implement real-time crawler            | Public data search in real-time |
| 4     | Build Flutter frontend                 | User-friendly interface         |
| 5     | Integrate frontend/backend             | End-to-end workflow complete    |
| 6     | Add basic auth + JWT                   | Secure logins enabled           |

---

## 📈 8. Future Improvements

* Add Docker support and Synology NAS deployment
* Refactor for scalability (async jobs, Redis queue)
* Add privacy dashboard for opt-outs
* Research federated learning models for privacy-first AI

---

## ✅ Conclusion

This technical design file outlines the entire structure, tools, and strategy for the **VisageSphere** project — a learning-ground for building AI applications in computer vision, recognition, and ethical web data processing.

This is a personal, research-driven initiative focused on **learning, experimentation, and responsible AI development**.
