from django.db import models

class Tag(models.Model):
    """docstring for tags"""
    tag_name=models.CharField(max_length=20,blank=True)
    creat_time=models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.tag_name
        
class BlogManager(models.Manager):
    """docstring for BlogManager"""
    def title_count(self, keyword):
        return self.filter(caption__icontains=keyword).count()

    def tag_count(self, keyword):
        return self.filter(tags__icontains=keyword).count()

    def author_count(self, keyword):
        return self.filter(author__icontains=keyword).count()
        
class Author(models.Model):
    """docstring for author"""
    name=models.CharField(max_length=30)
    email=models.EmailField(blank=True)
    website=models.URLField(blank=True)
    
    def __unicode__(self):
        return u'%s'%(self.name)
        
class Blog(models.Model):
    """docstrin for blog"""
    caption=models.CharField(max_length=50)
    author=models.ForeignKey(Author)
    tags=models.ManyToManyField(Tag,blank=True)
    content=models.TextField()
    publish_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return u'%s %s %s' %(self.caption,self.author,self.publish_time)
    class Meta:
        ordering = ['-publish_time']
        
class Weibo(models.Model):
    massage = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    publish_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.massage
    
