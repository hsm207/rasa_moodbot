# Introduction

Illustration the effect of the `max_history` parameter in a dialog policy

# Usage

1. Run:
``bash
rasa train -c config_max_hist_2.yml --out models/max_hist_2 && \
    rasa train -c config_max_hist_3.yml --out models/max_hist_3 
```

2. Load each trained model e.g:
```bash
rasa shell --model models/max_hist_2 -vv
```

3. Test with the following conversation:
```bash
/ask_how_to_install
/ask_weather
```
The model trained with config `config_max_hist_2.yml` will predict action listen but the one trained with config `config_max_hist_3.yml` will predict the correct action i.e. `utter_continue_install`.
