 User Stories & Use Cases

**Project:** CystaCare  
**Version:** 0.2.0  
**Date:** January 2026

---

 User Personas

 Persona 1: Hardavi (Primary User)
- **Age:** 26
- **Occupation:** Software Engineer
- **Location:** Urban India
- **Tech Savviness:** High
- **Pain Points:** 
  - Irregular periods, unsure if it's PCOS
  - Anxiety about fertility
  - Difficulty maintaining PCOS-friendly diet
  - Lack of emotional support

 Persona 2: Dr. Sharma (Secondary User)
- **Role:** Gynecologist
- **Use Case:** Preliminary screening tool
- **Needs:** Quick risk assessment for patients

---

 User Stories

 Module 1: PCOS-Detection

**US-001:** Risk Assessment
```
As a user concerned about PCOS,
I want to input my health symptoms and get a risk assessment,
So that I can decide whether to consult a doctor.

Acceptance Criteria:
- Form accepts 29+ health parameters
- Results show risk level (High/Medium/Low)
- Recommendations provided based on risk
- Data stored securely
```

**US-002:** View Prediction History
```
As a registered user,
I want to view my previous PCOS assessments,
So that I can track changes over time.
```

---

 Module 2: Moodie (Journal)

**US-003:** Create Journal Entry
```
As a user dealing with PCOS,
I want to write daily journal entries about my feelings,
So that I can track my emotional well-being.

Acceptance Criteria:
- Simple text input interface
- Optional title and image
- Auto-save functionality
- Timestamp recorded
```

**US-004:** View Emotion Analysis
```
As a journaling user,
I want to see what emotions my entries reflect,
So that I can understand my mental health patterns.

Acceptance Criteria:
- 5 emotions detected (Happy, Sad, Angry, Fear, Surprise)
- Visual representation of emotions
- Weekly summary available
```

**US-005:** Search & Filter Entries
```
As a user with multiple journal entries,
I want to search and filter my past entries,
So that I can easily find specific thoughts or periods.
```



 Module 3: Foodie (Chatbot)

**US-006:** Get Recipe Suggestions
```
As a user with PCOS,
I want to ask for PCOS-friendly recipe suggestions,
So that I can maintain a healthy diet.

Acceptance Criteria:
- Natural language input accepted
- Bilingual support (English/Hindi)
- Responses consider PCOS dietary restrictions
- Conversational, empathetic tone
```

**US-007:** Ingredient-Based Recipes
```
As a user with limited ingredients,
I want to tell the chatbot what I have,
So that I can get recipes using those ingredients.
```

**US-008:** Discourage Unhealthy Eating
```
As a user tempted by junk food,
I want the chatbot to discourage unhealthy choices,
So that I stay motivated to eat healthy.
```

---

 Module 4: Authentication

**US-009:** User Registration
```
As a new user,
I want to create an account securely,
So that my health data remains private.

Acceptance Criteria:
- Email validation
- Strong password requirements
- Confirmation email sent
- Terms of service acceptance
```

**US-010:** Secure Login
```
As a returning user,
I want to log in securely,
So that I can access my personalized data.
```



 Use Cases

 UC-001: Complete PCOS Risk Assessment

**Actor:** Hardavi (New User)

**Preconditions:** None

**Flow:**
1. Hardavi visits CystaCare homepage
2. Clicks "PCOS Risk Assessment"
3. Fills health questionnaire (symptoms, cycle info, lifestyle)
4. Submits form
5. ML model processes data
6. Risk score displayed with recommendations
7. Option to create account to save results

**Postconditions:** Risk assessment saved (if registered)



 UC-002: Daily Journaling with Emotion Tracking

**Actor:** Hardavi (Registered User)

**Preconditions:** User is logged in

**Flow:**
1. Hardavi navigates to "Moodie" section
2. Clicks "New Journal Entry"
3. Writes about her day and feelings
4. Clicks "Publish"
5. Sentiment analysis runs automatically
6. Emotions detected and displayed
7. Entry added to journal list

**Postconditions:** Journal stored, emotions analyzed



 UC-003: Get Dinner Recipe Suggestion

**Actor:** Hardavi (Registered User)

**Preconditions:** User is logged in

**Flow:**
1. Hardavi opens "Foodie" chatbot
2. Types: "I have rice and vegetables. What can I make for dinner?"
3. Chatbot processes query via OpenAI
4. Receives PCOS-friendly recipe suggestion
5. Can ask follow-up questions
6. Conversation history maintained

**Postconditions:** Chat log saved



 Feature Priority

 Must Have (MVP)
- ✅ User authentication
- ✅ PCOS risk prediction
- ✅ Basic journaling
- ✅ Sentiment analysis
- ✅ Chatbot integration

 Should Have
- Weekly emotion reports
- Search functionality
- Prediction history
- Profile management

 Could Have
- Song therapy
- Daily challenges
- Community forum
- Admin dashboard

 Won't Have (This Semester)
- Mobile app
- Wearable integration
- Telemedicine



 Acceptance Testing Scenarios

 Scenario 1: End-to-End User Journey
```
Given: A new user visits CystaCare
When: They complete registration, take risk assessment, write a journal, and chat with Foodie
Then: All features work seamlessly and data is stored correctly
```

 Scenario 2: Security Testing
```
Given: An unauthorized user tries to access /user/journal
When: They are not logged in
Then: They are redirected to login page with 401 status
```

 Scenario 3: ML Model Accuracy
```
Given: Test dataset with known PCOS cases
When: Model makes predictions
Then: Accuracy should be ≥ 83%
```



**Document Status:** Draft  
**Last Updated:** January 2026  


