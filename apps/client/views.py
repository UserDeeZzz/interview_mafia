import logging

from django.http import JsonResponse
# Create your views here.
from django.views import View
from django_redis import get_redis_connection
from django.conf import settings
from .forms import LeaderBoardForm, SearchRankForm
from .models import LeaderBoard

logger = logging.getLogger('apps.client.view')

class LeaderBoardView(View):
    """
    URL:/api/client/leader_board
        leader board view
        client update new score
    """

    def get(self, request):
        """
        redis cache implement dynamic rank
        """
        valid_res = SearchRankForm(request.GET)
        # if form fields valid
        if valid_res.is_valid():
            client = valid_res.cleaned_data.get('client')
            logger.debug(f"用户请求client:{client}")
            # get current client rank idx
            coon = get_redis_connection(settings.RANK_REDIS_POOL)
            # notice: distinguish None or 0
            idx = coon.zrevrank(settings.RANK_REDIS_ZSET, client)
            # 　redis cache exists client
            if isinstance(idx, int):
                # via rank get score
                res = coon.zrevrange(settings.RANK_REDIS_ZSET, idx, idx + 1, withscores=True)
                score = res[0][1]
                # get leader board info
                start = valid_res.cleaned_data.get('start')
                end = valid_res.cleaned_data.get('end')
                res = self.get_rank(start, end)
                # 　append to the tail
                res.append({'order': idx + 1, 'client': client, 'score': score})
                code = 10000
            else:
                code = 10002
                res = f"您要查询的< {client} >不存在"
        else:
            code = 10001
            res = valid_res.errors
        return JsonResponse({
            "info": res, "code": code
        })

    def post(self, request):
        """
            client update score
        :param request:
        :return:
        """
        valid_res = LeaderBoardForm(request.POST)
        if valid_res.is_valid():
            score = valid_res.cleaned_data.get('score')
            client = valid_res.cleaned_data.get('client')
            logger.debug(f"用户POST请求:{client},{score}")
            # add to redis
            conn = get_redis_connection(settings.RANK_REDIS_POOL)
            conn.zadd(settings.RANK_REDIS_ZSET, {client: score})
            # add to mysql
            lb, created = LeaderBoard.objects.update_or_create(
                defaults=dict(score=score), client=client
            )
            mode = 'create' if created else 'update'
            res = f"{lb.client} : success {mode} score"
            code = 10000
        else:
            res, code = valid_res.errors, 10001
        return JsonResponse({"info": res, "code": code})

    @staticmethod
    def get_rank(start, end):
        """
        the clients between start and end
        :param start:
        :param end:
        :return:
        """
        conn = get_redis_connection(settings.RANK_REDIS_POOL)
        clients = conn.zrevrange(settings.RANK_REDIS_ZSET, start, end, withscores=True)
        ranks = [{'order': i + start + 1, 'client': c[0].decode(), 'score': c[1]} for i, c in
                 enumerate(clients)]
        return ranks
