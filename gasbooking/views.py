from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from datetime import date
from datetime import datetime



def home(request):
    return render(request,'carousel.html')

def Admin_Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "yes"
            else:
                error = "not"
        except:
            error="not"
    d = {'error': error}
    return render(request,'login.html',d)
def Admin_Home(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    book=Newconnection.objects.all()
    book1=Bookcylinder.objects.all()
    book2=Addstaff.objects.all()
    book3=Registration.objects.all()
    b=0
    c1=0
    c2=0
    c3=0
    for i in book:
        b+=1
        if i.connection == 'Approved':
            c1+=1
        elif i.connection == 'canceled':
            c2+=1
        elif i.connection == 'Onhold':
            c3+=1
    b1=0
    bc1=0
    bc2=0
    bc3=0
    for i in book1:
        b1+=1
        if i.bookstatus == 'confirmed':
            c1+=1
        elif i.bookstatus == 'ontheway':
            c2+=1
        elif i.bookstatus == 'canceled':
            c3+=1
    b2=0
    for i in book2:
        b2+=1
    b3=0
    for i in book3:
        b3+=1

    d={'b':b,'b1':b1,'b2':b2,'b3':b3,'c1':c1,'c2':c2,'c3':c3,'bc1':bc1,'bc2':bc2,'bc3':bc3}
    return render(request, 'admin_home.html',d)
def User_Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if not user.is_staff:
                login(request, user)
                error ="yes"
            else:
                error = "not"
        except:
            error="not"
    d = {'error': error}
    return render(request,'user_login.html',d)
def Signup(request):
    error=""
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        m=request.POST['mobile']
        e=request.POST['email']
        user=User.objects.create_user(username=u,password=p,email=e)
        sign=Registration.objects.create(mobile=m,user=user)
        error="yes"
    d={'error':error}
    return render(request,'signup.html',d)
def New_connection(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = False
    br=""
    rt =datetime.now()
    rd = date.today()
    rt1 = str(rt).split(":")
    rt2 = "".join(rt1)
    order_id1 = rt2.split("-")
    order_id2 = "".join(order_id1)
    order_id3 = order_id2.split(" ")
    order_id4 = "".join(order_id3)
    order_id = order_id4.replace("2020","")
    order_id5 =order_id.split(".")
    order_id6 = "".join(order_id5)
    user = User.objects.get(id=request.user.id)
    data=Registration.objects.get(user=user)
    new_con=""
    try:
        new_con = Newconnection.objects.get(user=data)
    except:
        pass
    if new_con:
        error="already"
    else:
        if request.method == "POST":
            u = request.POST['uname']
            e = request.POST['email']
            mo = request.POST['mobile']
            g = request.POST['gender']
            n = request.POST['nationality']
            m = request.POST['married']
            a = request.POST['add']
            r = request.POST['ralated']
            f = request.POST['fname']
            l = request.POST['lname']
            c = request.POST['city']
            z = request.POST['zipcode']
            i = request.FILES['img']
            b = User.objects.get(username=u, email=e)
            br = Registration.objects.get(user=b, mobile=mo)
            Newconnection.objects.create(user=br, gen=g, connection='null', date=date.today(), cost='null',
                                         registration=order_id6, nationality=n, merriedstatus=m, address=a, related=r,
                                         fname=f, lname=l, city=c, zipcode=z, img=i)
            error = "create"
    d={'data':data,'error':error}
    return render(request,'new_connection.html',d)
def user_Home(request):
    return render(request, 'user_home.html')
def View_connection(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user=User.objects.get(id=request.user.id)
    data=Registration.objects.get(user=user)
    data1=Newconnection.objects.filter(user=data)
    d={'data1':data1}
    return render(request,'view_connection.html',d)
def admin_viewbooking(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data1=Bookcylinder.objects.all()
    d={'data1':data1}
    return render(request,'admin_viewbooking.html',d)

def edit_connection(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user=User.objects.get(id=request.user.id)
    data=Registration.objects.get(user=user)
    data1=Newconnection.objects.get(user=data)
    error=False
    if request.method=="POST":
        u = request.POST['uname']
        e= request.POST['email']
        mo = request.POST['mobile']
        g = request.POST['gender']
        n = request.POST['nationality']
        m= request.POST['married']
        a = request.POST['add']
        r = request.POST['ralated']
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['city']
        z = request.POST['zipcode']
        i= request.FILES['img']

        try:
            i= request.FILES['img']
            data1.img=i
            data1.save()
        except:
            pass
        user.username=u
        user.email=e
        data.mobile=mo
        data1.gen=g
        data1.nationality=n
        data1.merriedstatus=m
        data1.related=r
        data1.fname=f
        data1.rname=l
        data1.city=c
        data1.zipcode=z
        data1.save()
        data.save()
        user.save()
        error="yes"

    d={'data1':data1,'error':error,'data':data,}
    return render(request,'edit_connection.html',d)

def Logout_user(request):
    if not request.user.is_staff:
        return redirect('home')
    logout(request)
    return redirect('home')

def admin_viewconnection(request):
    data=Newconnection.objects.all()
    d={'data':data}
    return render(request,'admin_viewconnection.html',d)
def Admin_connection(request,pid):
    data=Newconnection.objects.get(id=pid)
    d={'data':data}
    return render(request,'admin_connectiondetail.html',d)
def Edit_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    book =Newconnection.objects.get(id=pid)
    error=""
    if request.method == "POST":
        s = request.POST['status']
        c = request.POST['cost']
        book.connection = s
        book.cost= c
        book.save()
        error="yes"
    d = {'book': book,'error':error}
    return render(request,'edit_status.html', d)
def bookcylinder(request):
    user=User.objects.get(id=request.user.id)
    data=Registration.objects.get(user=user)
    data1=Newconnection.objects.filter(user=data)
    d={'data1':data1}
    return render(request,'bookingcylinder.html',d)
def bookdetail(request):
    user=User.objects.get(id=request.user.id)
    data=Registration.objects.get(user=user)
    data1=Newconnection.objects.filter(user=data)
    d={'data1':data1}
    return render(request,'bookdetail.html',d)
def book(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user=User.objects.get(id=request.user.id)
    data=Registration.objects.get(user=user)
    data1=Newconnection.objects.get(user=data)
    error=False
    rt = datetime.now()
    rd = date.today()
    rt1 = str(rt).split(":")
    rt2 = "".join(rt1)
    order_id1 = rt2.split("-")
    order_id2 = "".join(order_id1)
    order_id3 = order_id2.split(" ")
    order_id4 = "".join(order_id3)
    order_id = order_id4.replace("2020","")
    order_id5 =order_id.split(".")
    order_id6 = "".join(order_id5)
    if request.method == "POST":
        g = request.POST['gassize']
        Bookcylinder.objects.create(user=data1,gassize=g,booknumber=order_id6,bookdate=date.today(),bookstatus='null',reffercost='null',responsetime='null')
        error="yes"
    d={'data1':data1,'error':error}
    return render(request,'book.html',d)
def View_booking(request):
    user=User.objects.get(id=request.user.id)
    data=Registration.objects.get(user=user)
    data2=0
    try:
        data2=Newconnection.objects.get(user=data)
    except:
        pass
    data1=Bookcylinder.objects.filter(user=data2)
    d={'data1':data1}
    return render(request,'view_booking.html',d)
def bookhistory(request):
    user=User.objects.get(id=request.user.id)
    data=Registration.objects.get(user=user)
    data2=Newconnection.objects.get(user=data)
    data1=Bookcylinder.objects.filter(user=data2)
    d={'data1':data1,'data2':data2}
    return render(request,'bookhistory.html',d)
def Admin_booking(request,pid):
    data=Bookcylinder.objects.get(id=pid)
    history = History.objects.filter(booking=data).all()
    d={'data':data,'history':history}
    return render(request,'admin_bookingdetail.html',d)
def Admin_booking2(request,pid):
    data=Bookcylinder.objects.get(id=pid)
    history = History.objects.filter(booking=data).all()
    d={'data':data,'history':history}
    return render(request,'admin_bookingdetail2.html',d)
def Edit_booking(request,pid):
    if not request.user.is_staff:
        return redirect('admin_login')
    book =Bookcylinder.objects.get(id=pid)
    data=Addstaff.objects.all()
    error=""
    if request.method == "POST":
        s = request.POST['bookstatus']
        a = request.POST['assignto']
        r= request.POST['reffercost']
        book.bookstatus = s
        sta=Addstaff.objects.get(name=a)
        book.assignto= sta
        book.reffercost= r
        book.responsetime= date.today()
        book.save()
        error="yes"
    d = {'book': book,'data':data,'error':error}
    return render(request,'edit_booking.html', d)
def edit_assign(request,pid):
    data=Bookcylinder.objects.get(id=pid)
    staff=Addstaff.objects.all()
    error=""
    if request.method == "POST":
        st = request.POST['staff']
        s = request.POST['status']
        data.bookstatus = s
        sta = Addstaff.objects.get(name=st)
        data.assignto = sta
        data.save()
        History.objects.create(d_boy=st,booking=data,status=s,time1=datetime.today())
        error="yes"
    d = {'error':error,'data':data,'staff':staff}
    return render(request,'edit_assign.html',d)

def addstaff(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    error=False
    if request.method == "POST":
        i = request.POST['staffid']
        n = request.POST['name']
        e= request.POST['email']
        m= request.POST['mobile']
        a= request.POST['address']
        Addstaff.objects.create(staffid=i,email=e,mobile=m,name=n,address=a)
        error="yes"
    d={'error':error}
    return render(request,'addstaff.html',d)
def view_staff(request):
     if not request.user.is_staff:
        return redirect('admin_login')
     data=Addstaff.objects.all()
     d={'data':data}
     return render(request,'view_staff.html',d)
def edit_staff(request,pid):
    if not request.user.is_staff:
        return redirect('admin_login')
    data=Addstaff.objects.get(id=pid)
    error=""
    if request.method == "POST":
        i = request.POST['staffid']
        n = request.POST['name']
        e= request.POST['email']
        m= request.POST['mobile']
        a= request.POST['address']
        data.staffid=i
        data.name=n
        data.email=e
        data.mobile=m
        data.address=a
        data.save()
        error="yes"
    d={'data':data,'error':error}
    return render(request,'edit_staff.html',d)
def delete_staff(request,pid):
    if not request.user.is_staff:
        return redirect('admin_login')
    data=Addstaff.objects.get(id=pid)
    data.delete()
    return redirect('view_staff')
def view_user(request):
    data=Registration.objects.all()
    d={'data':data}
    return render(request,'view_user.html',d)

def admin_onholdconnection(request):
    data=Newconnection.objects.all()
    d={'data':data}
    return render(request,'admin_onholdconnection.html',d)
def admin_approvedconnection(request):
    data=Newconnection.objects.all()
    d={'data':data}
    return render(request,'admin_approvedconnection.html',d)
def admin_rejectedconnection(request):
    data=Newconnection.objects.all()
    d={'data':data}
    return render(request,'admin_rejectedconnection.html',d)
def admin_confirmedbooking(request):
    data=Bookcylinder.objects.all()
    d={'data':data}
    return render(request,'admin_confirmedbooking.html',d)
def admin_onthewaybooking(request):
    data=Bookcylinder.objects.all()
    d={'data':data}
    return render(request,'admin_onthewaybooking.html',d)
def admin_canceledbooking(request):
    data=Bookcylinder.objects.all()
    d={'data':data}
    return render(request,'admin_canceledbooking.html',d)
def Admin_booking2(request,pid):
    data=Bookcylinder.objects.get(id=pid)
    history = History.objects.filter(booking=data).all()
    d={'data':data,'history':history}
    return render(request,'admin_bookingdetail2.html',d)
def search_booking(request):
    data=Bookcylinder.objects.all()
    error=False
    s=0
    if request.method=="POST":
        s = request.POST['booknumber']
        data = Bookcylinder.objects.filter(booknumber=s)
        if data:
            data1 = data
            error=True
    d={'data':data,'error':error,'s':s}
    return render(request,'search_booking.html',d)
def Booking_report(request):
    data=Bookcylinder.objects.all()
    error=False
    i=""
    n=""
    if request.method == "POST":
        i = request.POST['date1']
        n = request.POST['date2']
        i1=datetime.fromisoformat(i).month
        i2=datetime.fromisoformat(i).year
        i3=datetime.fromisoformat(i).day
        n1=datetime.fromisoformat(n).month
        n2=datetime.fromisoformat(n).year
        n3=datetime.fromisoformat(n).day
        for j in data:
            d1=datetime.fromisoformat(j.bookdate).month
            d2=datetime.fromisoformat(j.bookdate).year
            d3=datetime.fromisoformat(j.bookdate).day
            day3=(d2*365)+(d1*30)+d3
            day1=(i2*365)+(i1*30)+i3
            day2=(n2*365)+(n1*30)+n3
            if day3 > day1 and day3 < day2:
                j.status='active'
                j.save()
                error=True
            else:
                j.status='inactive'
                j.save()
    d={'data':data,'error':error,'i':i,'n':n}
    return render(request,'booking_report.html',d)

def Connection_report(request):
    data=Newconnection.objects.all()
    error=False
    i=""
    n=""
    if request.method == "POST":
        i = request.POST['date1']
        n = request.POST['date2']
        i1=datetime.fromisoformat(i).month
        i2=datetime.fromisoformat(i).year
        i3=datetime.fromisoformat(i).day
        n1=datetime.fromisoformat(n).month
        n2=datetime.fromisoformat(n).year
        n3=datetime.fromisoformat(n).day
        for j in data:
            d1=datetime.fromisoformat(j.date).month
            d2=datetime.fromisoformat(j.date).year
            d3=datetime.fromisoformat(j.date).day
            day3=(d2*365)+(d1*30)+d3
            day1=(i2*365)+(i1*30)+i3
            day2=(n2*365)+(n1*30)+n3
            if day3 > day1 and day3 < day2:
                j.status='active'
                j.save()
                error=True
            else:
                j.status='inactive'
                j.save()
    d={'data':data,'error':error,'i':i,'n':n}
    return render(request,'connection_report.html',d)
def adminsearch_booking(request):
    data=Bookcylinder.objects.all()
    error=False
    s=""
    if request.method=="POST":
        s = request.POST['booknumber']
        data = Bookcylinder.objects.filter(booknumber=s)
        if data:
            data1 = data
            error=True
    d={'data':data,'error':error,'s':s}
    return render(request,'adminsearch_booking.html',d)
def adminsearch_connection(request):
    data=Newconnection.objects.all()
    error=False
    s=""
    if request.method=="POST":
        s = request.POST['registration']
        data = Newconnection.objects.filter(registration=s)
        if data:
            data1 = data
            error=True
    d={'data':data,'error':error,'s':s}
    return render(request,'adminsearch_connection.html',d)
def all_booking(request):
    data=Bookcylinder.objects.all()
    d={'data':data}
    return render(request,'all_booking.html',d)
def all_connection(request):
    data=Newconnection.objects.all()
    d={'data':data}
    return render(request,'all_connection.html',d)

def Logout(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    logout(request)
    return redirect('home')

def view_profile(request):
    user=User.objects.get(id=request.user.id)
    data=Registration.objects.get(user=user)
    d={'data':data}
    return render(request,'view_profile.html',d)
def edit_profile(request):
    user=User.objects.get(id=request.user.id)
    data=Registration.objects.get(user=user)
    error=False
    if request.method=='POST':
        u=request.POST['uname']
        m=request.POST['mobile']
        e=request.POST['email']
        user.username=u
        user.email=e
        data.mobile=m
        user.save()
        data.save()
        error="yes"
    d={'data':data,'error':error}
    return render(request,'edit_ptofile.html',d)
def Change_Password(request):
    error = ""
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "yes"
        else:
            error = "not"
    d = {'error':error}
    return render(request,'change_password.html',d)

def admin_confirmedbooking1(request):
    data=Bookcylinder.objects.filter(bookstatus = "confirmed")
    d={'data':data}
    return render(request,'admin_confirmedbooking1.html',d)

def admin_deliveredbooking1(request):
    data=Bookcylinder.objects.filter(bookstatus = "delivered")
    d={'data':data}
    return render(request,'admin_confirmedbooking1.html',d)

def admin_new(request):
    data=Bookcylinder.objects.filter(bookstatus = "null")
    d={'data':data}
    return render(request,'admin_new.html',d)
def admin_onthewaybooking2(request):
    data=Bookcylinder.objects.filter(bookstatus="ontheway")
    d={'data':data}
    return render(request,'admin_onthewaybooking2.html',d)
def admin_canceledbooking3(request):
    data=Bookcylinder.objects.filter(bookstatus="canceled")
    d={'data':data}
    return render(request,'admin_canceledbooking3.html',d)
