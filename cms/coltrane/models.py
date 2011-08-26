from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField

from markdown import markdown

import datetime

class Category(models.Model):
    title = models.CharField(max_length=250, help_text="Maximum of 250 characters.")
    slug= models.SlugField(unique=True,help_text="Suggested value automatically generated from title.  Must be unique.")
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['title']
        
    def get_absolute_url(self):
        return "/categories/%s/" % self.slug
    
    
    
    
    def __unicode__(self):
        return self.title

class Entry(models.Model): 
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
                      (LIVE_STATUS, 'Live'),
                      (DRAFT_STATUS, 'Draft'),
                      (HIDDEN_STATUS, 'Hidden'),
                      )  
    # Core Fields 
    title = models.CharField(max_length=250)
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    
    slug = models.SlugField(unique_for_date='pub_date')
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    
    categories = models.ManyToManyField(Category)
    excerpt_html = models.TextField(editable=False,blank=True)
    body_html = models.TextField(editable=False,blank=True)
    
    tags = TagField()
    
    
    
    
    def save(self, force_insert=False,force_update=False):
        self.body_html =  markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save(force_insert, force_update)
        
    class Meta:
        verbose_name_plural = "Entries"
        ordering = ['-pub_date']
        
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/weblog/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)
    