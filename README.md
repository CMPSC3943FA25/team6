# Heart Check Website

A Flask-based web application for assessing heart health status based on vital signs and lifestyle factors.

## Team Members & Roles

- **Prasanna Shah** - Product Owner (Backend & Coordination)
- **Manish Malla** - Scrum Master (Project Management & Frontend)
- **Prasiddhi Chapagain** - Developer (Backend Features)
- **Rabindra Karki** - Developer (Database & Integration)
- **Samiran Dhakal** - Designer (Frontend Design)
- **Aayush** - Designer (Styling & Interactivity)
- **Ashley** - Designer (Content & Usability)

## Features

- ✅ User-friendly input form for health metrics
- ✅ Instant heart health assessment
- ✅ Personalized health recommendations
- ✅ Educational health tips page
- ✅ Responsive design for all devices

## Installation Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Git

### Setup Steps

1. **Clone or download the project:**
   ```bash
   cd heart_check_web
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment:**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **Mac/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install flask
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Open in browser:**
   ```
   http://127.0.0.1:5000
   ```

## Project Structure

```
heart_check_web/
│
├── app.py                 # Main Flask application
├── README.md             # This file
│
├── models/
│   └── health_logic.py   # Heart health calculation logic
│
├── templates/            # HTML templates
│   ├── index.html        # Home page
│   ├── form.html         # Input form
│   ├── result.html       # Results page
│   └── tips.html         # Health tips
│
├── static/
│   ├── css/
│   │   └── style.css     # Stylesheet
│   ├── images/           # Image assets (if any)
│   └── js/               # JavaScript files (if any)
│
└── data/                 # Database/data storage (future use)
```

## How to Use

1. **Home Page**: Click "Start Heart Check" to begin
2. **Form Page**: Fill in your health information accurately
3. **Results Page**: View your heart health status and risk score
4. **Tips Page**: Read personalized recommendations and general health tips

## Health Metrics Used

- Age and Gender
- Blood Pressure (Systolic/Diastolic)
- Resting Heart Rate
- Total Cholesterol
- Smoking Status
- Exercise Frequency

## Risk Categories

- **Excellent** (0-2 points): Great heart health
- **Good** (3-5 points): Generally healthy
- **Fair** (6-8 points): Needs attention
- **At Risk** (9-12 points): Multiple risk factors
- **High Risk** (13+ points): Seek medical attention

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3
- **Styling**: Custom CSS with responsive design
- **Future**: SQLite database (optional)

## Development Workflow

1. **Foundation Setup** - Prasanna & Manish
2. **Backend Logic** - Prasiddhi & Rabindra
3. **Frontend Design** - Samiran & Aayush
4. **Content & Testing** - Ashley
5. **Integration** - All team members

## Git Workflow

```bash
# Create feature branch
git checkout -b feature-name

# Make changes and commit
git add .
git commit -m "Description of changes"

# Push to GitHub
git push origin feature-name

# Create pull request on GitHub
```

## Troubleshooting

### Port Already in Use
```bash
# Change port in app.py:
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Module Not Found
```bash
# Make sure virtual environment is activated
# Reinstall Flask
pip install flask
```

### Template Not Found
- Ensure templates are in the `templates/` folder
- Check file names match exactly (case-sensitive)

## Future Enhancements

- [ ] User login/registration system
- [ ] Save and track health history
- [ ] SQLite database integration
- [ ] Export results as PDF
- [ ] Email health reports
- [ ] Multi-language support

## Disclaimer

⚠️ This application is for educational purposes only and should not replace professional medical advice. Always consult with a healthcare provider for health concerns.

## License

This project is for educational use as part of a university course project.

## Contact

For questions or issues, contact the team through your course communication channels.

---

