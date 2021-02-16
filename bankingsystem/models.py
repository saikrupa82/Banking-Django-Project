from django.db import models
from datetime import *

class bankcustomer(models.Model):
    firstname=models.CharField(max_length=100,blank=False)
    EmailId=models.CharField(max_length=200)
    lastName=models.CharField(max_length=200,blank=True)
    Balance=models.IntegerField(blank=False)
    AccountNumber=models.IntegerField(blank=False,primary_key=True)
    slug = models.SlugField(null=False,unique=True)
    def save(self, *args, **kwargs):
        test=''
        if not self.slug:
            for i in self.AccountNumber:
                if i==' ':
                    test+=i
            self.slug = slugify(test)
        super(bankcustomer,self).save()
    def get_absolute_url(self):
        return reverse('bankcustomer', kwargs={'slug': self.slug})


class transferdetails(models.Model):
    uniqueid=models.CharField(max_length=100,blank=False,primary_key=True)
    FromAccount=models.IntegerField(blank=False)
    ToAccount=models.IntegerField(blank=False)
    AmountSent=models.IntegerField(blank=False)
    Remarks=models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    def save(self, *args, **kwargs):
        test='BXNT'
        today = date.today()
        now = datetime.now().time()
        if not self.uniqueid:
            for i in str(self.FromAccount)[-3:]:
                    test+=i
            for i in str(self.ToAccount)[-3:]:
                    test+=i
            test+=''.join(str(today).split('-'))+''.join(str(now).split(':'))[:6]
            self.uniqueid = test
        super(transferdetails,self).save()

