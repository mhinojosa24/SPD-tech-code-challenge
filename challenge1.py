from linkedlist import LinkedList




'''
Find the middle item in a singly linked list,
or two middle items if it contains an even number of nodes.

'''

def find_list_size(list):
    size_for_list = 0
    node = list.head

    while node is not None:
        size_for_list += 1
        node = node.next
    return size_for_list


def find_mid_val(list):
    size = find_list_size(list)
    curr_count = 0
    node = list.head
    mid = size // 2

    while node is not None:
        if mid == curr_count:
            return node.data
        node = node.next
        curr_count += 1

def main():
    list = LinkedList(['f', 't', 'r', 'l'])


if __name__ == '__main__':
    main()
