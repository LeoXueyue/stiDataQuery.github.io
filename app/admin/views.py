from . import admin
import time, json
from app import db
from app.models import Sti_gtshmed, Sti_gtshmed_device
from flask import render_template


# 主页
@admin.route('/<int:page>', methods=['GET'])
def hello_world(page=None):
    if page == None:
        page = 1
    page_data = db.session().query(Sti_gtshmed, Sti_gtshmed_device).filter(
        Sti_gtshmed.createName == Sti_gtshmed_device.device_name).order_by(
        Sti_gtshmed.createdAt.desc()
    ).paginate(page=page, per_page=10)
    data_all_count = db.session().query(Sti_gtshmed, Sti_gtshmed_device).filter(
        Sti_gtshmed.createName == Sti_gtshmed_device.device_name).count()
    if page == int(data_all_count / 10) + 1:
        singal_data_count = data_all_count % 10
    else:
        singal_data_count = 10
    return render_template("index.html", page_data=page_data, data_all_count=data_all_count,
                           singal_data_count=singal_data_count)

#列表
@admin.route('/list/<int:page>', methods=['GET'])
def list(page=None):
    if page == None:
        page = 1
    # sti=db.session().query(Sti_gtshmed,Sti_gtshmed_device).filter(Sti_gtshmed.createName==Sti_gtshmed_device.device_name).all()
    # for v in sti:
    #     print(v.Sti_gtshmed.createdAt)
    # print(sti)
    data_all_count = db.session().query(Sti_gtshmed, Sti_gtshmed_device).filter(
        Sti_gtshmed.createName == Sti_gtshmed_device.device_name).count()
    page_data = db.session().query(
        Sti_gtshmed, Sti_gtshmed_device
    ).filter(
        Sti_gtshmed.createName == Sti_gtshmed_device.device_name
    ).order_by(
        Sti_gtshmed.createdAt.desc()
    ).paginate(page=page, per_page=10)
    print(page_data)
    if page == int(data_all_count / 10) + 1:
        singal_data_count = data_all_count % 10
    else:
        singal_data_count = 10
    return render_template("index.html", page_data=page_data, data_all_count=data_all_count,
                           singal_data_count=singal_data_count)

#默认查询列表
@admin.route('/query/<int:page>', methods=['GET', 'POST'])
def query(page=None):
    if page == None:
        page = 1
    date_list = []
    n = 0
    nowtimeint = int(time.time())
    nowtimestr = time.strftime("%Y-%m-%d", time.localtime(nowtimeint))
    print(nowtimestr)
    starttimeint = nowtimeint - 60 * 60 * 24 * 30
    starttimestr = time.strftime("%Y-%m-%d", time.localtime(starttimeint))
    print(starttimestr)
    nexttimeint = nowtimeint
    while starttimeint < nexttimeint:
        nexttimeint = nowtimeint - 60 * 60 * 24 * n
        nexttimestr = time.strftime("%Y-%m-%d", time.localtime(nexttimeint))
        sti_count = Sti_gtshmed.query.filter(Sti_gtshmed.createdAt.ilike("%" + nexttimestr + "%")).count()
        date_dict = {"time": nexttimestr, "count": sti_count}
        date_list.append(date_dict)
        print(nexttimestr)
        n = n + 1
    count = int(len(date_list) / 10) + 1
    pagenum = []
    for a in range(1, count + 1):
        pagenum.append(a)
    page_data = date_list[(page - 1) * 10:page * 10]
    pre_page = page - 1
    next_page = page + 1

    if page == int(31 / 10) + 1:
        singal_data_count = 31 % 10
    else:
        singal_data_count = 10
    return render_template('query.html', date_list=date_list,
                           starttimestr=starttimestr, nowtimestr=nowtimestr,
                           count=count, page_data=page_data, pagenum=pagenum,
                           pre_page=pre_page, next_page=next_page, page=page, singal_data_count=singal_data_count)

