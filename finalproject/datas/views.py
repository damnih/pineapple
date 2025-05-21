from django.shortcuts import render, redirect
import requests 
from django.conf import settings 
from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
# from django.contrib.auth.decorators import 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from .forms import MyDataForm

# Create your views here.


# 요청URL = http://finlife.fss.or.kr/finlife/fdrmDpstApi/list.{응답방식}

# http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={발급받은 인증키}&topFinGrpNo=020000&pageNo=1





API_KEY = settings.API_KEY 

# response = requests.get('http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1')

# Create your views here.

URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'

# params = {
#     'auth': settings.API_KEY,
#     'topFinGrpNo': '020000', 
#     'pageNo': page
# }


@api_view(['GET'])
def save_deposit_products(request):
    page = 1
    total_saved = 0
    while True: 
        try:
            params = {
                'auth': settings.API_KEY,
                'topFinGrpNo': '020000',
                'pageNo': page 
            }
            response = requests.get(URL, params=params)
            response.raise_for_status()
            data = response.json()

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        base_list = data.get('result', {}).get('baseList', [])
        if not base_list:
            break 

        option_list = data.get('result', {}).get('optionList', [])

        # 모든 필드 포함
        products = [
            DepositProducts(
                fin_prdt_cd=item['fin_prdt_cd'],
                kor_co_nm=item.get('kor_co_nm', ''),
                fin_prdt_nm=item.get('fin_prdt_nm', ''),
                etc_note=item.get('etc_note', ''),
                join_deny=int(item.get('join_deny', 0)),
                join_member=item.get('join_member', ''),
                join_way=item.get('join_way', ''),
                spcl_cnd=item.get('spcl_cnd', ''),
            ) for item in base_list
        ]
        DepositProducts.objects.bulk_create(products, ignore_conflicts=True)
        total_saved += len(products)

        options = []
        for opt in option_list:
            try:
                product = DepositProducts.objects.get(fin_prdt_cd=opt['fin_prdt_cd'])
                options.append(
                    DepositOptions(
                        product=product,
                        fin_prdt_cd=opt.get('fin_prdt_cd', ''),
                        intr_rate_type_nm=opt.get('intr_rate_type_nm', ''),
                        intr_rate=float(opt.get('intr_rate') or 0),
                        intr_rate2=float(opt.get('intr_rate2') or 0),
                        save_trm=int(opt.get('save_trm') or 0),
                    )
                )
            except DepositProducts.DoesNotExist:
                continue

        DepositOptions.objects.bulk_create(options)
        page += 1
    return Response({'saved_items': len(base_list)}, status=status.HTTP_201_CREATED)

    

# 이거가능 
# path('deposit-products/', views.deposit_products, name='deposit'),
# datas/deposit-products/
@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 이거불가능
# /finlife/deposit-product-options/<str:fin_prdt_cd>
# @api_view(['GET'])
# def deposit_product_options(request):
#     if request.method == 'GET':
#         products = DepositProducts.objects.all()
#         DepositOptions.objects.get(fin_prdt_cd=products['fin_prdt_cd'])


# 이거가능
# path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_product_options, name='depositopt'),
# datas/deposit-product-options/<str:fin_prdt_cd>/
# @api_view(['GET'])
# def deposit_product_options(request, fin_prdt_cd):
#     try:
#         product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
#     except DepositProducts.DoesNotExist:
#         return Response({'error': '상품이 존재하지 않습니다'}, status=status.HTTP_404_NOT_FOUND)
    
#     options = product.options.all()  # related_name 사용
#     serializer = DepositOptionsSerializer(options, many=True)
#     return Response(serializer.data)



# 이거불가능
# finlife/deposit-products/top-rate/
# @api_view(['GET'])
# def top_rate(request):
    # 금리가 가장 높은 옵션을 찾기 
    # 그 옵션의 외래키로 설정되어있는 금융 상품 찾기 



# 이거가능
# @api_view(['GET'])
# def top_rate(request):
#     top_option = DepositOptions.objects.order_by('-intr_rate2').first()

#     if not top_option:
#         return Response({'message': '옵션 데이터가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

#     product = top_option.product
#     product_serializer = DepositProductsSerializer(product)
#     option_serializer = DepositOptionsSerializer(DepositOptions.objects.filter(product=product), many=True)

#     return Response({
#         'product': product_serializer.data,
#         'options': option_serializer.data
#     })


def input_my_data(request):
    # context = {
    #     'form': form,
    #     'products': products,
    # }
    # return render(request, 'datas/main.html', context)
    return render(request, 'datas/main.html')



def filter_by_mine(request):
    products = None

    if request.method == 'POST':
        form = MyDataForm(request.POST)
        if form.is_valid():
            # 사용자가 선택한 기간 (정수)
            schedule = form.cleaned_data['schedule']

            # DepositOptions.save_trm < schedule 인 DepositProducts 조회
            # related_name='options' 를 통해 DepositOptions에 접근
            products = (
                DepositProducts.objects
                .filter(options__save_trm__lt=schedule)
                .distinct()
            )
    else:
        form = MyDataForm()
    context = {
        'form': form,
        'products': products,
    }
    # return render(request, 'datas/filter.html', context )
    return render(request, 'datas/main.html', context )
    