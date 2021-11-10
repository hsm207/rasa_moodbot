# Introduction

This repo is an example of this rasa oss bug on the [use_entities feature](https://github.com/RasaHQ/rasa/issues/10137).

# Usage

To view the results of the bug:

```bash
make check-bug
```

The bug does not exist if only one domain file is used:

```bash
make check-notbug
```

The workaround is to repeat the list of entities in `domain.yml` in `foo.yml`:

```bash
make check-workaround
```