from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

def index(request):
    bank=bankcustomer.objects.all()
    context={'bankcustomer':bank}
    return render(request,'index.html',context)

@csrf_protect
def transfer(request,slug):
    bank=bankcustomer.objects.all().filter(~Q(slug=slug))

    presentcustomer=get_object_or_404(bankcustomer,slug=slug)
    print(presentcustomer)
    context={'bankcustomer':bank,'presentcustomer':presentcustomer}
    if request.method=="POST":
        context['transfer']=''
        answer = request.POST['dropdown']
        
        TransferTo=get_object_or_404(bankcustomer,AccountNumber=answer)
       
        context['transfer']=TransferTo
        FromAccount=presentcustomer.AccountNumber
        ToAccount=request.POST['dropdown']
        AmountSent=request.POST.get('AmountSent')
        Remarks=request.POST.get('Remarks')
        print(''==AmountSent)
        if FromAccount!=ToAccount and AmountSent.isdigit() :
            if  presentcustomer.Balance>int(AmountSent):
                Trans=transferdetails(
                    FromAccount=FromAccount,
                    ToAccount=ToAccount,
                    AmountSent=AmountSent,
                    Remarks=Remarks
                )
                Trans.save()
                return redirect("/ReviewOfTransfer")
            else:
                messages.warning(request, 'Insufficent Balance Please Check It')
        
        else:
            if not AmountSent.isdigit() and not AmountSent=='' :
                messages.error(request, 'Please See the details you have Entered')
            

    return render(request,'transfer.html',context)

@csrf_protect
def reviewoftransfer(request):

    transferdetail=transferdetails.objects.latest('date')
    Sender=get_object_or_404(bankcustomer,AccountNumber=transferdetail.FromAccount)
    Reciver=get_object_or_404(bankcustomer,AccountNumber=transferdetail.ToAccount)
    context={'transferdetail':transferdetail,'Reciver':Reciver,'Sender':Sender}
    if request.method=="POST":
        if request.POST.get("submit")=="Submit":
            Reciver.Balance+=transferdetail.AmountSent
            Reciver.save()
            Sender.Balance-=transferdetail.AmountSent
            Sender.save()
            messages.warning(request,'RS {} has been sent to {}({}{}) from {}({}{})'.format(transferdetail.AmountSent,Reciver.AccountNumber,Reciver.firstname,Reciver.lastName,Sender.AccountNumber,Sender.firstname,Sender.lastName))

            
            return redirect('/')
            
        if request.POST.get("cancel")=="Cancel":
            messages.error(request,'Transaction Failed')
            return redirect('/')

    return render(request,'reviewoftransfer.html',context)


def Transaction(request):
    TransferredSent=transferdetails.objects.all()
    context={'TransferredSent':TransferredSent}
    return render(request,"transations.html",context)



