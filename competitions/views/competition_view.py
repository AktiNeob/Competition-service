import logging
from .base_view import BaseView
from ..models import Competitions
import json

log = logging.getLogger('competitions_log')


class CompetitionsView(BaseView):

    @BaseView.authorization(('admin', 'anonymous'))
    def get(self, request, client, client_id):
        params = request.GET
        response = list(Competitions.objects.filter(**params).values())
        # stat = BaseView.send_stat_log(request, client, client_id)
        # if not stat:
        BaseView.log(log, request, client, client_id)
        return {'status': 'Success', 'data': response, 'code': 200}

    @BaseView.authorization(('admin', 'anonymous'))
    def post(self, request, client, client_id):
        data = json.loads(request.body.decode('utf-8'))
        response = Competitions.objects.create(**data).pk
        # stat = BaseView.send_stat_log(request, client, client_id)
        # if not stat:
        BaseView.log(log, request, client, client_id)
        return {'status': 'Success', 'data': response, 'code': 200}

class CompetitionView(BaseView):

    @BaseView.authorization(('admin', 'anonymous'))
    def get(self, request, uuid, client, client_id):
        response = list(Competitions.objects.filter(pk=uuid).values())
        if not response:
            return {'status': 'Failed', 'message': 'Object does not exist', 'code': 404}
        # stat = BaseView.send_stat_log(request, client, client_id)
        # if not stat:
        BaseView.log(log, request, client, client_id)
        return {'status': 'Success', 'data': response, 'code': 200}

    @BaseView.authorization(('admin', 'anonymous'))
    def patch(self, request, uuid, client, client_id):
        data = json.loads(request.body.decode('utf-8'))
        Competitions.objects.filter(pk=uuid).update(**data)
        response = list(Competitions.objects.filter(pk=uuid).values())
        # stat = BaseView.send_stat_log(request, client, client_id)
        # if not stat:
        BaseView.log(log, request, client, client_id)
        return {'status': 'Success', 'data': response, 'code': 200}

    @BaseView.authorization(('admin', 'anonymous'))
    def delete(self, request, uuid, client, client_id):
        entry = Competitions.objects.filter(pk=uuid)
        entry.delete()
        # stat = BaseView.send_stat_log(request, client, client_id)
        # if not stat:
        BaseView.log(log, request, client, client_id)
        return {'status': 'Success', 'code': 200}