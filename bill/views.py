from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.contrib import messages
from adduser.models import client, transport
from product.models import product
from bill.models import item, formatt, bill, temp, order
from xhtml2pdf import pisa
from django.template.loader import get_template
from .forms import billgenerator
import datetime
from num2words import num2words


def additem(request):
	if request.user.is_authenticated:
		p = product.objects.all()
		it = item.objects.all()
		if request.method == 'POST':
			pid = request.POST['pid']
			qty = request.POST['qty']
			box = request.POST['box']
			mtr = request.POST['mtr']
			r = request.POST['rate']
			r1 = int(r) / 1.05
			rate = "{:.2f}".format(r1)
			r2 = float(rate)
			total = int(qty) * (r2)

			p1 = product.objects.get(id=pid)

			i = item(product=p1, quantity=qty, rate=rate, box=box, total=total, mtr=mtr)
			i.save()
			return render(request, "additem.html", {'product':p, 'items':it})
		else:
			return render(request, "additem.html", {'product':p, 'items':it})
	else:
		return redirect('/')


def clearlist(request):
	i = item.objects.all()
	i.delete()
	return redirect('/bill/additem/')

def cancel(request):
	i = item.objects.all()
	i.delete()
	return redirect('/')

def delitem(request):
	if request.method == 'POST':
		tid = request.POST['tid']
		t = item.objects.get(id=tid)

		t.delete()
		return redirect('/bill/additem/')
	else:
		return redirect('/bill/additem/')


def render_pdf_view(request):
	if request.user.is_authenticated:
		f = formatt.objects.get(id=1)
		b = bill.objects.get(invoice_no=f.invno)
		o = order.objects.filter(invoice_no=f.invno)
		
		
		h=""
		m=0
		c=0
		for o in o:
			c=c+1
			total="{:,}".format(o.total)
			h+="<tr class='td1' style='border-top: none; border-bottom: none;'><td class='td2'>"+str(c)+"</td><td><strong>"+o.product.name+"</strong><br>"+o.product.description+"</td><td class='td2'>"+o.box+"</td><td class='td2'>"+o.product.hsn+"</td><td class='td2'>"+o.mtr+"</td><td class='td2'>"+o.quantity+"</td><td class='td2'>"+ o.rate +"</td><td class='td2'>"+str(total)+"</td></tr>"
			m=(float(m)+o.total)

		l=c*30
		l1=270
		jh = l1 - l
		jh1=str(jh)
		print(jh)
		jh2="<tr class='td1' style='empty-cells: hide; border-top: none; border-bottom: none; height: "+jh1+"px;''><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>"



		if b.user.gst == "I-GST":
			n= (int(m) * 5)/100
			n2=float(n)
			n1=round(n1, 2)
			q=int(m) + n1
			q3=round(q, 0)
			q1="{:,}".format(q3)
			q2=num2words(q1)
			h1="<td colspan='4' style='padding: 6px; font-size: 14px; border-right: none;'><strong>I-GST @ 5% </strong></td><td class='td1' style=' border-left: none;'>"+str(n1)+"</td>"
		else:
			n=(m * 25)/1000
			n2=float(n)
			n1=round(n2, 2)
			q=int(m) + n1 + n1
			q3=round(q, 0)
			q1="{:,}".format(q3)
			q2=num2words(q3)
			h1="<td colspan='4' style='padding: 6px; font-size: 14px; border-right: none;'><strong>C-GST @ 2.5%<br>S-GST @ 2.5%</strong></td><td class='td1' style=' border-left: none; font-size: 15px'>"+str(n1)+"<br>"+str(n1)+"</td>"




		template_path = 'format/example1.html'
		context = {'f':f, 'b':b, 'order':o, 'h':h, 'jh2':jh2, 'm':m, 'h1':h1, 'q':q1, 'q1':q2}
	    # Create a Django response object, and specify content_type as pdf
		response = HttpResponse(content_type='application/pdf')
	    #response['Content-Disposition'] = 'attachment; filename="report.pdf"' - to download the file

	    #to view only:
		response['Content-Disposition'] = 'filename="INVOICE" +b.invoice_no+".pdf"'
	    # find the template and render it.
		template = get_template(template_path)
		html = template.render(context)

	    # create a pdf
		pisa_status = pisa.CreatePDF(html, dest=response)
	    # if error then show some funy view
		if pisa_status.err:
		   return HttpResponse('We had some errors <pre>' + html + '</pre>')
		return response
	else:
		return redirect('/')


