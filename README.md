# CystaCare: AI-Powered Companion for Managing PCOS

**Project Status:** Initial Development Phase   
**Student:** Hardavi Thoria (829265453)  
**Course:** CPSC 597  
**Professor:** Paul Salvador Inventado   
**Semester:** Spring 2026

---

## 📋 Project Overview

CystaCare is an AI-powered digital health companion designed to support women with PCOS through three intelligent modules:

1. **PCOS-Detection** - ML-based risk prediction
2. **Moodie** - Emotional wellness journaling with sentiment analysis
3. **Foodie** - AI-powered nutrition chatbot

---

## 🎯 Current Phase: UI/UX Design & Architecture Planning

### Completed (Week 1-2):
- ✅ Problem domain research
- ✅ User persona definition
- ✅ Competitive analysis
- ✅ Use case identification
- ✅ Technology stack selection

### In Progress (Week 3-4):
- 🔄 Wireframe development
- 🔄 System architecture design
- 🔄 Database schema planning
- 🔄 Repository setup
- 🔄 Development environment configuration

---

## 🏗️ System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────┐
│           User Interface Layer          │
│    (HTML, CSS, Bootstrap, EJS)          │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│       Application Logic Layer           │
│      (Node.js + Express.js)             │
└─────────────────────────────────────────┘
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│   MongoDB   │ │   Python    │ │   OpenAI    │
│   Database  │ │  ML Models  │ │     API     │
└─────────────┘ └─────────────┘ └─────────────┘
```

### Module Architecture

**1. PCOS-Detection Module**
- Input: User health parameters (29+ features)
- Processing: Random Forest Classifier
- Output: Risk score and recommendations

**2. Moodie Module**
- Input: User journal entries
- Processing: Sentiment analysis (text2emotion)
- Output: Emotional wellness insights

**3. Foodie Module**
- Input: User dietary queries
- Processing: OpenAI GPT-3.5
- Output: PCOS-friendly nutrition advice

---

## 💻 Technology Stack

### Frontend
- HTML5, CSS3, JavaScript
- Bootstrap 5 (Responsive UI)
- EJS Templating Engine

### Backend
- Node.js v18+
- Express.js
- RESTful API architecture

### Database
- MongoDB (NoSQL)
- Collections: Users, Posts, ChatLogs

### Machine Learning
- Python 3.x
- Scikit-learn (Random Forest)
- Pandas, NumPy (Data processing)

### AI/NLP
- OpenAI API (GPT-3.5)
- text2emotion library

### Authentication & Security
- JWT (JSON Web Tokens)
- bcrypt.js (Password hashing)

### Development Tools
- Git/GitHub (Version control)
- VS Code (IDE)
- Postman (API testing)
- Jupyter Notebooks (ML prototyping)

---

## 📂 Repository Structure

```
CystaCare/
├── README.md                  # This file
├── docs/                      # Documentation
│   ├── architecture.md        # System architecture details
│   ├── user-stories.md        # User stories and use cases
│   └── tech-stack.md          # Technology decisions
├── wireframes/                # UI/UX designs
│   ├── home-page.png
│   ├── pcos-detection.png
│   ├── moodie-journal.png
│   └── foodie-chatbot.png
├── src/                       # Source code (initial setup)
│   ├── frontend/              # Frontend components
│   ├── backend/               # Backend API
│   └── ml-models/             # ML model scripts
└── config/                    # Configuration files
    ├── .env.example
    └── package.json.example
```

---

## 👥 User Personas

### Primary User: "Hardavi" - 26-year-old working professional
- **Needs:** Early PCOS detection, emotional support, dietary guidance
- **Pain Points:** Delayed diagnosis, lack of holistic support
- **Tech Savviness:** Moderate (smartphone user, social media active)

### Secondary User: "Healthcare Provider"
- **Needs:** Patient data insights, risk assessment reports
- **Use Case:** Preliminary screening tool


---

## 🎨 Design Principles

1. **User-Centric Design** - Empathetic, non-clinical interface
2. **Accessibility** - WCAG 2.1 compliance
3. **Cultural Sensitivity** - Bilingual support (English/Hindi)
4. **Privacy-First** - HIPAA-compliant data handling
5. **Mobile-Responsive** - Progressive Web App approach

---

## 🔐 Security Considerations

- JWT-based authentication with httpOnly cookies
- Password hashing with bcrypt (10 rounds minimum)
- Input validation and sanitization
- MongoDB injection prevention
- HTTPS enforcement (production)
- Environment variable management
- Rate limiting on API endpoints

---

## 📈 Success Metrics

### Technical Metrics
- ML Model Accuracy: Target 83%+
- API Response Time: < 2 seconds
- Sentiment Analysis Accuracy: 80%+
- System Uptime: 99%+

### User Metrics
- User Registration Rate
- Daily Active Users
- Journal Entry Frequency
- Chatbot Engagement Rate

---

## 🔮 Future Enhancements

- Weekly emotional wellness reports
- Song therapy integration (Spotify API)
- Daily challenges based on mood
- Community forum
- Mobile app (React Native)
- Wearable device integration
- Telemedicine integration

---

## 📚 References

1. Mayo Clinic - PCOS Information
2. Scikit-learn Documentation
3. OpenAI API Documentation
4. MongoDB Documentation
5. Node.js Best Practices

---

## 📞 Contact

**Hardavi Thoria**  
Email: hardavit@csu.fullerton.edu  
Student ID: 829265453

**Faculty Advisor**  
Prof. Paul Salvador Inventado  
Department of Computer Science  
California State University, Fullerton

---

**Last Updated:** January 2026  
**Project Phase:** Initial Development (Weeks 1-2)

