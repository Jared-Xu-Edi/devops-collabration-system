
from devopcollab import db
from devopcollab.models import BlogPost, User
if __name__ == '__main__':
    # all_requests = BlogPost.query.all() # list of all requests in table
    # print(all_requests)
    # print('\n\n')
    # all_users = User.query.all() # list of all requests in table
    # print(all_users)

    # ----- set non_admin user -----
    # for i in range(8):
    #     print(i+1)
    #     non_admin_user = User.query.get(i+1)
    #     non_admin_user.is_admin = False
    #     db.session.add(non_admin_user)
    #     db.session.commit()

    admin_user = User.query.get(1)
    admin_user.is_admin = True
    db.session.add(admin_user)
    db.session.commit()
    # post = BlogPost.query.get(8)
    # post.effort_hour=0
    # db.session.add(post)
    # db.session.commit()
    # filters = {BlogPost.devops_onwer == 'Iron.Man'}
    # black_request=BlogPost.query.filter(*filters)
    # print(black_request)