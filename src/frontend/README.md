# Frontend Source Code

**Status:** UI Prototypes Created - Week 3-4  
**Development Planned:** Week 9-10

---

## Current Pages (Prototypes)

✅ **Completed UI Prototypes:**
1. `home.html` - Landing page with hero section and features
2. `signup.html` - User registration form with validation
3. `login.html` - Authentication page with password toggle
4. `dashboard.html` - Main user dashboard with module cards

---

## How to View Prototypes

Simply open any HTML file in your browser:

```bash
# Navigate to frontend folder
cd src/frontend

# Open in browser (Mac)
open home.html

# Or just double-click the files
```

**Live Demo Flow:**
```
home.html → signup.html → login.html → dashboard.html
```

---

## Planned Structure (Full Implementation)

```
frontend/
├── public/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── main.js
│   └── images/
│       └── logo.png
├── views/
│   ├── partials/
│   │   ├── header.ejs
│   │   └── footer.ejs
│   ├── home.ejs
│   ├── signup.ejs
│   ├── login.ejs
│   ├── dashboard.ejs
│   ├── journal.ejs
│   ├── compose.ejs
│   ├── chat.ejs
│   └── predict.ejs
└── README.md (this file)
```

---

## Technology Used

- **HTML5** - Semantic markup
- **CSS3** - Custom styling with CSS variables
- **Bootstrap 5** - Responsive framework (CDN)
- **Bootstrap Icons** - Icon library
- **JavaScript (ES6+)** - Client-side interactivity
- **EJS** - Server-side templating (planned for backend integration)

---

## Design Features

### ✨ Implemented Features:
- ✅ Responsive mobile-first design
- ✅ Modern gradient backgrounds
- ✅ Interactive hover effects
- ✅ Form validation (client-side)
- ✅ Password strength indicator
- ✅ Password visibility toggle
- ✅ Smooth animations
- ✅ Accessible color contrast (WCAG 2.1)

### Color Palette:
- **Primary Pink:** #FF69B4
- **Secondary Blue:** #4A90E2
- **Accent Green:** #50C878
- **Background:** #F5F5F5
- **Text:** #333333

---

## Page Details

### 1. Home Page (`home.html`)
- Hero section with gradient background
- Three feature cards (Predict, Moodie, Foodie)
- Stats section
- About section
- Responsive navigation

### 2. Signup Page (`signup.html`)
- Full registration form
- Real-time password strength indicator
- Terms & conditions checkbox
- Social login placeholders
- Form validation

### 3. Login Page (`login.html`)
- Email/password authentication
- Password visibility toggle
- Remember me checkbox
- Forgot password link
- Demo credentials info

### 4. Dashboard (`dashboard.html`)
- Fixed sidebar navigation
- Welcome message with stats
- Three module cards
- Getting started section
- User profile actions

---

## Development Timeline

- ✅ **Week 3-4:** UI Prototypes (Current)
- **Week 7-8:** Backend API development
- **Week 9:** Convert to EJS templates
- **Week 10:** Backend integration and dynamic data
- **Week 11-12:** Connect with ML models and chatbot
- **Integration:** Full-stack functionality

---

## Next Steps (Week 7+)

1. Convert HTML to EJS templates
2. Integrate with Express.js backend
3. Implement actual authentication
4. Connect to MongoDB
5. Add dynamic data rendering
6. Implement AJAX calls for smooth UX

---

## Notes for Professor

These are **static HTML prototypes** demonstrating:
- UI/UX design implementation
- Responsive layout
- Component structure
- User flow

Full backend integration will occur in Week 9-10 after API development (Week 7-8).

---

**Current Phase:** UI Prototyping ✅  
**Next Milestone:** Backend API Development (Week 7-8)

