<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, session
import os

# HeartHealthChecker Class - All logic in one file


class HeartHealthChecker:
    """Class to analyze heart health based on various parameters"""

    def __init__(self):
        self.risk_factors = []
        self.risk_score = 0

    def check_blood_pressure(self, systolic, diastolic):
        """Check blood pressure and return status"""
        if systolic < 120 and diastolic < 80:
            return "Normal", 0
        elif systolic < 130 and diastolic < 80:
            return "Elevated", 1
        elif systolic < 140 or diastolic < 90:
            return "High Blood Pressure (Stage 1)", 2
        elif systolic < 180 or diastolic < 120:
            return "High Blood Pressure (Stage 2)", 3
        else:
            return "Hypertensive Crisis", 4

    def check_heart_rate(self, heart_rate, age):
        """Check if heart rate is normal"""
        if age < 18:
            normal_range = (60, 100)
        elif age < 60:
            normal_range = (60, 100)
        else:
            normal_range = (60, 90)

        if heart_rate < normal_range[0]:
            return "Low (Bradycardia)", 1
        elif heart_rate > normal_range[1]:
            return "High (Tachycardia)", 2
        else:
            return "Normal", 0

    def check_cholesterol(self, cholesterol):
        """Check cholesterol level"""
        if cholesterol < 200:
            return "Desirable", 0
        elif cholesterol < 240:
            return "Borderline High", 1
        else:
            return "High", 2

    def calculate_risk_score(self, age, gender, smoker, exercise):
        """Calculate overall risk score"""
        score = 0

        if age > 45 and gender == 'male':
            score += 1
        elif age > 55 and gender == 'female':
            score += 1

        if age > 65:
            score += 1

        if smoker:
            score += 2

        if exercise == 'none':
            score += 2
        elif exercise == 'light':
            score += 1
        elif exercise == 'moderate':
            score += 0
        else:
            score -= 1

        return max(0, score)

    def get_health_status(self, total_score):
        """Determine overall health status"""
        if total_score <= 2:
            return {
                'status': 'Excellent',
                'color': 'green',
                'message': 'Your heart health appears to be in great shape! Keep up the good work.',
                'emoji': '💚'
            }
        elif total_score <= 5:
            return {
                'status': 'Good',
                'color': 'lightgreen',
                'message': 'Your heart health is generally good, but there\'s room for improvement.',
                'emoji': '✅'
            }
        elif total_score <= 8:
            return {
                'status': 'Fair',
                'color': 'orange',
                'message': 'Your heart health needs attention. Consider lifestyle changes.',
                'emoji': '⚠️'
            }
        elif total_score <= 12:
            return {
                'status': 'At Risk',
                'color': 'darkorange',
                'message': 'You have several risk factors. Please consult a healthcare provider.',
                'emoji': '⚠️'
            }
        else:
            return {
                'status': 'High Risk',
                'color': 'red',
                'message': 'You have significant risk factors. Seek medical attention soon.',
                'emoji': '🚨'
            }

    def analyze_heart_health(self, age, gender, systolic_bp, diastolic_bp,
                             heart_rate, cholesterol, smoker, exercise):
        """Main analysis function"""

        bp_status, bp_score = self.check_blood_pressure(
            systolic_bp, diastolic_bp)
        hr_status, hr_score = self.check_heart_rate(heart_rate, age)
        chol_status, chol_score = self.check_cholesterol(cholesterol)
        lifestyle_score = self.calculate_risk_score(
            age, gender, smoker, exercise)

        total_score = bp_score + hr_score + chol_score + lifestyle_score

        health_status = self.get_health_status(total_score)

        result = {
            'total_score': total_score,
            'health_status': health_status,
            'blood_pressure': {
                'status': bp_status,
                'values': f"{systolic_bp}/{diastolic_bp} mmHg",
                'score': bp_score
            },
            'heart_rate': {
                'status': hr_status,
                'value': f"{heart_rate} bpm",
                'score': hr_score
            },
            'cholesterol': {
                'status': chol_status,
                'value': f"{cholesterol} mg/dL",
                'score': chol_score
            },
            'lifestyle': {
                'smoker': smoker,
                'exercise': exercise,
                'score': lifestyle_score
            },
            'recommendations': self.get_recommendations(total_score, bp_score,
                                                        hr_score, chol_score,
                                                        smoker, exercise)
        }

        return result

    def get_recommendations(self, total_score, bp_score, hr_score,
                            chol_score, smoker, exercise):
        """Generate personalized recommendations"""
        recommendations = []

        if bp_score > 1:
            recommendations.append("Monitor your blood pressure regularly")
            recommendations.append("Reduce sodium intake in your diet")

        if hr_score > 0:
            recommendations.append("Discuss your heart rate with a doctor")

        if chol_score > 0:
            recommendations.append("Reduce saturated fats in your diet")
            recommendations.append("Increase fiber intake")

        if smoker:
            recommendations.append("Consider a smoking cessation program")

        if exercise in ['none', 'light']:
            recommendations.append(
                "Aim for at least 150 minutes of moderate exercise per week")

        if total_score > 8:
            recommendations.append(
                "Schedule a comprehensive health checkup with your doctor")

        if not recommendations:
            recommendations.append("Maintain your current healthy lifestyle")
            recommendations.append("Continue regular health checkups")

        return recommendations


