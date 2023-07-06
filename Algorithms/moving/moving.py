'''
Module 4: Moving Boxes
Akshay Choksi (ajc9yr)
Greedy Algorithms
'''



def cost_calculator(x_cost, y_cost, total_boxes, keep_boxes):
    diff = y_cost - x_cost
    total_cost = 0
    while(True):
        if (total_boxes + 1) // 2 > keep_boxes:
            total_cost+=y_cost
            total_boxes = total_boxes - (total_boxes+1)//2
        else:
            total_cost+= (x_cost * (total_boxes - keep_boxes))
            break
    return total_cost

#Read input
number_of_cases = int(input())
for i in range(number_of_cases):
    box_number, keep_number, company_number = (input().split())
    box_number = int(box_number)
    keep_number = int(keep_number)
    company_number = int(company_number)
    ret = []
    for j in range(company_number):
        company, x_cost, y_cost = input().split()
        x_cost = int(x_cost)
        y_cost = int(y_cost)
        min_cost = cost_calculator(x_cost,y_cost, box_number, keep_number)
        ret.append([company, min_cost])
    ret.sort(key=lambda cost: (cost[1], cost[0]))
    print("Case", str(i+1))
    for provider, cost in ret:
        print(provider, str(cost))