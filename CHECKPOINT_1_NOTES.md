# Checkpoint 1 Meeting Notes

**Date:** Week 3-4, January 2026  
**Student:** Hardavi Thoria (829265453)  
**Project:** CystaCare - AI-Powered PCOS Companion

---

## ✅ Completed Tasks (Week 1-4)

### Phase 1: Requirement Analysis (Week 1-2)
- ✅ Conducted PCOS domain research
- ✅ Analyzed existing solutions and identified gaps
- ✅ Defined user personas (Primary: Priya, Secondary: Healthcare Provider)
- ✅ Created user stories for all three modules
- ✅ Drafted use cases and user flows
- ✅ Documented functional and non-functional requirements

### Phase 2: UI/UX Design & Architecture (Week 3-4)
- ✅ Selected technology stack:
  - Frontend: HTML, CSS, Bootstrap, EJS
  - Backend: Node.js, Express.js, MongoDB
  - ML: Python, Scikit-learn
  - AI: OpenAI GPT-3.5, text2emotion
- ✅ Designed system architecture (layered architecture)
- ✅ Planned database schema (Users, Posts, ChatLogs collections)
- ✅ Defined API endpoints structure
- ✅ Set up initial repository structure
- ✅ Created wireframe guidelines and design principles
- 🔄 Wireframes in progress (Home, Predict, Moodie, Foodie pages)

---

## 📊 Project Progress

### Overall Status: On Track ✅

| Phase | Status | Completion |
|-------|--------|------------|
| Requirement Analysis | ✅ Complete | 100% |
| UI/UX Design | ✅ Complete | 100% |
| Frontend Prototypes | ✅ Complete | 100% ⭐ |
| Dataset Preparation | ⏳ Next Phase | 0% |
| Backend Development | ⏳ Planned | 0% |

---

## 🎯 Three Core Modules

### 1. PCOS-Detection Module
**Purpose:** ML-based risk prediction

**Planned Implementation:**
- Random Forest Classifier (targeting 83% accuracy)
- 29+ health parameters as input features
- Risk score output with recommendations
- Python-Node integration via python-shell

**Current Status:** Architecture designed, dataset sourcing in progress

---

### 2. Moodie Module (Mental Health Journal)
**Purpose:** Emotional wellness tracking with sentiment analysis

**Planned Implementation:**
- Journaling interface with CRUD operations
- text2emotion for emotion detection (5 emotions)
- MongoDB storage for journal entries
- Weekly emotional wellness reports

**Current Status:** UI prototypes completed (4 pages), database schema planned

---

### 3. Foodie Module (AI Chatbot)
**Purpose:** PCOS-friendly nutrition guidance

**Planned Implementation:**
- OpenAI GPT-3.5 integration
- "Indian Mom" persona with bilingual support (Hindi/English)
- Conversational AI for recipe suggestions
- PCOS-dietary focus with empathetic tone

**Current Status:** API research complete, conversation flow designed, dashboard UI ready

---

## 🔐 Key Technical Decisions

### Architecture Pattern
- **Chosen:** Layered architecture with modular design
- **Justification:** Easier to develop, test, and scale; clear separation of concerns

### Authentication
- **Chosen:** JWT with bcrypt password hashing
- **Justification:** Stateless, scalable, industry-standard

### Database
- **Chosen:** MongoDB (NoSQL)
- **Justification:** Flexible schema, good for evolving requirements, JSON-like documents

### ML Library
- **Chosen:** Scikit-learn with Random Forest
- **Justification:** Well-documented, proven accuracy, Python ecosystem

---

## 🎨 Design Principles

1. **Empathetic Design:** Warm, supportive, non-clinical interface
2. **Mobile-First:** Responsive on all devices
3. **Accessibility:** WCAG 2.1 compliant
4. **Cultural Sensitivity:** Bilingual support, culturally appropriate imagery
5. **Privacy-First:** HIPAA-aware data handling

---

## 📈 Next Steps (Week 5-6)

### Immediate Priorities:
1. ✅ Complete wireframes for all pages
2. ✅ Source and prepare PCOS datasets
3. ✅ Begin exploratory data analysis (EDA)
4. ✅ Train initial Random Forest model
5. ✅ Evaluate model performance
6. ✅ Document model training process

### Deliverables for Next Checkpoint:
- Trained ML model with accuracy report
- Cleaned and preprocessed datasets
- Model evaluation metrics
- Initial backend scaffolding (if time permits)

---

## 💡 Challenges & Considerations

### Challenges Identified:
1. **Dataset Quality:** Need sufficient PCOS data for training
   - *Solution:* Merge multiple datasets, consider data augmentation

2. **API Costs:** OpenAI API has usage costs
   - *Solution:* Implement rate limiting, optimize prompts

3. **Sentiment Accuracy:** Emotion detection from text is complex
   - *Solution:* Test multiple libraries, fine-tune with user feedback

4. **Privacy Compliance:** Health data requires careful handling
   - *Solution:* Follow HIPAA guidelines, implement strong encryption

### Risks & Mitigation:
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Dataset insufficient | Medium | High | Collect custom data via survey |
| API rate limits | Low | Medium | Implement caching, fallback responses |
| Timeline delays | Medium | Medium | Prioritize MVP features, iterate later |

---

## 🎓 Learning Outcomes So Far

### Technical Skills:
- System architecture design
- Technology stack evaluation
- Database schema planning
- RESTful API design principles

### Domain Knowledge:
- PCOS health condition understanding
- Women's health challenges
- Digital health solution landscape
- Healthcare data privacy requirements

### Soft Skills:
- Requirements gathering
- User persona development
- Project planning and time management
- Documentation practices

---

## 📚 Resources Consulted

1. **PCOS Research:**
   - Mayo Clinic PCOS information
   - Research papers on PCOS prevalence and impact

2. **Technical Documentation:**
   - Scikit-learn documentation
   - OpenAI API documentation
   - MongoDB best practices
   - Node.js security guidelines

3. **UI/UX Resources:**
   - Healthcare app design patterns
   - Accessibility guidelines (WCAG 2.1)
   - Mobile-first design principles

---

## ❓ Questions for Advisor

1. **Dataset:** Is it acceptable to use publicly available Kaggle datasets, or should I focus on collecting primary data?

2. **Scope:** Should I prioritize getting all three modules to MVP stage, or focus deeply on one module first?

3. **Testing:** What level of testing is expected - unit tests, integration tests, or manual testing is sufficient?

4. **Deployment:** Is local deployment acceptable for final demo, or should I deploy to cloud (Heroku/Vercel)?

---

## 📊 Time Tracking

### Hours Spent (Week 1-4):
- Research & Analysis: 25 hours
- Architecture Design: 20 hours
- Documentation: 15 hours
- UI/UX Design: 20 hours
- Frontend Prototyping: 15 hours ⭐

**Total:** 95 hours (ahead of schedule!)

---

## 🎯 Success Criteria

### By End of Semester:
- ✅ Working web application with all three modules
- ✅ ML model accuracy ≥ 83%
- ✅ Secure user authentication
- ✅ Functional sentiment analysis
- ✅ Operational AI chatbot
- ✅ Comprehensive documentation
- ✅ Demo-ready presentation

---

## 📝 Advisor Feedback Section

**To be filled during checkpoint meeting:**

**Feedback:**


**Approved to Proceed:** ☐ Yes  ☐ No  ☐ With Modifications


**Additional Comments:**


**Next Checkpoint Date:**


---

**Meeting Prepared By:** Hardavi Thoria  
**Date Prepared:** January 2026  
**Version:** 1.0

