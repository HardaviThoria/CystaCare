# Backend Source Code




 Planned Structure

```
backend/
├── models/
│   ├── User.js
│   ├── Post.js
│   └── ChatLog.js
├── routes/
│   ├── auth.js
│   ├── journal.js
│   ├── chat.js
│   └── prediction.js
├── controllers/
│   ├── authController.js
│   ├── journalController.js
│   └── chatController.js
├── middleware/
│   ├── auth.js
│   └── errorHandler.js
├── config/
│   └── database.js
├── utils/
│   └── helpers.js
├── app.js
└── server.js
```

---

## Technology

- **Node.js** - Runtime environment
- **Express.js** - Web framework
- **MongoDB** - Database
- **Mongoose** - ODM
- **JWT** - Authentication
- **bcrypt** - Password hashing

---

## API Endpoints (Planned)

### Authentication
- `POST /api/auth/signup` - Register user
- `POST /api/auth/login` - Login user
- `GET /api/auth/logout` - Logout user

### Journal
- `GET /api/journal` - Get all entries
- `POST /api/journal` - Create entry
- `PUT /api/journal/:id` - Update entry
- `DELETE /api/journal/:id` - Delete entry

### Chatbot
- `POST /api/chat` - Send message

### Prediction
- `POST /api/predict` - Submit health data

---

## Development Timeline

- **Week 7:** Models and database setup
- **Week 8:** Routes and authentication
- **Integration:** Connect with frontend and ML models

---

**Current Phase:** Architecture Planning  
**Next Milestone:** Begin backend scaffolding 

