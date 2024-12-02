## create empty files nameed 'munual_ans_{i}.txt', where i is from 0 to 44.

def create_empty_files():
    for i in range(45):
        with open(f'munual_ans_{i}.txt', 'w') as f:
            pass
    return None

if __name__ == '__main__':
    create_empty_files()