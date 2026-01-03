import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Application

app = Flask(__name__)

# ================= CONFIG =================
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_secret_key')

# SQLite (works locally + on Render)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'sqlite:///users.db'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ================= LOGIN MANAGER =================
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# ================= HOME =================
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')


# ================= REGISTER =================
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(
            username=request.form['username'],
            email=request.form['email']
        )
        user.set_password(request.form['password'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


# ================= LOGIN =================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')


# ================= DASHBOARD =================
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        app_item = Application(
            company_name=request.form['company'],
            job_position=request.form['position'],
            status=request.form['status'],
            interview_date=request.form['date'],
            user_id=current_user.id
        )
        db.session.add(app_item)
        db.session.commit()
        return redirect(url_for('dashboard'))

    applications = Application.query.filter_by(user_id=current_user.id).all()

    # -------- STATISTICS --------
    total_apps = len(applications)
    interviews_scheduled = len([a for a in applications if a.status == 'Interview Scheduled'])
    selected = len([a for a in applications if a.status == 'Selected'])
    rejected = len([a for a in applications if a.status == 'Rejected'])

    return render_template(
        'dashboard.html',
        applications=applications,
        username=current_user.username,
        total_apps=total_apps,
        interviews_scheduled=interviews_scheduled,
        selected=selected,
        rejected=rejected
    )


# ================= UPDATE =================
@app.route('/update/<int:id>', methods=['POST'])
@login_required
def update_application(id):
    app_item = Application.query.get_or_404(id)
    if app_item.user_id != current_user.id:
        return redirect(url_for('dashboard'))

    app_item.company_name = request.form['company']
    app_item.job_position = request.form['position']
    app_item.status = request.form['status']
    app_item.interview_date = request.form['date']

    db.session.commit()
    return redirect(url_for('dashboard'))


# ================= DELETE =================
@app.route('/delete/<int:id>')
@login_required
def delete_application(id):
    app_item = Application.query.get_or_404(id)
    if app_item.user_id == current_user.id:
        db.session.delete(app_item)
        db.session.commit()
    return redirect(url_for('dashboard'))


# ================= LOGOUT =================
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
