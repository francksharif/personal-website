import os
base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI='postgres://uas0acfa009ii2:p3dc41a82689c919764e8b4c8f825555ab3e18d082c72fccb167907420c389cac@caij57unh724n3.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d2f3h8tbeg4eou'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app/static/uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    WTF_CSRF_ENABLED = True