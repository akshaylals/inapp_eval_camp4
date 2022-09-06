from flask import Blueprint, render_template, request, abort, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash

from apps import login_manager
from .models import Comments, Users, Blogs
from .database import db

bp = Blueprint(
    'root', __name__,
)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@bp.route('/')
def blogs():
    rowsPerPage = request.args.get('rows', 10, type=int)
    users = {}
    for u in Users.query.all():
        users[u.id] = u
    page = request.args.get('page', 1, type=int)
    return render_template('pages/home.html', blogs=Blogs.query.order_by(Blogs.id.desc()).paginate(page=page, per_page=rowsPerPage), users=users)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('root.login'))

@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('root.blogs'))

    return render_template("pages/login.html")


@bp.route('/blog/<int:id>', methods=['GET', 'POST'])
def blog(id):
    if request.method == 'POST':
        db.session.add(Comments(request.form.get('comment'), current_user.id, id))
        db.session.commit()
    users = {}
    for u in Users.query.all():
        users[u.id] = u
    try:
        blog = Blogs.query.filter_by(id=id).first()
        comments = Comments.query.filter_by(blog=id)
        return render_template('pages/blog.html', blog=blog, comments=comments, users=users)
    except:
        abort(404)
