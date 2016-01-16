# repo-compare

Simple lib to compare github repositories


## WIP

This projects is under development!


## About

This is a simple project to compare repositories from Github, based on repository data.
For now, the program compare only:

- Stars
- Forks
- Watchers


## Instructions

- Clone the repository:

```sh
$ git clone https://github.com/feliperuhland/repo-compare.git
$ cd repo-compare
```

- Execute python file:

```sh
$ ./compare -h
```

- Compare repositories

```sh
$ ./compare.py mitsuhiko/flask django/django tornadoweb/tornado
mitsuhiko/flask   : [++ ] 2
django/django     : [+  ] 1
tornadoweb/tornado: [   ] 0
```

