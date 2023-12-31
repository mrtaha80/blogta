from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import ArticleForm, CommentForm
from .models import Article, Comment


from django.core.mail import send_mail
from django.contrib.auth.models import User

@permission_required('add_article')
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()

            # Get all users
            users = User.objects.all()

            # Send email to each user
            for user in users:
                subject = 'New Article'
                message = f'A new article titled "{form.cleaned_data["title"]}" has been submitted by {request.user.username}.'
                from_email = 'tahaislion@example.com'
                recipient_list = [user.email]
                send_mail(subject, message, from_email, recipient_list)

            return redirect('articles')
    else:
        form = ArticleForm()

    context = {
        'form': form
    }
    return render(request, 'add_article.html', context)


class ArticleDetailView(UserPassesTestMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'

    def test_func(self):
        article = self.get_object()
        return article.published

    def handle_no_permission(self):
        return redirect('login')


class CommentCreateView(UserPassesTestMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_create.html'

    def form_valid(self, form):
        form.instance.article = Article.objects.get(pk=self.kwargs['pk'])
        form.instance.commenter = self.request.user
        return super().form_valid(form)

    def test_func(self):
        article = Article.objects.get(pk=self.kwargs['pk'])
        return article.published

    def handle_no_permission(self):
        return redirect('login')


class CommentUpdateView(UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_update.html'

    def test_func(self):
        comment = self.get_object()
        return comment.commenter == self.request.user

    def handle_no_permission(self):
        return redirect('login')