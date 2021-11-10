# Introduction

This repo is an example of this rasa oss bug on the [use_entities feature](https://github.com/RasaHQ/rasa/issues/10137).

# Usage

To view the results of the bug:

```bash
make check-bug
```

![image](https://user-images.githubusercontent.com/2398765/141085389-c86fea0b-f8b4-4195-bd7a-7469961a72f5.png)


The bug does not exist if only one domain file is used:

```bash
make check-notbug
```
![image](https://user-images.githubusercontent.com/2398765/141085469-a6f27295-45e3-4bda-8d0a-34fd1bf4d875.png)


The workaround is to repeat the list of entities in `domain.yml` in `foo.yml`:

```bash
make check-workaround
```

![image](https://user-images.githubusercontent.com/2398765/141085508-33252549-ac7d-406d-a5b5-6e9d84f44ea1.png)
