import configparser

cfg = configparser.ConfigParser()
cfg.read("config.cfg")
fn = cfg["file"]["file"]
r_word = cfg["word_to_replace"]["word"]
n_word = cfg["new_word"]["word"]
with open(fn, "r") as f:
    s = f.read()
with open(fn, "w") as f:
    f.write(s.replace(r_word, n_word))