#实际查询列表
@admin.route('/query/list/<string:send_time>/<int:page>', methods=['GET', 'POST'])
def query_list(send_time, page=None):
    if page == None:
        page = 1
    date_list = []
    n = 0
    data = send_time.split(",")
    starttimestr = data[0]
    nowtimestr = data[1]
    # print('starttime', starttimestr)
    # print('nowtime', nowtimestr)
    starttimeint = int(time.mktime(time.strptime(starttimestr, "%Y-%m-%d")))
    nowtimeint = int(time.mktime(time.strptime(nowtimestr, "%Y-%m-%d")))
    # print("poststartint", starttimeint)
    # print("postnowint", nowtimeint)
    # print("poststartstr", starttimestr)
    # print("postnowstr", nowtimestr)
    nexttimeint = nowtimeint
    print("nexttimeint", nexttimeint)
    while starttimeint + 14400 <= nexttimeint:
        nexttimeint = nowtimeint - 60 * 60 * 24 * n
        nexttimestr = time.strftime("%Y-%m-%d", time.localtime(nexttimeint))
        print("postnextstr", nexttimestr)
        sti_count = Sti_gtshmed.query.filter(Sti_gtshmed.createdAt.ilike("%" + nexttimestr + "%")).count()
        date_dict = {"time": nexttimestr, "count": sti_count}
        date_list.append(date_dict)
        # print(nexttimestr)
        n = n + 1
        # print(n)
    count = int(len(date_list) / 10) + 1
    pagenum = []
    for a in range(1, count + 1):
        pagenum.append(a)
    page_data = date_list[(page - 1) * 10:page * 10]
    pre_page = page - 1
    next_page = page + 1
    if page == int(n / 10) + 1:
        singal_data_count = n % 10
    else:
        singal_data_count = 10
    return render_template('query_list.html', send_time=send_time, date_list=date_list, starttimestr=starttimestr,
                           nowtimestr=nowtimestr, count=count, page_data=page_data,
                           pagenum=pagenum, pre_page=pre_page, next_page=next_page, page=page, n=n,
                           singal_data_count=singal_data_count)

#查询列表个体信息
@admin.route('/check/list/<string:createdtime>/<int:page>', methods=['GET'])
def check_list(createdtime, page=None):
    if page == None:
        page = 1
    # sti_count=Sti_gtshmed.query.filter(Sti_gtshmed.createdAt.ilike("%"+createdtime+"%")).count()
    # print("sti_count",sti_count)
    # sti=Sti_gtshmed.query.filter(Sti_gtshmed.createdAt.ilike("%"+createdtime+"%")).all()
    data_all_count = Sti_gtshmed.query.filter(Sti_gtshmed.createdAt.ilike("%" + createdtime + "%")).count()
    page_data = Sti_gtshmed.query.filter(Sti_gtshmed.createdAt.ilike("%" + createdtime + "%")).order_by(
        Sti_gtshmed.createdAt.desc()
    ).paginate(page=page, per_page=10)
    if page == int(data_all_count / 10) + 1:
        singal_data_count = data_all_count % 10
    else:
        singal_data_count = 10
    return render_template("check.html", page_data=page_data, createdtime=createdtime, data_all_count=data_all_count,
                           singal_data_count=singal_data_count)

#统计
@admin.route('/pro_count', methods=['GET'])
def pro_count():
    provice = []#省
    data = []#数据
    sti_device = Sti_gtshmed_device.query.all()
    for v in sti_device:
        provice.append(v.provice)
    province = []
    for id in provice:
        if id not in province:
            province.append(id)
    # print(province)
    sti = Sti_gtshmed.query.count()
    count = db.session().query(Sti_gtshmed, Sti_gtshmed_device) \
        .filter(Sti_gtshmed.createName == Sti_gtshmed_device.device_name).count()
    for v in province:
        sti_count = db.session().query(Sti_gtshmed, Sti_gtshmed_device) \
            .filter(Sti_gtshmed.createName == Sti_gtshmed_device.device_name, Sti_gtshmed_device.provice == v).count()
        # a = {"vaule": sti_count, "name": v}
        data.append(sti_count)
    weizhi=sti-count
    province.append("未知")
    data.append(weizhi)
    # print(data)
    # sti = db.session().query(Sti_gtshmed, Sti_gtshmed_device).filter(
    #     Sti_gtshmed.createName == Sti_gtshmed_device.device_name).all()

    return render_template("pro_count.html",data=json.dumps(data),province=json.dumps(province))
