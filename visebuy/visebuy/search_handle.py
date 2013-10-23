# -*- coding: utf-8 -*-
from itertools import count
import md5
import pycurl
import urllib
from django.views.decorators.csrf import csrf_exempt
import xmltodict
import cStringIO
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render

products = None
dm_server = "http://msm.cais.ntu.edu.sg:8195/dmserver/"

@csrf_exempt
def search_by_imageurl(request):
    if request.method == "POST":
        #so the job is broken down to smaller tasks
        #get image url from user and then add all the filter
        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        imageurl = request.POST['imageurl']
        full_curl = str('http://msm.cais.ntu.edu.sg:8295/dmserver/svc3?data='+imageurl+'&servFlag=0&svcFlag=1&modFlag=0')
        c.setopt(c.URL, full_curl)
        c.setopt(c.WRITEFUNCTION, buf.write)
        c.setopt(c.CONNECTTIMEOUT, 10)
        c.perform()
        value = buf.getvalue()
        buf.close()
        return HttpResponse(value)
    return HttpResponse("Invalid search request from client")

def search(request):
    buf = cStringIO.StringIO()
    c = pycurl.Curl()
    # c.setopt(c.URL, dm_server + 'svc3?data=' + '1' + '&servFlag=0&svcFlag=0&modFlag=' + '1')
    c.setopt(c.URL, 'http://msm.cais.ntu.edu.sg:8295/dmserver/svc3?data=http://s3.amazonaws.com/rapgenius/filepicker/5jTDmubSTnCREE8BIe5w_nike_shoes.jpg&servFlag=0&svcFlag=1&modFlag=0')
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.setopt(c.CONNECTTIMEOUT, 10)
    c.perform()
    value = buf.getvalue()

    buf.close()
    return HttpResponse(value)

def format_pages(searchType, pageArray, id, filters, display, result):
    pages = pageArray.split(';')
    for page in pages:
        page_element = page.split(',')
        if(count(page_element) != 1):
            link = ""
            page = '<a href=' + link + '">' + page[0] + '</a>'
        else:
            page = '<span class="active">' + page[0] + '</span>'
    return pages

def action_index(request):
    return render(request, 'visebuy/pages/error.html', {'msg': "请在输入框中输入在右上角的搜索字词。"})

def action_create(request, format = ''):
    body_content = get_template('visebuy/search/create.html')
    mainBody = body_content.render(Context({}))
    api = ''
    #TODO what is this api
    if format != '':
        format += format
    else:
        format = ''
    #TODO not sure if this right or not

    if 'modflag' not in request.session:
        request.session['modflag'] = 0

    base_url = '/visebuy'
    #TODO not sure if this is correct or not

    if 'id' not in request.POST:
        i = request.GET['id']
        u = request.GET['url']

        mod_flag = request.POST['modflag']
        # cache id not randomized because the image ids for the same image will always be the same
        cache_id = md5.new(i).digest()

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, dm_server + 'svc3?data=' + i + '&servFlag=0&svcFlag=0&modFlag='+mod_flag)
        c.setopt(c.WRITEFUNCTION, buf.write)
        c.setopt(c.CONNECTTIMEOUT, 10)
        c.perform()
        value = buf.getvalue()
        buf.close()

        #then convert the return xml to python dictionary
        xmltodict.parse(value)

        #missing a part that writes data to the cache_data
        # $cache_data = array(
			# 'file' => $u,
			# 'images_ids' => $data['Output']['CacheImgList']
			# );
        #
			# Cache::set($cache_id, $cache_data, false);
			# Response::redirect("{$api}/search/images{$format}/{$cache_id}");

        return HttpResponseRedirect(api + "/search/image" + format + "/" + cache_id)

    if 'q' in request.POST:
        q = request.POST['q']
        q = urllib.unquote(q).decode('utf8')

        mod_flag = request.POST['modflag']

        if q[0, 7] == "http://":  # missing parseurl(q)
            tmp = open(q).read()  # not sure if this function is correct or not
            cache_id = 0

            t = q  # should have parsed q into url
            if t['path']:
                return HttpResponseRedirect('/page/error')

            path_info = t['path']  # missing path_info function





    return 'nothing'