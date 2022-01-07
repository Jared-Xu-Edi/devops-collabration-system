from flask import render_template,url_for,flash, redirect,request,Blueprint
from flask_login import current_user,login_required
from devopcollab import db
from devopcollab.models import BlogPost
from devopcollab.blog_posts.forms import BlogPostForm, BlogPostFormAdmin

blog_posts = Blueprint('blog_posts',__name__)

@blog_posts.route('/create',methods=['GET','POST'])
@login_required
def create_post():

    if not current_user.is_admin:
        form = BlogPostForm()

        if form.validate_on_submit():

            blog_post = BlogPost(title=form.title.data,
                                text=form.text.data,
                                status=form.status.data,
                                user_id=current_user.id
                                )
            db.session.add(blog_post)
            db.session.commit()
            flash("Blog Post Created")
            return redirect(url_for('core.index'))
    else:
        #is admin
        form = BlogPostFormAdmin(devops_owner='John.Doe',effort_hour=0)
        if form.validate_on_submit():
            blog_post = BlogPost(title=form.title.data,
                                text=form.text.data,
                                status=form.status.data,
                                user_id=current_user.id,
                                devops_owner=form.devops_owner.data,
                                effort_hour=form.effort_hour.data
                                )
            db.session.add(blog_post)
            db.session.commit()
            flash('Post Created by Admin')
            return redirect(url_for('core.index'))

    return render_template('create_post.html',form=form)


# int: makes sure that the blog_post_id gets passed as in integer
# instead of a string so we can look it up later.
@blog_posts.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    # grab the requested blog post by id number or return 404
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog_post.html',title=blog_post.title,
                            date=blog_post.date,post=blog_post
    )

@blog_posts.route("/<int:blog_post_id>/update", methods=['GET', 'POST'])
@login_required
def update(blog_post_id):
    print('update blog: '+str(blog_post_id)+' by '+ current_user.username + ' is_admin:' + str(current_user.is_admin))
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if not current_user.is_admin and blog_post.author != current_user:
        # Forbidden, No Access
        abort(403)
    if not current_user.is_admin:
        form = BlogPostForm()
        if form.validate_on_submit():
            blog_post.title = form.title.data
            blog_post.text = form.text.data
            blog_post.status = form.status.data
            db.session.commit()
            flash('Post Updated')
            return redirect(url_for('blog_posts.blog_post', blog_post_id=blog_post.id))
        # Pass back the old blog post information so they can start again with
        # the old text and title.
        elif request.method == 'GET':
            form.title.data = blog_post.title
            form.text.data = blog_post.text
            form.status.data = blog_post.status

    if current_user.is_admin:
        print('admin path.')
        form = BlogPostFormAdmin(devops_owner='John.Doe',effort_hour=0)
        if form.validate_on_submit():
            blog_post.title = form.title.data
            blog_post.text = form.text.data
            blog_post.status = form.status.data
            blog_post.devops_onwer = form.devops_owner.data
            blog_post.effort_hour = form.effort_hour.data
            print('effort_hour: '+ str(form.effort_hour.data))
            db.session.commit()
            flash('Post Updated')
            return redirect(url_for('blog_posts.blog_post', blog_post_id=blog_post.id))
        # Pass back the old blog post information so they can start again with
        # the old text and title.
        elif request.method == 'GET':
            form.title.data = blog_post.title
            form.text.data = blog_post.text
            form.status.data = blog_post.status
            form.devops_owner.data = blog_post.devops_onwer
            form.effort_hour.data = blog_post.effort_hour if blog_post.effort_hour != None else 0

    return render_template('create_post.html', title='Update',
                           form=form)


@blog_posts.route("/<int:blog_post_id>/delete", methods=['POST'])
@login_required
def delete_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)
    db.session.delete(blog_post)
    db.session.commit()
    flash('Post has been deleted')
    return redirect(url_for('core.index'))

# @blog_posts.route('/api/data')
# def data():
#     return {'data': [user.to_dict() for user in blog_post.query]}
