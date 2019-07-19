import math
from datetime import datetime, timedelta, time

from django.shortcuts import render, redirect
from django.http import JsonResponse

from image2key.base64toimg import stringToRGB
from .forms import KeyImageCreateForm, KeyImageCompareForm

from .models import KeyImage

from .compareImg import img_smil

# Create your views here.
from django.views import View


class AddView(View):
    def post(self, req):
        key_image = KeyImageCreateForm(req.POST).get_commit_data()

        key_image.save()

        return JsonResponse(
            {
                'success': True,
                'id': KeyImage.objects.last().id
            }
        )


class CompareView(View):
    def post(self, req):
        img_input, user_uuid = KeyImageCompareForm(req.POST).get_data()

        user_images = KeyImage.objects.all().filter(user_uuid=user_uuid)
        print(user_images)
        tmp_list = list()
        for user_image in user_images:
            now_image = user_image.key_img
            img_tmp = stringToRGB(bytes(now_image, 'utf-8'))

            good, rate = img_smil(img_input, img_tmp)

            if good:
                tmp_list.append([good, user_image.key_uuid])

        tmp_list.sort(key=lambda x: x[0])

        result = list()
        for i in tmp_list:
            result.append(i[1])

        return JsonResponse(
            {
                'success': True,
                'data': result
            }
        )
