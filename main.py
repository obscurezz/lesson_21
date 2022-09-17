from fixtures import test_shop, test_store
from request_class import Request


def main():
    print('Input a string, formatted like @Deliver <amount> <item> from <store> to <shop>@')
    user_input = input()
    user_request = Request(store=test_store, shop=test_shop, message=user_input)
    print(user_request)

    if test_store.items[user_request.item] >= user_request.amount:
        print(f'We have the right amount in {user_request.from_keyword}')

        try:
            print(f'The courier took {user_request.amount} {user_request.item} from the {user_request.from_keyword}')
            user_request.store.remove(user_request.item, user_request.amount)

            print(f'The courier carries {user_request.amount} {user_request.item} from the {user_request.from_keyword} '
                  f'to the {user_request.to_keyword}')
            user_request.shop.add(user_request.item, user_request.amount)

            print(f'The courier delivered {user_request.amount} {user_request.item} to the {user_request.to_keyword}')

            print('Items in the store:\n', test_store.get_items())
            print('Items in the shop:\n', test_shop.get_items())
        except ValueError:
            print('There is not enough space in the shop, try something else')
    else:
        print(f'We do not have the right amount in {user_request.from_keyword}, try to order lesser value')


if __name__ == '__main__':
    main()
