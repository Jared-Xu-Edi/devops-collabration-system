from flask import render_template,request,Blueprint
from devopcollab.models import BlogPost

core = Blueprint('core',__name__)

@core.route('/')
def index():
    '''
    This is the home page view. Notice how it uses pagination to show a limited
    number of posts by limiting its query size and then calling paginate.
    '''
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=100)
    return render_template('index.html',blog_posts=blog_posts)
# def index():
#     return render_template('ajax_table.html', title='Ajax Table')

@core.route('/info')
def info():
    '''
    Example view of any other "core" page. Such as a info page, about page,
    contact page. Any page that doesn't really sync with one of the models.
    '''
    return render_template('info.html')

# @core.route('/user_mgr')
# def info():
#     '''
#     Example view of any other "core" page. Such as a info page, about page,
#     contact page. Any page that doesn't really sync with one of the models.
#     '''
#     return render_template('user_mgr.html')
