# System Architecture Document

**Project:** CystaCare  
**Version:** 0.3.0  
**Date:** January 2026  
**Status:** Draft - Week 3

---

## 1. Architecture Overview

CystaCare follows a **layered architecture pattern** with clear separation of concerns between presentation, business logic, and data layers.

### 1.1 Architecture Style
- **Pattern:** Layered + Microservices-ready
- **Communication:** RESTful APIs
- **Deployment:** Monolithic initially, scalable to microservices

---

## 2. System Components

### 2.1 Frontend Layer
- **Technology:** HTML5, CSS3, JavaScript, Bootstrap 5
- **Templating:** EJS (Embedded JavaScript)
- **State Management:** Session-based (JWT tokens)
- **Responsive Design:** Mobile-first approach

### 2.2 Backend Layer
- **Framework:** Express.js (Node.js)
- **API Style:** RESTful
- **Middleware:** Body-parser, CORS, Cookie-parser
- **Authentication:** JWT + bcrypt

### 2.3 Database Layer
- **Database:** MongoDB (Document-based NoSQL)
- **ODM:** Mongoose
- **Collections:**
  - Users (authentication data)
  - Posts (journal entries)
  - ChatLogs (chatbot interactions)
  - PredictionHistory (ML predictions)

### 2.4 ML/AI Layer
- **ML Engine:** Python scripts (sklearn)
- **Sentiment Analysis:** text2emotion library
- **Chatbot:** OpenAI GPT-3.5 API
- **Integration:** Python-Node bridge (python-shell)

---

## 3. Data Flow Architecture

### 3.1 PCOS Prediction Flow
```
User Input → Express API → Python ML Script → 
Random Forest Model → Prediction Result → 
MongoDB Storage → User Dashboard
```

### 3.2 Journal & Sentiment Analysis Flow
```
User Journal Entry → Express API → 
MongoDB Storage → Python Sentiment Script → 
Emotion Analysis → Weekly Report Generation
```

### 3.3 Chatbot Flow
```
User Query → Express API → OpenAI API → 
GPT-3.5 Processing → Response → 
MongoDB Log → User Interface
```

---

## 4. Database Schema Design

### 4.1 Users Collection
```javascript
{
  _id: ObjectId,
  name: String,
  email: String (unique),
  password: String (hashed),
  createdAt: Date,
  tokens: [{ token: String }],
  posts: [ObjectId] // References to Posts
}
```

### 4.2 Posts Collection (Journals)
```javascript
{
  _id: ObjectId,
  user: ObjectId (ref: User),
  title: String,
  content: String,
  emotions: {
    happy: Number,
    sad: Number,
    angry: Number,
    fear: Number,
    surprise: Number
  },
  createdAt: Date,
  updatedAt: Date
}
```

### 4.3 ChatLogs Collection
```javascript
{
  _id: ObjectId,
  user: ObjectId (ref: User),
  query: String,
  response: String,
  timestamp: Date
}
```

---

## 5. API Endpoints Design

### 5.1 Authentication Routes
- `POST /user/signup` - User registration
- `POST /user/login` - User authentication
- `GET /user/logout` - Session termination

### 5.2 Journal Routes
- `GET /user/journal` - View all entries
- `POST /post/compose` - Create entry
- `GET /post/posts/:id` - View single entry
- `PUT /post/edit/:id` - Update entry
- `DELETE /post/delete` - Remove entry

### 5.3 Chatbot Routes
- `GET /chatbox` - Chatbot interface
- `POST /api/chatBot` - Send query

### 5.4 Prediction Routes
- `GET /predict` - Prediction form
- `POST /predict` - Submit health data

---

## 6. Security Architecture

### 6.1 Authentication Flow
```
User Login → Validate Credentials → 
Generate JWT Token → Store in httpOnly Cookie → 
Verify on Protected Routes
```

### 6.2 Security Measures
- Password hashing: bcrypt (10 rounds)
- Token-based auth: JWT with secret key
- Cookie security: httpOnly, secure flags
- Input validation: Express-validator
- MongoDB injection prevention: Mongoose ODM

---

## 7. Scalability Considerations

### 7.1 Horizontal Scaling
- Load balancing with NGINX
- Stateless API design
- Session management via JWT

### 7.2 Database Scaling
- MongoDB sharding
- Read replicas for analytics
- Indexing on frequently queried fields

### 7.3 Caching Strategy
- Redis for session management (future)
- API response caching
- Static asset CDN

---

## 8. Technology Justification

| Technology | Justification |
|------------|---------------|
| Node.js | Non-blocking I/O for real-time features |
| MongoDB | Flexible schema for evolving requirements |
| Python | Rich ML/AI ecosystem |
| OpenAI | State-of-art conversational AI |
| JWT | Stateless, scalable authentication |

---

## 9. Development Phases

**Current Phase (Week 3-4):** Architecture Design & Documentation

**Next Steps:**
- Finalize database schema
- Set up development environment
- Create API endpoint specifications
- Begin backend scaffolding

---

**Document Status:** Draft  
**Last Updated:** January 2026

