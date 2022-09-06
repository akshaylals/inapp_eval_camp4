def deploy():
    from apps import create_app
    from apps.database import db
    from apps.models import Users, Blogs, Comments

    app = create_app()
    app.app_context().push()
    db.init_app(app)
    db.create_all()

def dummy():
    from werkzeug.security import generate_password_hash
    from apps import create_app
    from apps.database import db
    from apps.models import Users, Blogs, Comments

    app = create_app()
    app.app_context().push()

    db.session.add(Users('user', 'abc', generate_password_hash('user123'), 'user@foo'))
    db.session.add(Users('user', 'def', generate_password_hash('user123'), 'user@fee'))
    db.session.commit()


    db.session.add(Blogs(
        'lorem ipsum',
        'Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum non facere aperiam fugiat dolor provident dolores quaerat. Natus architecto officia maxime doloribus suscipit esse aperiam. Molestias beatae nemo est quis?',
        1
    ))
    db.session.add(Blogs(
        'lorem ipsum 2',
        'Asperiores cupiditate optio, doloremque aliquid, maiores repellendus earum possimus voluptates ea cum perferendis eveniet autem minus nisi pariatur quia. Fuga expedita totam nemo repudiandae soluta saepe natus non nulla nihil?',
        2
    ))
    db.session.commit() 


    db.session.add(Comments(
        'great',
        2,
        1
    ))
    db.session.commit()

    

if __name__ == '__main__':
    deploy()
    dummy()