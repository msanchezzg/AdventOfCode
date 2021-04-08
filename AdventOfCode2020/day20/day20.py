#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys
from image import Image, Matrix


sea_monster = (
    ('.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.'),
    ('#', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', '#', '#'),
    ('.', '#', '.', '.', '#', '.', '.', '#', '.', '.', '#', '.', '.', '#', '.', '.', '#', '.', '.', '.')
)


def match_in_group(placed_imgs, frame):
    matched = False

    for pf in placed_imgs:
        # If pf does not have top neigh, try to match with frame
        if pf.top_neigh is None and frame.bottom_neigh is None:
            if pf.match_top_border(frame):
                matched = True
                continue
        # If pf does not have bottom neigh, try to match with frame
        if pf.bottom_neigh is None and frame.top_neigh is None:
            if pf.match_bottom_border(frame):
                matched = True
                continue
        # If pf does not have left neigh, try to match with frame
        if pf.left_neigh is None and frame.right_neigh is None:
            if pf.match_left_border(frame):
                matched = True
                continue
        # If pf does not have right neigh, try to match with frame
        if pf.right_neigh is None and frame.left_neigh is None:
            if pf.match_right_border(frame):
                matched = True
                continue

    return matched

def sort_imgs(placed_imgs, non_placed_imgs):
    """
    Sort images (find their top, bottom, left and right neighbors) which are part of
    a big image using a backtracking strategy.

    Args:
        placed_imgs (list(Image)): Images already sorted.
        non_placed_imgs (list(Image)): Images with no neighbors yet.

    """

    if len(non_placed_imgs) == 0:
        return True

    img = non_placed_imgs.pop(0)
    rotations = img.pixels_matrix.get_all_rotations()

    for rot in rotations:
        rot_img = Image(rot, img.id)
        rot_img.reset_neighs()

        res = match_in_group(placed_imgs, rot_img)
        if res:
            placed_imgs.append(rot_img)
            if sort_imgs(placed_imgs, non_placed_imgs):
                return True

            rot_img = placed_imgs.pop(-1)
            rot_img.reset_neighs()

    non_placed_imgs.append(img)
    return sort_imgs(placed_imgs, non_placed_imgs)


def append_imgs_rows(left_frame, row_index, remove_border=False):
    """
    Get a big row as the concatenation of the same row of
    horizontally adjacent images.

    Args:
        left_frame (Image): Left extreme of the row of images.
        row_index (int): Index of the row to append.
        remove_border (bool, optional): If true, the row border (the first and last pixel)
            is not included. Defaults to False.

    Returns:
        [type]: [description]
    """

    row = []
    while True:
        r = left_frame.pixels_matrix.get_row(row_index)
        if remove_border:
            r = r[1:-1]
        row += r
        left_frame = left_frame.right_neigh
        if left_frame is None:
            break
    return row


def is_sea_monster(image):
    if len(image) != len(sea_monster):
        return False

    for i, sea_monster_row in enumerate(sea_monster):
        image_row = image[i]

        if len(sea_monster_row) != len(image_row):
            return False

        for j, sea_monster_elem in enumerate(sea_monster_row):
            sea_monster_elem = sea_monster_row[j]
            image_elem = image_row[j]

            if sea_monster_elem == '.':
                continue
            if sea_monster_elem != image_elem:
                return False

    return True


def star2(top_left_corner):
    big_image = []

    frame_row_left = top_left_corner
    while True:
        for row_index in range(1, top_left_corner.pixels_matrix.get_nrows()-1):
            big_image.append(append_imgs_rows(frame_row_left, row_index, remove_border=True))

        frame_row_left = frame_row_left.bottom_neigh

        if frame_row_left is None:
            break

    image = Image(Matrix(big_image), 0)

    # Look for sea monsters
    rotations = image.pixels_matrix.get_all_rotations()
    num_monsters = 0
    sea_monster_rows = len(sea_monster)
    sea_monster_cols = len(sea_monster[0])

    for rot in rotations:
        if num_monsters != 0:
            break
        for row_index in range(0, rot.get_nrows() - sea_monster_rows):
            for col_index in range(0, rot.get_ncols() - sea_monster_cols):
                submatrix = rot.get_submatrix(row_index, row_index+sea_monster_rows-1, col_index, col_index+sea_monster_cols-1)
                if is_sea_monster(submatrix.matrix):
                    num_monsters += 1

    num_monster_hash = num_monsters * 15
    sea_roughness = image.count_pixels('#') - num_monster_hash

    print('PART 2')
    print(f'Number of sea monsters = {num_monsters}')
    print(f'Sea roughness = {sea_roughness}')


def main(input_file):

    with open(input_file, 'r') as f:
        lines = f.read().split('\n\n')

    image_pieces = []

    for line in lines:
        image = line.split('\n')
        image_id = int(image[0].split(' ')[-1][:-1])
        image_matrix = [list(row) for row in image[1:]]
        image_pieces.append(Image(Matrix(image_matrix), image_id))

    placed_imgs = [image_pieces[0]]
    not_placed_frames = image_pieces[1:]
    sort_imgs(placed_imgs, not_placed_frames)

    print('PART 1')

    print('Frames neighbors:')
    for frame in placed_imgs:
        print('\t', end='')
        frame.pretty_print_neighs()
    print()

    top_left_corner = None
    top_right_corner = None
    bottom_left_corner = None
    bottom_right_corner = None

    for frame in placed_imgs:
        if frame.top_neigh is None:
            if frame.left_neigh is None:
                top_left_corner = frame
            elif frame.right_neigh is None:
                top_right_corner = frame
        elif frame.bottom_neigh is None:
            if frame.left_neigh is None:
                bottom_left_corner = frame
            elif frame.right_neigh is None:
                bottom_right_corner = frame

    corners_product = top_left_corner.id * top_right_corner.id * bottom_left_corner.id * bottom_right_corner.id

    print(f'Top left corner: {top_left_corner.id}')
    print(f'Top right corner: {top_right_corner.id}')
    print(f'Bottom left corner: {bottom_left_corner.id}')
    print(f'Bottom right corner: {bottom_right_corner.id}')
    print()
    print(f'Corners IDs product = {corners_product}')

    print('\n------------------------------------------------\n')

    star2(top_left_corner)


if __name__ == "__main__":
    main(sys.argv[1])
