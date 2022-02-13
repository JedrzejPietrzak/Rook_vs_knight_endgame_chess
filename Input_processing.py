# the credit for the Dataset belongs to UCI
from functions import *
import pandas as pd

def main():
    # Since the model was tested, where the white king can only be within the left low corner, I warn the user of such situation

    display('Please remeber, that the white king is supposed to be withing A-D, and 1-4 range\n')
    display('Also in the program, we assume, that the user knows how to play chess\n')

    # taking the initial position

    wh_king_position =[i for i in take_input('State the current position of the white King: ').lower()]
    rook_position = [i for i in take_input('State the current position of the rook: ').lower()]
    blk_king_position = [i for i in take_input('State the current position of the black King: ').lower()]
    # display(wh_king_position)


    init_positions = wh_king_position + rook_position + blk_king_position

    checked_data = pd.DataFrame([init_positions], columns=['a', '1', 'b', '3', 'c', '2'])
    needed_df = pd.DataFrame(
        {
            'a': ['a', 'b', 'c', 'd','a', 'b', 'c', 'd'],
            '1': [1, 1, 1, 1, 1, 1, 1, 1],
            'b': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
            '3': [1, 1, 1, 1, 1, 1, 1, 1],
            'c': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
            '2': [1, 1, 1, 1, 1, 1, 1, 1]
        }
    )
    checked_data = pd.concat([checked_data, needed_df], keys=['data', 'useless'], axis=0)


    wh_king_pos = pd.get_dummies(checked_data['a']).rename(columns={'a':'wa','b':'wb','c':'wc','d':'wd'})
    rook_pos = pd.get_dummies(checked_data['b']).rename(columns={'a':'Wa','b':'Wb','c':'Wc','d':'Wd'})
    blk_king_pos = pd.get_dummies(checked_data['c'])
    checked_data.drop(['a', 'b', 'c'], axis=1, inplace=True)
    checked_data = pd.concat([checked_data, wh_king_pos, rook_pos, blk_king_pos], axis=1)

    # Final step, where we provide the answer from the model
    from The_machine import knn
    prediction = knn.predict(checked_data.loc['data'])

    if prediction == [1]:
        display('The player should win the game.')
    else:
        display('The player should not win the game.')


if __name__ == '__main__':
    main()