from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.views import APIView

from django.db.models import Count

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


# Create your views here.


# vue와 연결해줄거임 
# class ArticleCreateView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(author=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         print(serializer.errors)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

User = get_user_model()

class ArticleCreateView(APIView):
    def post(self, request):
        try:
            token_key = request.data.get('token')
            if not token_key:
                return Response({'error': '토큰이 필요합니다.'}, status=400)

            try:
                token = Token.objects.get(key=token_key)
                user = token.user

            except Token.DoesNotExist:

                return Response({'error': '유효하지 않은 토큰입니다.'}, status=401)

            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid():
                article = serializer.save(author=user)

                return Response(serializer.data, status=201)

            return Response(serializer.errors, status=400)

        except Exception as e:
            import traceback
            print("🔥 예외 발생:", e)
            traceback.print_exc()
            return Response({'error': '서버 내부 오류'}, status=500)







@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # 전체 게시글 데이터 조회
        articles = Article.objects.all()
        # articles는 django에서는 쓸 수 있는 queryset 데이터 타입이기 때문에
        # 우리가 만든 모델시리얼라이저로 변환 진행
        serializer = ArticleListSerializer(articles, many=True)
        # DRF에서 제공하는 Response를 사용해 JSON 데이터를 응답
        # JSON 데이터는 serializer의 data 속성에 존재
        return Response(serializer.data)

    # 게시글 생성 요청에 대한 응답
    elif request.method == 'POST':
        # 예전 코드
        # form = ArticleFrom(request.POST)
        # 사용자가 보낸 ㅈ데이터를 클래스로 받아서 직렬화
        serializer = ArticleSerializer(data=request.data)
        # 유효성 검사
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # 단일 게시글 데이터 조회
    article = Article.objects.get(pk=article_pk)
    # 단일 게시글 데이터 조회 + 그 단일 게시글에 작성된 댓글의 개수도 계산해달라고 DB에 한번에 요청
    article = Article.objects.annotate(num_of_comments=Count('comment')).get(pk=article_pk)
    # 기존에 article 객체에는 없었지만 결과에만 잠시 포함된 신규 데이터 (실제 article 테이블의 컬럼이 변한 것은 아님)
    print(article.num_of_comments)  # 특정 게시글의 댓글 개수

    if request.method == 'GET':
        # ArticleSerializer 클래스로 직렬화를 진행
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        # 사용자가 보낸 수정 데이터를 직렬화
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        # serializer = ArticleSerializer(instance=article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def comment_list(request):
    # 댓글 전체 조회
    comments = Comment.objects.all()
    # 댓글 데이터를 가공
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    # 특정 댓글 데이터를 조회
    comment = Comment.objects.get(pk=comment_pk)

    if request.method == 'GET':
        # 조회한 단일 댓글 데이터를 가공
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # 사용자가 보낸 새로운 댓글 데이터와 기존 데이터를 활용해 가공
        serializer = CommentSerializer(comment, data=request.data)
        # 유효성 검사
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    # 어떤 게시글에 작성되는 댓글인지 단일 게시글을 조회
    article = Article.objects.get(pk=article_pk)
    # 사용자가 보낸 댓글 데이터를 활용해 가공
    serializer = CommentSerializer(data=request.data)
    # 유효한지 검사
    if serializer.is_valid(raise_exception=True):
        # 추가 데이터를 save 메서드의 인자로 작성
        serializer.save(article=article, comment_author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
