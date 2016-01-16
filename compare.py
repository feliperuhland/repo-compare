#!/usr/bin/env python
# coding: utf-8

import argparse

from repo import Repo, Report


def compare(*repository):
    report = Report([Repo(full_name) for full_name in repository])
    report.test_score()
    report.show_result()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('repository', help='Repositories to compare', type=str, nargs='+')
    args = parser.parse_args()
    compare(*args.repository)
