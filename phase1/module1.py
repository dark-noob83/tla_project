from phase0.FA_class import DFA, State
from utils import utils
from utils.utils import imageType


def solve(image: imageType) -> 'DFA':
    dfa = DFA()
    i = j = 0
    dfa.add_state(0)
    while True:
        u_i = dfa.get_state_by_id(i)
        for k in range(4):

            ...

if __name__ == "__main__":
    image = [[1, 1, 1, 1],
             [1, 0, 1, 0],
             [0, 1, 0, 1],
             [1, 1, 1, 1]]

    utils.save_image(image)
    fa = solve(image)
    print(fa.serialize_json())
