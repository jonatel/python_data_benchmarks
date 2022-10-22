
import random
import string
import pickle
import time


N_ROWS = 1_000_000
N_KEYS = 100
MIN_STR = 10
MAX_STR = 100
PRINTABLE = string.ascii_letters + string.digits + " "


def set_key_value(dtype):
    if dtype == int:
        return random.randint(0, 1_000_000)
    elif dtype == float:
        return random.random()
    elif dtype == str:
        k = random.randint(MIN_STR, MAX_STR)
        return "".join(random.choices(PRINTABLE, k=k))


def main():
    tini = time.perf_counter()
    # create random data as list of dicts
    key_types = (int, float, str)
    keys = [(f"key_{i}", random.choice(key_types)) for i in range(N_KEYS)]
    dataset = [
        {
            key[0]:set_key_value(key[1])
            for key in keys
        }
        for _ in range(N_ROWS)
    ]
    tend = time.perf_counter()
    print(f"dataset created in {round((tend - tini) / 60, 2)} minutes")
    # save dataset
    with open("data/dataset.pickle", 'wb') as file:
        pickle.dump(dataset, file)
    with open("data/keys.pickle", 'wb') as file:
        pickle.dump(keys, file)
    print("dataset saved")


if __name__ == "__main__":
    main()