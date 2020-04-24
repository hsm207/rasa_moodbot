from hyperopt import hp

search_space = {"epochs": hp.qloguniform("epochs", 0, 8, 2)}