def generate(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			form = billgenerator(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/bill/step2/')
		else:
			form = billgenerator()
			context = {'form': form}
			return render(request, 'generator.html', context)
	else:
		return redirect('/')


def step2(request):
	i=item.objects.all()
	t=temp.objects.get(tid=1)
	f=formatt.objects.get(id=1)
	x = datetime.date.today()
	date=x.strftime("%b %d, %Y")

	t1 = int(f.invno)
	f1 = t1 + 1
	f2 = "%s" %f1
	f.invno = f2.zfill(3)
	f.save()

	b = bill(user=t.user, transport=t.transport, payment=t.payment, invoice_no=f.invno, date=date)
	b.save()
	for x in i:
		o = order(invoice_no=f.invno, product=x.product, quantity=x.quantity, box=x.box, rate=x.rate, total=x.total, mtr=x.mtr)
		o.save()

	i.delete()
	t.delete()

	return redirect('/bill/final_step/')


def render_bill(request):
	if request.user.is_authenticated:
		b=bill.objects.all()
		if request.method == "POST":
			invo=request.POST['billid']

			f = formatt.objects.get(id=1)
			b = bill.objects.get(invoice_no=invo)
			o = order.objects.filter(invoice_no=invo)
			
			h=""
			m=0
			c=0
			for o in o:
				c=c+1
				total="{:,}".format(o.total)
				h+="<tr class='td1' style='border-top: none; border-bottom: none;'><td class='td2'>"+str(c)+"</td><td><strong>"+o.product.name+"</strong><br>"+o.product.description+"</td><td class='td2'>"+o.box+"</td><td class='td2'>"+o.product.hsn+"</td><td class='td2'>"+o.mtr+"</td><td class='td2'>"+o.quantity+"</td><td class='td2'>"+ o.rate +"</td><td class='td2'>"+str(total)+"</td></tr>"
				m=(float(m)+o.total)

			l=c*30
			l1=270
			jh = l1 - l
			jh1=str(jh)
			jh2="<tr class='td1' style='empty-cells: hide; border-top: none; border-bottom: none; height: "+jh1+"px;''><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>"



			if b.user.gst == "I-GST":
				n= (int(m) * 5)/100
				n2=float(n)
				n1=round(n1, 2)
				q=int(m) + n1
				q3=round(q, 0)
				q1="{:,}".format(q3)
				q2=num2words(q1)
				h1="<td colspan='4' style='padding: 6px; font-size: 14px; border-right: none;'><strong>I-GST @ 5% </strong></td><td class='td1' style=' border-left: none;'>"+str(n1)+"</td>"
			else:
				n=(m * 25)/1000
				n2=float(n)
				n1=round(n2, 2)
				q=int(m) + n1 + n1
				q3=round(q, 0)
				q1="{:,}".format(q3)
				q2=num2words(q3)
				h1="<td colspan='4' style='padding: 6px; font-size: 14px; border-right: none;'><strong>C-GST @ 2.5%<br>S-GST @ 2.5%</strong></td><td class='td1' style=' border-left: none; font-size: 15px'>"+str(n1)+"<br>"+str(n1)+"</td>"



			template_path = 'format/example1.html'
			context = {'f':f, 'b':b, 'order':o, 'h':h, 'jh2':jh2, 'm':m, 'h1':h1, 'q':q1, 'q1':q2}
		    # Create a Django response object, and specify content_type as pdf
			response = HttpResponse(content_type='application/pdf')
		    #response['Content-Disposition'] = 'attachment; filename="report.pdf"' - to download the file

		    #to view only:
			response['Content-Disposition'] = 'filename="INVOICE" +b.invoice_no+".pdf"'
		    # find the template and render it.
			template = get_template(template_path)
			html = template.render(context)

		    # create a pdf
			pisa_status = pisa.CreatePDF(html, dest=response)
		    # if error then show some funy view
			if pisa_status.err:
			   return HttpResponse('We had some errors <pre>' + html + '</pre>')
			return response
		else:
			return render(request, "viewbill.html", {'bill':b})
	else:
		return redirect('/')

def final_step(request):
	if request.user.is_authenticated:
		f = formatt.objects.get(id=1)
		b = bill.objects.get(invoice_no=f.invno)
		o = order.objects.filter(invoice_no=f.invno)

		h=""
		m=0
		c=0
		for o in o:
			c=c+1
			total="{:,}".format(o.total)
			h+="<tr class='td1' style='border-top: none; border-bottom: none;'><td class='td2'>"+str(c)+"</td><td><strong>"+o.product.name+"</strong><br>"+o.product.description+"</td><td class='td2'>"+o.box+"</td><td class='td2'>"+o.product.hsn+"</td><td class='td2'>"+o.mtr+"</td><td class='td2'>"+o.quantity+"</td><td class='td2'>"+ o.rate +"</td><td class='td2'>"+str(total)+"</td></tr>"
			m=(float(m)+o.total)


		if b.user.gst == "I-GST":
			n= (int(m) * 5)/100
			n2=float(n)
			n1=round(n1, 2)
			q=int(m) + n1
			q3=round(q, 0)
			q1="{:,}".format(q3)
		else:
			n=(m * 25)/1000
			n2=float(n)
			n1=round(n2, 2)
			q=int(m) + n1 + n1
			q3=round(q, 0)
			q1="{:,}".format(q3)

		if request.method == "POST":
			ewaybill=request.POST['ewaybillno']
			b.ewaybill = ewaybill
			b.save()
			return render(request, 'final_view.html', {'b':b, 'order':o, 'h':h, 'm':m, 'n':n, 'q':q1})
		else:
			return render(request, 'final_view.html', {'b':b, 'order':o, 'h':h, 'm':m, 'n':n, 'q':q1})
	else:
		return redirect('/')