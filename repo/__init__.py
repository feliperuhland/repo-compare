# coding: utf-8

import sys

import requests

GITHUB_URL = 'https://api.github.com/repos'


def _get_bar(num, total):
    return ('+' * num) + (' ' * (total - num))


class Repo(object):
    def __init__(self, full_name):
        self.full_name = full_name
        self.name = None
        self.stars = None
        self.forks = None
        self.subscribers = None
        self.pushed_at = None
        self.created_at = None
        self.updated_at = None
        self._update_attrs(full_name)

    def _update_attrs(self, full_name):
        url = '{}/{}'.format(GITHUB_URL, full_name)
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception('Repository not found: {}'.format(full_name))

        _json = response.json()
        self.name = _json['name']
        self.stars = _json['stargazers_count']
        self.forks = _json['forks_count']
        self.subscribers = _json['subscribers_count']
        self.pushed_at = _json['pushed_at']
        self.created_at = _json['created_at']
        self.updated_at = _json['updated_at']

    def __repr__(self):
        return '<Repo: {}>'.format(self.full_name)


class Report(object):
    fields = {
        'created_at': min,
        'forks': max,
        'pushed_at': max,
        'stars': max,
        'subscribers': max,
        'updated_at': max,
    }

    def __init__(self, repos):
        self.repos = repos
        self.score = {repo.full_name: {'total': 0} for repo in self.repos}
        self.col_width = max(len(repo.full_name) for repo in self.repos)

    def get_best_value(self, func, field):
        return func([getattr(repo, field) for repo in self.repos])

    def test_score(self):
        for field in self.fields:
            best = self.get_best_value(max, field)
            for repo in self.repos:
                if getattr(repo, field) == best:
                    self.score[repo.full_name][field] = 1
                    self.score[repo.full_name]['total'] += 1

    def show_result(self):
        for repo in self.repos:
            sys.stdout.write('{}: [{}] {}\n'.format(
                repo.full_name.ljust(self.col_width),
                _get_bar(self.score[repo.full_name]['total'], len(self.fields)),
                self.score[repo.full_name]['total']
            ))