# Flask Application
app = Flask(__name__)
app.secret_key = '36LcSOovnxs66JiMU35aKAOKYrp_7Jg6oyz34g193aCPWdqK1'

# Initialize the health checker
health_checker = HeartHealthChecker()


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/form')
def form():
    """Heart check form page"""
    return render_template('form.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    """Process form data and show results"""
    try:
        # Get form data
        name = request.form.get('name', 'User')
        age = int(request.form.get('age', 0))
        gender = request.form.get('gender', 'other')
        systolic_bp = int(request.form.get('systolic_bp', 0))
        diastolic_bp = int(request.form.get('diastolic_bp', 0))
        heart_rate = int(request.form.get('heart_rate', 0))
        cholesterol = int(request.form.get('cholesterol', 0))
        smoker = request.form.get('smoker', 'no') == 'yes'
        exercise = request.form.get('exercise', 'none')

        # Calculate health status
        result = health_checker.analyze_heart_health(
            age=age,
            gender=gender,
            systolic_bp=systolic_bp,
            diastolic_bp=diastolic_bp,
            heart_rate=heart_rate,
            cholesterol=cholesterol,
            smoker=smoker,
            exercise=exercise
        )

        # Store in session
        session['result'] = result
        session['name'] = name

        return render_template('result.html', result=result, name=name)

    except Exception as e:
        return f"Error: {str(e)}", 400


@app.route('/tips')
def tips():
    """Health tips page"""
    return render_template('tips.html')


@app.route('/reset')
def reset():
    """Clear session and return to home"""
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
=======
from flask import Flask, render_template, request, redirect, url_for, session
import os

# HeartHealthChecker Class - All logic in one file


class HeartHealthChecker:
    """Class to analyze heart health based on various parameters"""

    def __init__(self):
        self.risk_factors = []
        self.risk_score = 0

    def check_blood_pressure(self, systolic, diastolic):
        """Check blood pressure and return status"""
        if systolic < 120 and diastolic < 80:
            return "Normal", 0
        elif systolic < 130 and diastolic < 80:
            return "Elevated", 1
        elif systolic < 140 or diastolic < 90:
            return "High Blood Pressure (Stage 1)", 2
        elif systolic < 180 or diastolic < 120:
            return "High Blood Pressure (Stage 2)", 3
        else:
            return "Hypertensive Crisis", 4

    def check_heart_rate(self, heart_rate, age):
        """Check if heart rate is normal"""
        if age < 18:
            normal_range = (60, 100)
        elif age < 60:
            normal_range = (60, 100)
        else:
            normal_range = (60, 90)

        if heart_rate < normal_range[0]:
            return "Low (Bradycardia)", 1
        elif heart_rate > normal_range[1]:
            return "High (Tachycardia)", 2
        else:
            return "Normal", 0

    def check_cholesterol(self, cholesterol):
        """Check cholesterol level"""
        if cholesterol < 200:
            return "Desirable", 0
        elif cholesterol < 240:
            return "Borderline High", 1
        else:
            return "High", 2

    def calculate_risk_score(self, age, gender, smoker, exercise):
        """Calculate overall risk score"""
        score = 0

        if age > 45 and gender == 'male':
            score += 1
        elif age > 55 and gender == 'female':
            score += 1

        if age > 65:
            score += 1

        if smoker:
            score += 2

        if exercise == 'none':
            score += 2
        elif exercise == 'light':
            score += 1
        elif exercise == 'moderate':
            score += 0
        else:
            score -= 1

        return max(0, score)

    def get_health_status(self, total_score):
        """Determine overall health status"""
        if total_score <= 2:
            return {
                'status': 'Excellent',
                'color': 'green',
                'message': 'Your heart health appears to be in great shape! Keep up the good work.',
                'emoji': '💚'
            }
        elif total_score <= 5:
            return {
                'status': 'Good',
                'color': 'lightgreen',
                'message': 'Your heart health is generally good, but there\'s room for improvement.',
                'emoji': '✅'
            }
        elif total_score <= 8:
            return {
                'status': 'Fair',
                'color': 'orange',
                'message': 'Your heart health needs attention. Consider lifestyle changes.',
                'emoji': '⚠️'
            }
        elif total_score <= 12:
            return {
                'status': 'At Risk',
                'color': 'darkorange',
                'message': 'You have several risk factors. Please consult a healthcare provider.',
                'emoji': '⚠️'
            }
        else:
            return {
                'status': 'High Risk',
                'color': 'red',
                'message': 'You have significant risk factors. Seek medical attention soon.',
                'emoji': '🚨'
            }

    def analyze_heart_health(self, age, gender, systolic_bp, diastolic_bp,
                             heart_rate, cholesterol, smoker, exercise):
        """Main analysis function"""

        bp_status, bp_score = self.check_blood_pressure(
            systolic_bp, diastolic_bp)
        hr_status, hr_score = self.check_heart_rate(heart_rate, age)
        chol_status, chol_score = self.check_cholesterol(cholesterol)
        lifestyle_score = self.calculate_risk_score(
            age, gender, smoker, exercise)

        total_score = bp_score + hr_score + chol_score + lifestyle_score

        health_status = self.get_health_status(total_score)

        result = {
            'total_score': total_score,
            'health_status': health_status,
            'blood_pressure': {
                'status': bp_status,
                'values': f"{systolic_bp}/{diastolic_bp} mmHg",
                'score': bp_score
            },
            'heart_rate': {
                'status': hr_status,
                'value': f"{heart_rate} bpm",
                'score': hr_score
            },
            'cholesterol': {
                'status': chol_status,
                'value': f"{cholesterol} mg/dL",
                'score': chol_score
            },
            'lifestyle': {
                'smoker': smoker,
                'exercise': exercise,
                'score': lifestyle_score
            },
            'recommendations': self.get_recommendations(total_score, bp_score,
                                                        hr_score, chol_score,
                                                        smoker, exercise)
        }

        return result

    def get_recommendations(self, total_score, bp_score, hr_score,
                            chol_score, smoker, exercise):
        """Generate personalized recommendations"""
        recommendations = []

        if bp_score > 1:
            recommendations.append("Monitor your blood pressure regularly")
            recommendations.append("Reduce sodium intake in your diet")

        if hr_score > 0:
            recommendations.append("Discuss your heart rate with a doctor")

        if chol_score > 0:
            recommendations.append("Reduce saturated fats in your diet")
            recommendations.append("Increase fiber intake")

        if smoker:
            recommendations.append("Consider a smoking cessation program")

        if exercise in ['none', 'light']:
            recommendations.append(
                "Aim for at least 150 minutes of moderate exercise per week")

        if total_score > 8:
            recommendations.append(
                "Schedule a comprehensive health checkup with your doctor")

        if not recommendations:
            recommendations.append("Maintain your current healthy lifestyle")
            recommendations.append("Continue regular health checkups")

        return recommendations


# Flask Application
app = Flask(__name__)
app.secret_key = '36LcSOovnxs66JiMU35aKAOKYrp_7Jg6oyz34g193aCPWdqK1'

# Initialize the health checker
health_checker = HeartHealthChecker()


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/form')
def form():
    """Heart check form page"""
    return render_template('form.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    """Process form data and show results"""
    try:
        # Get form data
        name = request.form.get('name', 'User')
        age = int(request.form.get('age', 0))
        gender = request.form.get('gender', 'other')
        systolic_bp = int(request.form.get('systolic_bp', 0))
        diastolic_bp = int(request.form.get('diastolic_bp', 0))
        heart_rate = int(request.form.get('heart_rate', 0))
        cholesterol = int(request.form.get('cholesterol', 0))
        smoker = request.form.get('smoker', 'no') == 'yes'
        exercise = request.form.get('exercise', 'none')

        # Calculate health status
        result = health_checker.analyze_heart_health(
            age=age,
            gender=gender,
            systolic_bp=systolic_bp,
            diastolic_bp=diastolic_bp,
            heart_rate=heart_rate,
            cholesterol=cholesterol,
            smoker=smoker,
            exercise=exercise
        )

        # Store in session
        session['result'] = result
        session['name'] = name

        return render_template('result.html', result=result, name=name)

    except Exception as e:
        return f"Error: {str(e)}", 400


@app.route('/tips')
def tips():
    """Health tips page"""
    return render_template('tips.html')


@app.route('/reset')
def reset():
    """Clear session and return to home"""
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
>>>>>>> 18b9581d947a0f2fec3b9c1c32e40ee5f034639e
