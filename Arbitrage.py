liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}
def dfs( current_currency, target_currency, target_amount,amount_so_far, path,path_amount, depth_limit):
    # 如果當前貨幣是目標貨幣並且擁有超過目標數量，返回True
    if current_currency == target_currency and amount_so_far >= target_amount:
        return True, path,path_amount

    # 遞歸深度限制
    if depth_limit <= 0:
        return False, None,None
    update_liquidity( path, path_amount)
    # 遍歷所有相鄰的貨幣
    for next_currency, next_now in liquidity[current_currency].items():
      next_amount = liquidity[next_currency][current_currency]-(liquidity[next_currency][current_currency]*liquidity[current_currency][next_currency]/(liquidity[current_currency][next_currency]+amount_so_far))
      next_amount = next_amount*0.997
      # 遞歸地探索下一個貨幣
      found,updated_path,updated_path_amount = dfs( next_currency, target_currency, target_amount,next_amount, path + [next_currency],path_amount+[next_amount] ,depth_limit - 1)
      if found:
          return True,updated_path, updated_path_amount

    # 如果無法找到符合條件的路徑，返回False
    return False, None,None

def find_path_dfs(liquidity, start_currency, target_currency, target_amount, max_depth=5):
    # 初始化初始金額和路徑
    start_amount = 5  # 起始代幣是5個tokenB
    start_path = [start_currency]
    start_path_amount=[start_amount]

    # 開始DFS搜索
    found, path,path_amount = dfs( start_currency, target_currency,target_amount, start_amount, start_path,start_path_amount, max_depth)
    if found:
      return path,path_amount
    else:
      return None

def update_liquidity( path, path_amount):
  liquidity = {
    "tokenA": {"tokenB": 17, "tokenC": 11, "tokenD": 15, "tokenE": 21},
    "tokenB": {"tokenA": 10, "tokenC": 36, "tokenD": 13, "tokenE": 25},
    "tokenC": {"tokenA": 7, "tokenB": 4, "tokenD": 30, "tokenE": 10},
    "tokenD": {"tokenA": 9, "tokenB": 6, "tokenC": 12, "tokenE": 60},
    "tokenE": {"tokenA": 5, "tokenB": 3, "tokenC": 8, "tokenD": 25},
    }
  if(len(path)>1): 
    for i in range(len(path) - 1):
      source, destination = path[i], path[i+1]
      # 減去換出的代幣，加入換入的代幣
      liquidity[source][destination] += path_amount[i]
      liquidity[destination][source] -= path_amount[i+1]

# 測試
#liquidity[source][destination]數量是source的
liquidity = {
    "tokenA": {"tokenB": 17, "tokenC": 11, "tokenD": 15, "tokenE": 21},
    "tokenB": {"tokenA": 10, "tokenC": 36, "tokenD": 13, "tokenE": 25},
    "tokenC": {"tokenA": 7, "tokenB": 4, "tokenD": 30, "tokenE": 10},
    "tokenD": {"tokenA": 9, "tokenB": 6, "tokenC": 12, "tokenE": 60},
    "tokenE": {"tokenA": 5, "tokenB": 3, "tokenC": 8, "tokenD": 25},
}

start_currency = "tokenB"  # 起始貨幣是tokenB
target_currency = "tokenB"  # 目標貨幣是tokenB（同樣的貨幣）
target_amount = 19

# 查找路徑
path,path_amount = find_path_dfs(liquidity, start_currency, target_currency, target_amount)
if path:

    print("path:tokenB",end='')
    for i in range (len(path)-1):
        print( "->",path[i+1],end='')
    print(", tokenB balance=",path_amount[-1])


else:
    print("找不到交換路徑")