from django.shortcuts import render, redirect
import requests 
from django.conf import settings 
from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, DepositResultSerializer
# from django.contrib.auth.decorators import 

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DepositOptions
from .serializers import DepositResultSerializer
from rest_framework.decorators import api_view

from rest_framework import status
from django.http import JsonResponse

from .forms import MyDataForm

from datetime import datetime, timedelta

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
    



# 믿기./


class DepositResultAPIView(APIView):
    def get(self, request):
        schedule = int(request.query_params.get('schedule_ans', 0))
        dest = request.query_params.get('destination_ans')
        budget = float(request.query_params.get('budget_ans', 0))

        qs = DepositOptions.objects.filter(save_trm__lte=schedule) \
                .select_related('product')

        # if dest:
        #     qs = qs.filter(product__destination__iexact=dest)

        top4 = qs.order_by('-intr_rate2')[:4]

        data = []
        for opt in top4:
            rate = opt.intr_rate2
            if opt.intr_rate_type_nm == '단리':
                maturity = budget * (1 + ( rate / 100 )  * (schedule / 12))
            else:
                maturity = budget * (1 + ( rate / 100 ) )  ** (schedule / 12)

            data.append({
                **DepositResultSerializer(opt).data,
                'maturity_amount': round(maturity, 0),
            })

        return Response(data)


# 한국은행 api 접속 위한 함수
def exchange_rate(request, code):
    today = datetime.now()

    # 매월 1일부터의 환율 데이터를 가져옴
    today_str = today.strftime('%Y%m%d')
    month_first = today_str[:6] + '01'
    
    API_KEY = settings.BOK_API_KEY
    url = f'https://ecos.bok.or.kr/api/StatisticSearch/{API_KEY}/json/kr/1/100/731Y001/D/{month_first}/{today_str}/{code}'

    try:
        response = requests.get(url)
        data = response.json()
        rows = data.get('StatisticSearch', {}).get('row', [])

        # 주말 등 값이 없는 날짜는 자동 필터링
        cleaned_data = [
            {'date': r['TIME'], 'rate': r['DATA_VALUE']}
            for r in rows
            if 'DATA_VALUE' in r
        ]

        return JsonResponse({'rates': cleaned_data})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
@api_view(['GET'])
def deposit_result_detail(request, id):
    try:
        option = DepositOptions.objects.get(pk=id)
    except DepositOptions.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)
    
    serializer = DepositResultSerializer(option)
    return Response(serializer.data)
