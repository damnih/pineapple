from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm

from rest_framework.authtoken.models import Token

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserCreationSerializer

from rest_framework.permissions import AllowAny


# Create your views here.


class SignupView(APIView):
    def post(self, request):
        serializer = CustomUserCreationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "회원가입 성공"}, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"errors": serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )


class LoginView(APIView):
    authentication_classes = []      # 로그인 자체는 인증이 필요 없으니 비워 둡니다
    permission_classes = [AllowAny]



    def post(self, request):
        print("Incoming data:", request.data)  
        # 1) 요청 데이터에서 id, pw 추출
        username = request.data.get('id')
        password = request.data.get('pw')

        # 2) 인증 시도
        user = authenticate(username=username, password=password)
        print("Authenticated user:", user)
        if not user:
            # 인증 실패
            return Response(
                {'errors': '아이디 또는 비밀번호가 잘못되었습니다.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 3) 인증 성공 → 토큰 발급(또는 기존 토큰 가져오기)
        # token, _ = Token.objects.get_or_create(user=user)

        token, created = Token.objects.get_or_create(user=user)
        print("Token:", token.key, "created?", created)

        return Response({'key': token.key}, status=status.HTTP_200_OK)


        # # 4) 토큰 반환
        # return Response(
        #     {'key': token.key},
        #     status=status.HTTP_200_OK
        # )


# class LoginView(APIView):
#     def post(self, request):



# def login(request):
#     if request.user.is_authenticated:
#         return redirect('articles:index')

#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             # auth_login(request, 로그인 인증된 유저 객체)
#             auth_login(request, form.get_user())
#             return redirect('articles:index')
#     else:
#         form = AuthenticationForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/login.html', context)


# @login_required
# def logout(request):
#     auth_logout(request)
#     return redirect('articles:index')




# def signup(request):
#     if request.user.is_authenticated:
#         return redirect('articles:index')
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save() # 폼 저장하구 
#             return redirect('articles:index')
        
#     else:
#         # 회원가입 템플릿과 회원정보 작성을 위한 폼을 올림 
#         # 그렇다면 폼 인스턴스가 필요~! 
#         # form = 유저인포 
#         # 아 그렇다면 이거 임포트가 필요하겠다 임포트하러 맨위로 가자! 
#         form = CustomUserCreationForm()
#     context = {
#         "form": form,
#     }
#     return render(request, 'accounts/signup.html', context)



# def signup(request):
#     if request.user.is_authenticated:
#         return redirect('articles:index')

#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('articles:index')
#     else:
#         # 회원가입 템플릿과 회원정보 작성을 위한 form을 응답
#         form = CustomUserCreationForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/signup.html', context)


# 유저 객체를 삭제
@login_required
def delete(request):
    # 유저를 조회해야 할까? 필요 없음
    # 애초에 탈퇴라는건 로그인이 되어있는 상태로 요청을 보내기 때문
    # 그래서 요청 객체안에 이미 어떤 사용자가 요청을 보내는 건지 정보가 들어있음
    # request.user
    # print(request.user)
    request.user.delete()
    return redirect('articles:index')


@login_required
def update(request):
    if request.method == 'POST':
        # 기존 유저 정보 (request.user)
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        # form = PasswordChangeForm(request.user, data=request.POST)
        # form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
