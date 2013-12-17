# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
import django

#so it's because of the url has been set so it will decide which controller action will take care of the request
def page(request):
    return render(request, 'visebuy/template.html', {
        'page_title': 'page'
        }
    )

def base(request):
    t = get_template('visebuy/layout/home.html')
    mainBody = t.render(Context({}))
    return render(request, 'visebuy/template.html', {
        'main_body': mainBody
    })

def detailpage(request, offset):
    t = get_template('visebuy/layout/otherurls.html')
    mainBody = t.render(Context({'content': offset}))
    return render(request, 'visebuy/template.html', {
        'main_body': mainBody
        }
    )

#start writing the demos to use the API

def demo_productdetailpage(request):
    return render(request, 'visebuy/demo_search/demo_product_detail.html')

def demo_homepage(request):
    return render(request, 'visebuy/demo_search/demo_home.html')

def demo_searchpage(request):
    return render(request, 'visebuy/demo_search/demo_search.html')

def search_handle(request):
    ab = "abc"
    return HttpResponse('correctly')




tel = {
    'per_page': 20,
		'num_links': 4,
		'brand': [
			"安踏",
			"回力",
			"古由卡",
			"卡洛驰",
			"李宁",
			"特步",
			"恒源祥",
			"阿迪达斯",
			"SUPRA",
			"耐克"
        ],
		'colours': {
			"黑色": '0,0,0',
			"白色": '255,255,255',
			"灰色": '128,128,128',
			"红色": '255,0,0',
			"橙色": '255,170,0',
			"棕色": '153,102,0',
			"黄色": '255,255,0',
			"绿色": '0,255,0',
			"青色": '0,255,212',
			"蓝色": '0,0,255',
			"紫色": '153,0,255',
			"粉红色": '255,0,161'
        },
		'advanced_colours': [
			"003366",
			"336699",
			"3366CC",
			"003399",
			"000099",
			"0000CC",
			"000066",
			"006666",
			"006699",
			"0099CC",
			"0066CC",
			"0033CC",
			"0000FF",
			"3333FF",
			"333399",
			"669999",
			"009999",
			"33CCCC",
			"00CCFF",
			"0099FF",
			"0066FF",
			"3366FF",
			"3333CC",
			"666699",
			"339966",
			"00CC99",
			"00FFCC",
			"00FFFF",
			"33CCFF",
			"3399FF",
			"6699FF",
			"6666FF",
			"6600FF",
			"6600CC",
			"339933",
			"00CC66",
			"00FF99",
			"66FFCC",
			"66FFFF",
			"66CCFF",
			"99CCFF",
			"9999FF",
			"9966FF",
			"9933FF",
			"9900FF",
			"006600",
			"00CC00",
			"00FF00",
			"66FF99",
			"99FFCC",
			"CCFFFF",
			"CCCCFF",
			"CC99FF",
			"CC66FF",
			"CC33FF",
			"CC00FF",
			"9900CC",
			"003300",
			"009933",
			"33CC33",
			"66FF66",
			"99FF99",
			"CCFFCC",
			"FFFFFF",
			"FFCCFF",
			"FF99FF",
			"FF66FF",
			"FF00FF",
			"CC00CC",
			"660066",
			"336600",
			"009900",
			"66FF33",
			"99FF66",
			"CCFF99",
			"FFFFCC",
			"FFCCCC",
			"FF99CC",
			"FF66CC",
			"FF33CC",
			"CC0099",
			"993399",
			"333300",
			"669900",
			"99FF33",
			"CCFF66",
			"FFFF99",
			"FFCC99",
			"FF9999",
			"FF6699",
			"FF3399",
			"CC3399",
			"990099",
			"666633",
			"99CC00",
			"CCFF33",
			"FFFF66",
			"FFCC66",
			"FF9966",
			"FF6666",
			"FF0066",
			"CC6699",
			"993366",
			"999966",
			"CCCC00",
			"FFFF00",
			"FFCC00",
			"FF9933",
			"FF6600",
			"FF5050",
			"CC0066",
			"660033",
			"996633",
			"CC9900",
			"FF9900",
			"CC6600",
			"FF3300",
			"FF0000",
			"CC0000",
			"990033",
			"663300",
			"996600",
			"CC3300",
			"993300",
			"990000",
			"800000",
			"993333"

		],
		'gender': [
			"男",
			"女",
			"中性"
		],
		'style': [
			"休闲鞋",
			"徒步鞋",
			"多功能鞋",
			"靴子",
			"凉鞋"
		],
		'category': [
			"低帮鞋",
			"日常休闲鞋",
			"系带款式",
			"懒人套式",
			"魔术贴式",
			"格子图案",
			"英伦风格",
			"头层牛皮",
			"人造皮革",
			"经典休闲",
			"搭扣款式",
			"帆布鞋",
			"人字拖",
			"户外拖鞋"
		],
		'category_list': {
			'女': {
				'单鞋': [
					"浅口鞋","满帮鞋","半口鞋","豆豆鞋","乐福鞋","鱼嘴鞋","唐卡鞋","帆船鞋","芭蕾鞋","生活鞋"
				],
				'女凉鞋': [
					"全凉鞋","鱼嘴鞋","凉拖","一字型","后空鞋","人字型","T型","中空","包头","洞洞鞋","套趾","其他"
				],
				'女靴': [
					"时装靴","休闲靴","马丁靴","工装靴","流苏靴","机车靴","铆钉靴","大头靴","军警靴"
				]
            },
			'男': {
				'男休闲': [
					"生活鞋","轻便鞋","工装鞋","透气鞋","帆船鞋","豆豆鞋","网眼鞋","乐福鞋","牛津鞋","驾车鞋","工装靴",
					"时装靴"
				],
				'正装鞋': [
					"生活鞋","牛津鞋","工装鞋","棉鞋","乐福鞋"
				],
				'男凉鞋': [
					"冲孔鞋","包头","套趾","洞洞鞋","一字型","露趾","人字型","人字拖","T型"
				]
            },
			'运动鞋': [
				"运动生活鞋","篮球鞋","跑步鞋","休闲鞋","滑板鞋","乒乓球鞋",
				"休闲复古鞋","帆布鞋","网球鞋","足球鞋","综训鞋","羽毛球鞋",
				"凉鞋/凉拖","硫化鞋","帆船鞋","室内鞋","户外鞋","赛车鞋",
				"健身鞋","健步鞋","靴子"
			],
			'户外鞋': [
				"透气鞋","网眼鞋","登山靴","生活鞋","轻便鞋","其他","满帮鞋"
			]
        }
}

