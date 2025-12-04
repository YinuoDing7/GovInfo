from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.admin import bp
from app.models import User, Role, SystemSetting
from functools import wraps

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role.name != 'Admin':
            flash('You do not have permission to access this page.')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/users')
@login_required
@admin_required
def users():
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@bp.route('/user/add', methods=['POST'])
@login_required
@admin_required
def add_user():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    role_id = request.form.get('role_id')
    
    if User.query.filter_by(username=username).first():
        flash('Username already exists.')
        return redirect(url_for('admin.users'))
        
    user = User(username=username, email=email, role_id=role_id)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    flash('User added successfully.')
    return redirect(url_for('admin.users'))

@bp.route('/user/delete/<int:id>')
@login_required
@admin_required
def delete_user(id):
    user = User.query.get_or_404(id)
    if user == current_user:
        flash('Cannot delete yourself.')
        return redirect(url_for('admin.users'))
        
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully.')
    return redirect(url_for('admin.users'))

@bp.route('/settings', methods=['GET', 'POST'])
@login_required
@admin_required
def settings():
    if request.method == 'POST':
        app_name = request.form.get('app_name')
        # Update or create setting
        setting = SystemSetting.query.filter_by(key='app_name').first()
        if not setting:
            setting = SystemSetting(key='app_name')
            db.session.add(setting)
        setting.value = app_name
        db.session.commit()
        flash('Settings updated.')
        return redirect(url_for('admin.settings'))
        
    app_name_setting = SystemSetting.query.filter_by(key='app_name').first()
    app_name = app_name_setting.value if app_name_setting else 'GovInfo System'
    return render_template('admin/settings.html', app_name=app_name)
