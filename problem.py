#encoding: utf-8

def mudar(valor):
    if valor == "off":
        return "on"
    else:
        return "off"

def lampadas(num):
    result = num * ["off"]

    for volta in range(1, num+1):
        for lamp in range(1, num+1):
            if lamp % volta == 0:
                result[lamp - 1] = mudar(result[lamp - 1])
            

    # if num == 1:
    #     result[0] = mudar(result[0])   
    # elif num == 2:
    #     result[0] = mudar(result[0])
    #     result[1] = mudar(result[1])
    #     result[1] = mudar(result[1])
    # elif num == 3:
    #     result[0] = mudar(result[0])
    #     result[1] = mudar(result[1])
    #     result[2] = mudar(result[2])
    #     result[1] = mudar(result[1])
    #     result[2] = mudar(result[2])
    # elif num == 5:
    #     result[0] = mudar(result[0])
    #     result[1] = mudar(result[1])
    #     result[2] = mudar(result[2])
    #     result[3] = mudar(result[3])
    #     result[4] = mudar(result[4])
    #     result[1] = mudar(result[1])
    #     result[3] = mudar(result[3])
    #     result[2] = mudar(result[2])
    #     result[3] = mudar(result[3])
    #     result[4] = mudar(result[4])

    return result
