"""
Definition of models.
"""

from django.db import models

# Create your models here.

class FunctionalGroup(models.Model):
    Name = models.CharField(max_length=100, primary_key=True)
    Smarts = models.CharField(max_length = 100)
    inRing = models.BooleanField(default=False)
    URL = models.URLField(max_length = 200)
    Image = models.ImageField


class Reaction(models.Model):
    Name = models.CharField(max_length = 100,  primary_key=True)
    URL = models.URLField(max_length = 200)
    ProductFunctionalGroup = models.ForeignKey('FunctionalGroup', on_delete=models.CASCADE)
    ReactantA = models.fori
    Image = models.ImageField

class Reference(models.Model):
    RISData = models.CharField(max_length = 5000)
    Reaction = models.ForeignKey('Reaction', on_delete=models.CASCADE)
    Type = models.CharField(max_length = 2)
    Title = models.CharField(max_length = 5000)


    #   public string FunctionalGroup { get; }
    #    public string ReactionName { get; }
    #    public string Type { get; }
    #    public string Title { get; }
    #    public string[] Authors
    #    {
    #        get
    #        {
    #            return m_authors.ToArray<string>();
    #        }
    #    }
    #    public string Abstract { get; }
     #   public string AuthorAddress { get; }
     #   public string Journal { get; }
     #   public string Volume { get; }
     #   public string Issue { get; }
     #   public string StartPage { get; }
     #   public string EndPage { get; }
     #   public string Date { get; }
     #   public string URL { get; }
     #   public string doi { get; }
      #  public string PY { get; }
       