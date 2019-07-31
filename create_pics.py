#!/usr/bin/env python
# encoding: utf-8
# @Time : 2019-07-31 10:24

__author__ = 'Ted'

from PIL import Image, ImageFont, ImageDraw

content={
    "back_img":"pre/paper.jpg",
    "001":{
        "ad":'老板，买10盒月饼呗',
        "head":'001.jpg'
    },
    "002": {
        "ad": '老板，买20盒月饼呗',
        "head": '002.jpg'
    },
    "003": {
        "ad": '老板，生活不易，买50盒月饼呗',
        "head": '003.jpg'
    },
    "004": {
        "ad": '老板，买个80盒月饼，不多',
        "head": '004.jpg'
    },
    "005": {
        "ad": '老板，看面相，你应该买100盒月饼',
        "head": '005.jpg'
    },
    "006": {
        "ad": '老板，恭喜你中奖了，奖品是150盒月饼',
        "head": '006.jpg'
    },
    "007": {
        "ad": '老板，你的员工让我告诉你，他们想吃月饼了',
        "head": '007.jpg'
    },
    "008": {
        "ad": '老板，我卖月饼，买200盒呗',
        "head": '008.jpg'
    },
    "009": {
        "ad": '老板，不整500盒月饼送礼啊',
        "head": '009.jpg'
    }
}
def get_pic(background,head,adcontent,mark,pic_name):
    im = Image.open(background)

    head_img = Image.open(f"head/{head}").resize((150,150),Image.ANTIALIAS)
    im.paste(head_img,(75,20))
    draw = ImageDraw.Draw(im)
    fnt = ImageFont.truetype("pre/SimSun.ttf",20)

    ad_parts = adcontent.split("，")
    y_pos = 180
    for ad_part in ad_parts:
        if ad_part!=ad_parts[-1]:
            ad_w,ad_h = draw.textsize(ad_part+"，", font=fnt)
            draw.text(((300-ad_w)/2,y_pos),ad_part+"，",font=fnt,fill=(0,0,0))
            y_pos+=ad_h+10
        else:
            ad_w, ad_h = draw.textsize(ad_part, font=fnt)
            draw.text(((300 - ad_w) / 2, y_pos), ad_part, font=fnt, fill=(0, 0, 0))
            y_pos += ad_h + 10



    mark_font = ImageFont.truetype("pre/arial.ttf",100)
    draw.text((125,400),mark,font=mark_font,fill=(0,0,0))

    haha = Image.open("pre/haha.jpg")
    im.paste(haha,(0,650))

    qrcode = Image.open("pre/tedxpy.jpg").resize((80,80),Image.ANTIALIAS)
    im.paste(qrcode,(180,810))
    sign_font = ImageFont.truetype("pre/SimSun.ttf",10)
    draw.text((60,875),"自定义制作图片，请扫码",font=sign_font,fill=(0,0,0))
    im.save(pic_name)

if __name__== "__main__":
    for i in range(1,10):
        background = "pre/paper.jpg"
        head = content[f'00{i}']['head']
        adcontent = content[f'00{i}']['ad']
        get_pic(background,head,adcontent,f"{i}",f"{i}.jpg")
    print("九宫格图片生成完毕！")

