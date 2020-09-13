import logging
from .base_view import BaseView
from ..models import Competitors, Competitions
import json
from django.conf import settings
import requests
from requests.exceptions import Timeout

log = logging.getLogger('competitors_log')



class CompetitorsView(BaseView):

    @BaseView.authorization(('admin', 'anonymous'))
    def get(self, request, competition_uuid, client, client_id):
        params = dict(request.GET)
        params['competition'] = str(competition_uuid)
        response = list(Competitors.objects.filter(**params).values())
        # stat = BaseView.send_stat_log(request, client, client_id)
        # if not stat:
        BaseView.log(log, request, client, client_id)
        return {'status': 'Success', 'data': response, 'code': 200}


    @BaseView.authorization(('admin', 'anonymous'))
    def post(self, request, competition_uuid, client, client_id):
        data = json.loads(request.body.decode('utf-8'))
        competition = Competitions.objects.filter(pk=competition_uuid)
        if not competition:
            return {'status': 'Failed', 'message': 'Not found', 'code': 404}
        data['competition'] = competition[0]
        member = Competitors.objects.create(**data)
        response = member.pk
        # stat = BaseView.send_stat_log(request, client, client_id)
        # if not stat:
        BaseView.log(log, request, client, client_id)
        return {'status': 'Success', 'data': response, 'code': 200}

class CompetitorView(BaseView):

    @BaseView.authorization(('admin', 'anonymous'))
    def get(self, request, uuid, client, client_id):
        response = list(Competitors.objects.filter(pk=uuid).values())
        if not response:
            return {'status': 'Failed', 'message': 'Object does not exist', 'code': 404}
        # stat = BaseView.send_stat_log(request, client, client_id)
        # if not stat:
        BaseView.log(log, request, client, client_id)
        return {'status': 'Success', 'data': response, 'code': 200}


    @BaseView.authorization(('admin', 'anonymous'))
    def delete(self, request, uuid, client, client_id):
        entry = Competitors.objects.filter(pk=uuid)

        if not entry:
            return {'status': 'Failed', 'message': 'Not found', 'code': 404}

        entry.delete()
        # stat = BaseView.send_stat_log(request, client, client_id)
        # if not stat:
        BaseView.log(log, request, client, client_id)
        return {'status': 'Success', 'code': 200}