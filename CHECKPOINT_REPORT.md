# CystaCare - Checkpoint 1 Project Report

**Student:** Hardavi Thoria (829265453)  
**Project:** CystaCare - AI-Powered PCOS Companion  
**Date:** January 25, 2026  
**Phase:** Weeks 3-4 (Architecture & UI Design)

---

## 1. Progress - What Was Completed

✅ **Requirements & Planning (Weeks 1-2)**
- Conducted PCOS domain research and competitive analysis
- Defined user personas and created detailed user stories
- Selected technology stack (Node.js, MongoDB, Python ML, OpenAI API)

✅ **Architecture & Design (Weeks 3-4)**
- Designed complete system architecture with three core modules:
  - PCOS-Detection (ML risk prediction)
  - Moodie Journal (sentiment analysis)
  - Foodie Chatbot (AI nutritionist)
- Created database schema for Users, Posts, and ChatLogs
- Defined RESTful API endpoints structure
- Designed UI/UX wireframes 

✅ **UI Prototypes (Ahead of Schedule)**
- Built 4 working HTML pages: Home, Signup, Login, Dashboard
- Implemented responsive design with Bootstrap 5
- Added interactive features (form validation, password strength indicator)
- Created consistent design system with gradient themes

---

## 2. Challenges - Issues & Design Decisions

**Challenge 1: Module Integration Complexity**
- *Issue:* Three distinct modules (ML, sentiment analysis, chatbot) require different tech stacks
- *Decision:* Designed microservices-style architecture where Python ML models communicate with Node.js backend via REST APIs

**Challenge 2: UI/UX for Sensitive Health Data**
- *Issue:* PCOS is a sensitive topic requiring empathetic design
- *Decision:* Used warm color palette (pink/blue gradients), non-clinical language, and reassuring iconography

**Challenge 3: Real-time Chatbot Performance**
- *Issue:* OpenAI API calls may have latency
- *Decision:* Will implement loading states, conversation caching, and typing indicators in frontend

---

## 3. Blockers - Current Limitations

**No Critical Blockers** - Project is on schedule

*Minor Considerations:*
- Dataset for PCOS prediction model needs to be sourced and cleaned 
- OpenAI API costs need to be managed - will implement rate limiting
- MongoDB Atlas setup pending 

---

## 4. TODO - Next Milestones

**Phase 1: ML Model Development (Weeks 5-6)**
- **Target Date:** February 8, 2026
- **Tasks:**
  - Source PCOS dataset (Kaggle/UCI)
  - Clean and preprocess data
  - Train Random Forest classifier
  - Achieve 83%+ accuracy
  - Create model serving API endpoint
- **Deliverables:** Trained model (.pkl file), model API script, accuracy report
- **Evaluation:** Model accuracy metrics, confusion matrix, validation tests

**Phase 2: Backend Development (Weeks 7-8)**
- **Target Date:** February 22, 2026
- **Tasks:**
  - Set up Express.js server and MongoDB
  - Implement JWT authentication
  - Build user registration/login APIs
  - Create journal entry CRUD operations
  - Integrate OpenAI API for chatbot
- **Deliverables:** Working REST API, Postman test collection
- **Evaluation:** All API endpoints functional, authentication working

**Phase 3: Frontend Integration (Weeks 9-10)**
- **Target Date:** March 8, 2026
- **Tasks:**
  - Convert HTML prototypes to EJS templates
  - Connect frontend to backend APIs
  - Implement dynamic data rendering
  - Add AJAX for smooth UX
- **Deliverables:** Full-stack working application
- **Evaluation:** Complete user flow from signup to feature usage

---

## 5. Checkpoint Meeting Notes

**Meeting Date:** January 25, 2026

### Feedback Received:
- *(To be filled after meeting)*

### Changes to Plan:
- *(To be filled after meeting)*

### Questions Asked:
- *(To be filled after meeting)*

### Action Items:
- *(To be filled after meeting)*

---

**Status:** ✅ On Track | 100% of planned tasks for Weeks 1-4 completed  
**Next Checkpoint:** Week 7 (Backend completion review)

