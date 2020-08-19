# sandwich_orders = ['hanbao','kele','shutiao']
# finished_sandwiches = []
#
# while sandwich_orders:
#
#     sandwich_order = sandwich_orders.pop()
#     print("Show to list:" + sandwich_order.title())
#     finished_sandwiches.append(sandwich_order)
#
# print("\nI made your tuna sandwich:" )
# for finished_sandwiche in finished_sandwiches:
#     print(finished_sandwiche.title())
#

sandwich_orders = ['pastrami','hanbao','pastrami','kele','pastrami','shutiao']
finished_sandwiches = []
print("Five cigarettes of bacon are sold out")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_order)
print("\nWhat's left:")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())



