from django.db import models


# Create your models here.
#about
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    about_img = models.ImageField(upload_to = "about/")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return self.short_description
    

#Skills
class Skills(models.Model):
    skill_name = models.TextField()
    
    def __str__(self):
        return self.skill_name
    


#My Projects
class My_projects(models.Model):
    title = models.TextField()
    project_img = models.ImageField(upload_to="projects/")
    project_link = models.URLField(max_length=200, blank=True, null=True)  # New field for project link

    def __str__(self):
        return self.title
    

#contact
class Contact(models.Model):
    email = models.EmailField()
    linkedin = models.URLField(max_length=200, blank=True, null=True)  # For LinkedIn URL
    github = models.URLField(max_length=200, blank=True, null=True)    # For GitHub URL
    location = models.CharField(max_length=255, blank=True, null=True)  # For location text
    

    def __str__(self):
        return self.email